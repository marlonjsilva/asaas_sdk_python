from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Transfers:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, transfer: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/transfers",
            method="POST",
            body=transfer,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, transfer_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/transfers/{transfer_id}", method="GET", auth=kwargs.get("auth")
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/transfers", method="GET", query=query, auth=kwars.get("auth")
        )
