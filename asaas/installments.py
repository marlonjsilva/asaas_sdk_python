from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Installments:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_by_id(self, installment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/installments/{installment_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/installments", method="GET", query=query, auth=kwars.get("auth")
        )

    def delete(self, installment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/installments/{installment_id}",
            method="DELETE",
            auth=kwargs.get("auth"),
        )

    def refund(self, installment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/installments/{installment_id}/refund",
            method="POST",
            auth=kwargs.get("auth"),
        )
