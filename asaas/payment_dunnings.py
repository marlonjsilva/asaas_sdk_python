from asaas.typing import SyncAsync
from typing import Any, Optional, Dict


class PaymentDunnings:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create(self, payment_dunning: dict, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path="/paymentDunnings",
            method="POST",
            body=payment_dunning,
            auth=kwargs.get("auth"),
        )

    def payment_dunning_simulation(
        self, payment_dunning: dict, **kwargs: Any
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path="/paymentDunnings/simulate",
            method="POST",
            body=payment_dunning,
            auth=kwargs.get("auth"),
        )

    def get_by_id(self, payment_dunning_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentDunnings/{payment_dunning_id}",
            method="GET",
            auth=kwargs.get("auth"),
        )

    def history(
        self,
        payment_dunning_id: str,
        query: Optional[Dict[Any, Any]] = None,
        **kwars: Any,
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentDunnings/{payment_dunning_id}/history",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )

    def partial_payments(
        self,
        payment_dunning_id: str,
        query: Optional[Dict[Any, Any]] = None,
        **kwars: Any,
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentDunnings/{payment_dunning_id}/partialPayments",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )

    def payments_available_for_dunning(
        self,
        payment_dunning_id: str,
        query: Optional[Dict[Any, Any]] = None,
        **kwars: Any,
    ) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/paymentDunnings/{payment_dunning_id}/paymentsAvailableForDunning",
            method="GET",
            query=query,
            auth=kwars.get("auth"),
        )

    def get_by_id(self, payment_dunning_id: str, **kwargs: Any) -> SyncAsync[Any]:
        return self.parent.request(
            path=f"/payments/{payment_dunning_id}/cancel",
            method="POST",
            auth=kwargs.get("auth"),
        )
