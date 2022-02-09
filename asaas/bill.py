from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Bill:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, bill: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/bill",
            method="POST",
            body=bill,
            auth=kwargs.get("auth"),
        )

    def payment_bill_simulation(self, bill: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/bill/simulate",
            method="POST",
            body=bill,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, bill_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/bill/{bill_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/bill", method="GET", query=query, auth=kwars.get("auth")
        )

    def cancel(self, bill_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/bill/{bill_id}/cancel",
            method="POST",
            auth=kwargs.get("auth"),
        )
