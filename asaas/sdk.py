import logging
from abc import abstractclassmethod
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Dict, List, Optional, Type, Union
from black import err

import httpx
from httpx import Request, Response

from asaas.customer import Customer
from asaas.accounts import Accounts
from asaas.payments import Payments
from asaas.installments import Installments
from asaas.subscriptions import Subscriptions
from asaas.payment_link import Payment_Link

from asaas.errors import (
    APIResponseError,
    HTTPResponseError,
    RequestTimeoutError,
    is_api_error_code,
)

from asaas.typing import SyncAsync
from asaas.logging import make_console_logger


@dataclass
class ClientOptions:
    """Options to configure the client.
    Attributes:
        auth: Bearer token for authentication. If left undefined, the `auth` parameter
            should be set on each request.
        timeout_ms: Number of milliseconds to wait before emitting a
            `RequestTimeoutError`.
        base_url: The root URL for sending API requests. By default uses https://sandbox.asaas.com
        log_level: Verbosity of logs the instance will produce. By default, logs are
            written to `stdout`.
        logger: A custom logger.
        version: Asaas SDK version.
    """

    auth: Optional[str] = None
    timeout_ms: int = 60_000
    base_url: str = "https://sandbox.asaas.com"
    log_level: int = logging.WARNING
    logger: Optional[logging.Logger] = None
    version: str = "0.1.0"


class BaseClient:
    def __init__(
        self,
        client: Union[httpx.Client, httpx.AsyncClient],
        options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
        **kwargs: Any,
    ) -> None:
        if options is None:
            options = ClientOptions(**kwargs)
        elif isinstance(options, dict):
            options = ClientOptions(**options)

        self.logger = options.logger or make_console_logger()
        self.logger.setLevel(options.log_level)
        self.options = options

        self._clients: List[Union[httpx.Client, httpx.AsyncClient]] = []
        self.client = client
        self.customer = Customer(parent=self)
        self.accounts = Accounts(parent=self)
        self.payments = Payments(parent=self)
        self.installments = Installments(parent=self)
        self.subscriptions = Subscriptions(parent=self)
        self.payment_link = Payment_Link(parent=self)

    @property
    def client(self) -> Union[httpx.Client, httpx.AsyncClient]:
        return self._clients[-1]

    @client.setter
    def client(self, client: Union[httpx.Client, httpx.AsyncClient]) -> None:
        client.base_url = httpx.URL(self.options.base_url + "/api/v3")
        client.timeout = httpx.Timeout(timeout=self.options.timeout_ms / 1_000)
        client.headers = httpx.Headers(
            {
                "PythonSDK-Version": self.options.version,
                "User-Agent": "Python SDK",
            }
        )
        if self.options.auth:
            client.headers["access_token"] = f"{self.options.auth}"
        self._clients.append(client)

    def _build_request(
        self,
        method: str,
        path: str,
        query: Optional[Dict[Any, Any]] = None,
        body: Optional[Dict[Any, Any]] = None,
        auth: Optional[str] = None,
    ) -> Request:
        headers = httpx.Headers()
        if auth:
            headers["access_code"] = f"{auth}"
        self.logger.info(f"{method} {self.client.base_url}{path}")
        self.logger.debug(f"=> {query} -- {body}")
        return self.client.build_request(
            method, path, params=query, json=body, headers=headers
        )

    def _parse_response(self, response: Response) -> Any:
        if response.status_code == 200:
            return {"status_code": response.status_code, "content": response.json()}
        else:
            return {"status_code": response.status_code, "content": response.content}

    @abstractclassmethod
    def request(
        self,
        path: str,
        method: str,
        query: Optional[Dict[Any, Any]] = None,
        body: Optional[Dict[Any, Any]] = None,
        auth: Optional[str] = None,
    ) -> SyncAsync[Any]:
        # noqa
        pass


class Client(BaseClient):
    """Synchronous client for Asaas API."""

    client: httpx.Client

    def __init__(
        self,
        options: Optional[Union[Dict[Any, Any], ClientOptions]] = None,
        client: Optional[httpx.Client] = None,
        **kwargs: Any,
    ) -> None:
        if client is None:
            client = httpx.Client()
        super().__init__(client, options, **kwargs)

    def __enter__(self) -> "Client":
        self.client = httpx.Client()
        self.client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        self.client.__exit__(exc_type, exc_value, traceback)
        del self._clients[-1]

    def close(self) -> None:
        """Close the connection pool of the current inner client."""
        self.client.close()

    def request(
        self,
        path: str,
        method: str,
        query: Optional[Dict[Any, Any]] = None,
        body: Optional[Dict[Any, Any]] = None,
        auth: Optional[str] = None,
    ) -> Any:
        """Send an HTTP request."""
        request = self._build_request(method, path, query, body, auth)
        try:
            response = self.client.send(request)
        except httpx.TimeoutException:
            raise RequestTimeoutError()
        return self._parse_response(response)


class AsyncClient(BaseClient):
    """Asynchronous client for Notion's API."""

    client: httpx.AsyncClient

    def __init__(
        self,
        options: Optional[Union[Dict[str, Any], ClientOptions]] = None,
        client: Optional[httpx.AsyncClient] = None,
        **kwargs: Any,
    ) -> None:
        if client is None:
            client = httpx.AsyncClient()
        super().__init__(client, options, **kwargs)

    async def __aenter__(self) -> "AsyncClient":
        self.client = httpx.AsyncClient()
        await self.client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        await self.client.__aexit__(exc_type, exc_value, traceback)
        del self._clients[-1]

    async def aclose(self) -> None:
        """Close the connection pool of the current inner client."""
        await self.client.aclose()

    async def request(
        self,
        path: str,
        method: str,
        query: Optional[Dict[Any, Any]] = None,
        body: Optional[Dict[Any, Any]] = None,
        auth: Optional[str] = None,
    ) -> Any:
        """Send an HTTP request asynchronously."""
        request = self._build_request(method, path, query, body, auth)
        try:
            response = await self.client.send(request)
        except httpx.TimeoutException:
            raise RequestTimeoutError()
        return self._parse_response(response)
