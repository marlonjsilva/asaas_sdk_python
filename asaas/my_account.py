from asaas.typing import SyncAsync
from typing import Any


class MyAccount:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_comercial_data(self, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/myAccount",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def get_checkout_data(self, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/myAccount/paymentCheckoutConfig",
            method="GET",
            auth=kwargs.get("auth"),
        )
