"""Custom type definitions for asaas_sdk_python."""
from typing import Awaitable, TypeVar, Union

T = TypeVar("T")
SyncAsync = Union[T, Awaitable[T]]
