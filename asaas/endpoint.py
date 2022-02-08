from asaas.sdk import BaseClient


class Endpoint:
    def __init__(self, parent: BaseClient) -> None:
        self.parent = parent
