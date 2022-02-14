from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class CustomerFiscalInfo:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def municipal_options(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/customerFiscalInfo/municipalOptions",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )

    def customer_fiscal_info(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/customerFiscalInfo",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )
