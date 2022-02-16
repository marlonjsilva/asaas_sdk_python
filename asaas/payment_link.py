from base64 import encode
from io import BufferedReader
from optparse import Option
from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class PaymentLinks:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, payment_link: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/paymentLinks",
            method="POST",
            body=payment_link,
            auth=kwargs.get("auth"),
        )

    def update(self, payment_link: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentLinks/{payment_link['id']}",
            method="POST",
            body=payment_link,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, payment_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentLinks/{payment_id}", method="GET", auth=kwargs.get("auth")
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/paymentLinks", method="GET", query=query, auth=kwars.get("auth")
        )

    def delete(self, payment_link: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentLinks/{payment_link}",
            method="DELETE",
            auth=kwargs.get("auth"),
        )

    def restore(self, payment_link: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_link}/restore",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def upload_image(
        self, payment_link_id: str, image: str = None, **kwargs: Any
    ) -> SyncAsync[Any]:
        data = {"main": "true"}
        file = {"image": open(image, "rb")}
        return self.parent.request(
            path=f"/paymentLinks/{payment_link_id}/images",
            method="POST",
            body=data,
            files=file,
            encode="multipart",
            auth=kwargs.get("auth"),
        )
