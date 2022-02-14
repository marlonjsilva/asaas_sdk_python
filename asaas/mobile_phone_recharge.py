from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class MobilePhoneRecharge:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, mobile: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/mobilePhoneRecharges",
            method="POST",
            body=mobile,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, mobile_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/mobilePhoneRecharges/{mobile_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def list(
        self, query: Optional[Dict[Any, Any]] = None, **kwars: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/mobilePhoneRecharges",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )

    def cancel(self, mobile_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymobilePhoneRecharges/{mobile_id}/cancel",
            method="POST",
            auth=kwargs.get("auth"),
        )

    def provider(self, phone_number: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymobilePhoneRecharges/{phone_number}/provider",
            method="POST",
            auth=kwargs.get("auth"),
        )
