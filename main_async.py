import asyncio
from asaas.sdk import AsyncClient


async def main():
    client = AsyncClient(
        auth="23206d8dc43d19a36fe82da32a21dc0884539eb80ed442fa8df31db048422948"
    )
    create_customer = {
        "name": "Hermanoteu Aguiar",
        "cpfCnpj": "98008274042",
        "email": "hermanoteuaguiar@gmail.com",
        "phone": "7336125397",
        "mobilePhone": "73988665421",
        "address": "Rua Hérminio da Mota",
        "addressNumber": "3434",
        "complement": "Nenhum",
        "province": "Centro",
        "postalCode": "45600-100",
    }
    response = await client.customer.list()
    print(response)


asyncio.run(main())
