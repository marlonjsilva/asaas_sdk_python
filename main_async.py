import asyncio
from asaas.sdk import AsyncClient


async def main():
    client = AsyncClient(auth="XXX")
    response = await client.customer.list()
    print(response)


asyncio.run(main())
