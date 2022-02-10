from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Invoices:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, invoice: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/invoices",
            method="POST",
            body=invoice,
            auth=kwargs.get("auth"),
        )

    def update(self, invoice: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/invoices/{invoice['id']}",
            method="POST",
            body=invoice,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, invoice_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/invoices/{invoice_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/invoices", method="GET", query=query, auth=kwars.get("auth")
        )

    def auhtorize(self, invoice_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/invoices/{invoice_id}/authorize",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def cancel(self, invoice_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/invoices/{invoice_id}/cancel",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def list_municipal_services(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/invoices/municipalServices",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )
