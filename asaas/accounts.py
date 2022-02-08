from pydoc import cli
from asaas.typing import SyncAsync
from typing import Any, Optional, Dict
import json


class Accounts:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, account=dict, **kwargs) -> SyncAsync[Any]:
        return self.parent.request(
            path="/accounts",
            method="POST",
            body=account,
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/accounts", method="GET", query=query, auth=kwars.get("auth")
        )
