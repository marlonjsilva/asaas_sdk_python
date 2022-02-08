from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Subscriptions:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, subscription: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/subscriptions",
            method="POST",
            body=subscription,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, subscription_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/subscriptions", method="GET", query=query, auth=kwars.get("auth")
        )

    def list_payments(self, subscription_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription_id}/payments",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def update(self, subscription: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription['id']}",
            method="POST",
            body=subscription,
            auth=kwargs.get("auth"),
        )

    def delete(self, subscription_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription_id}",
            method="DELETE",
            auth=kwargs.get("auth"),
        )

    def list_invoices(
        self,
        subscription_id: str,
        query: Optional[Dict[Any, Any]] = None,
        **kwargs: Any,
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription_id}/invoices",
            method="GET",
            query=query,
            auth=kwargs.get("auth"),
        )

    def invoice_settings(self, subscription: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription['id']}/invoiceSettings",
            method="POST",
            body=subscription,
            auth=kwargs.get("auth"),
        )

    def update_invoice_settings(
        self, subscription: str, **kwargs: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription['id']}/invoiceSettings",
            method="POST",
            body=subscription,
            auth=kwargs.get("auth"),
        )

    def get_invoice_settings(
        self, subscription_id: str, **kwargs: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription_id}/invoiceSettings",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def delete_invoice_settings(
        self, subscription_id: str, **kwargs: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/subscriptions/{subscription_id}/invoiceSettings",
            method="DELETE",
            auth=kwargs.get("auth"),
        )
