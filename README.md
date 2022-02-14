# Asaas SDK Python

Sync and Async Asaas SDK written in Python

**Sync Example:**
```python
from asaas.sdk import Client

client = Client(auth="XXXX")

print(client.customer.list())
```

**Async Example:**

```python
import asyncio
from asaas.sdk import AsyncClient


async def main():
    client = AsyncClient(auth="XXX")
    response = await client.customer.list()
    print(response)


asyncio.run(main())
```
