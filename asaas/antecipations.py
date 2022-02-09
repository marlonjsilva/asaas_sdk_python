from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Antecipations:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, antecipation: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/anticipations",
            method="POST",
            body=antecipation,
            auth=kwargs.get("auth"),
        )

    def antecipation_simulation(
        self, antecipation: dict, **kwargs: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/anticipations/simulate",
            method="POST",
            body=antecipation,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, antecipation_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/anticipations/{antecipation_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/anticipations", method="GET", query=query, auth=kwars.get("auth")
        )
