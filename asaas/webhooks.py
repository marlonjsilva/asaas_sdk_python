from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Webhooks:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, webhook: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/webhook",
            method="POST",
            body=webhook,
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/webhook", method="GET", query=query, auth=kwars.get("auth")
        )

    def create_invoice(self, webhook: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/webhook/invoice",
            method="POST",
            body=webhook,
            auth=kwargs.get("auth"),
        )

    def list_invoice(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/webhook/invoice", method="GET", query=query, auth=kwars.get("auth")
        )

    def create_transfer(self, webhook: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/webhook/transfer",
            method="POST",
            body=webhook,
            auth=kwargs.get("auth"),
        )

    def list_transfer(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/webhook/transfer", method="GET", query=query, auth=kwars.get("auth")
        )
    