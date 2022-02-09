from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class FinancialTransactions:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/financialTransactions",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )
