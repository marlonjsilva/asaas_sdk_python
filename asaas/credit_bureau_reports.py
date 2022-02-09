from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class CreditBureauReports:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, credit_bureau_report: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/creditBureauReport",
            method="POST",
            body=credit_bureau_report,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, credit_bureau_report_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/creditBureauReport/{credit_bureau_report_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/creditBureauReport",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )
