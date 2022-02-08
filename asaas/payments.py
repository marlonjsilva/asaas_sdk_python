from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class Payments:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, payment: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/payments",
            method="POST",
            body=payment,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}", method="GET", auth=kwargs.get("auth")
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/payments", method="GET", query=query, auth=kwars.get("auth")
        )

    def update(self, payment: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment['id']}",
            method="POST",
            body=payment,
            auth=kwargs.get("auth"),
        )

    def delete(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}",
            method="DELETE",
            auth=kwargs.get("auth"),
        )

    def restore(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}/restore",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def refund(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}/refund",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def get_boleto_code_bar(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}/identificationField",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def get_pix_qr_code(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}/pixQrCode",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def receive_in_cash(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}/receiveInCash",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def undo_receive_in_cash(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_id}/undoReceivedInCash",
            method="POST",
            auth=kwargs.get("auth"),
        )
