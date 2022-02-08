from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Customer:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, customer: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/customers",
            method="POST",
            body=customer,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, customer_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/customers/{customer_id}", method="GET", auth=kwargs.get("auth")
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/customers", method="GET", query=query, auth=kwars.get("auth")
        )

    def delete(self, customer_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/customers/{customer_id}",
            method="DELETE",
            auth=kwargs.get("auth"),
        )

    def restore(self, customer_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/customers/{customer_id}/restore",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def update(self, parent: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/customers/{parent['id']}",
            method="POST",
            body=parent,
            auth=kwargs.get("auth"),
        )
