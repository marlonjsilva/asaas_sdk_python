from pydoc import cli
from urllib import response
import pytest
import httpx
from pytest_httpx import HTTPXMock
from asaas.sdk import AsyncClient, Client
import os


@pytest.fixture
def prepare_async_client():
    client = AsyncClient(auth=os.environ["ASAAS_KEY"])
    return client


@pytest.fixture
def prepare_client():
    client = Client(auth=os.environ["ASAAS_KEY"])
    return client


@pytest.fixture
def response_create_new_customer():
    return {
        "status_code": 200,
        "content": {
            "object": "customer",
            "id": "cus_000004802607",
            "dateCreated": "2022-02-10",
            "name": "Aldemir Alves",
            "email": "aldemiralves@gmail.com",
            "company": None,
            "phone": "7336125485",
            "mobilePhone": "73988652842",
            "address": "Rua Hérminio da Mota",
            "addressNumber": "3535",
            "complement": "Depois da avenida",
            "province": "Centro",
            "postalCode": "45600100",
            "cpfCnpj": "32040512004",
            "personType": "FISICA",
            "deleted": False,
            "additionalEmails": None,
            "externalReference": "3445434",
            "notificationDisabled": False,
            "observations": None,
            "city": 9365,
            "state": "BA",
            "country": "Brasil",
            "foreignCustomer": False,
        },
    }


def test_inicialization(prepare_client):
    assert isinstance(prepare_client, Client)


def test_async_inicialization(prepare_async_client):
    assert isinstance(prepare_async_client, AsyncClient)


def test_sync_create_new_customer(
    prepare_client: Client, httpx_mock: HTTPXMock, response_create_new_customer
):
    httpx_mock.add_response(
        method="POST",
        json={
            "object": "customer",
            "id": "cus_000004802607",
            "dateCreated": "2022-02-10",
            "name": "Aldemir Alves",
            "email": "aldemiralves@gmail.com",
            "company": None,
            "phone": "7336125485",
            "mobilePhone": "73988652842",
            "address": "Rua Hérminio da Mota",
            "addressNumber": "3535",
            "complement": "Depois da avenida",
            "province": "Centro",
            "postalCode": "45600100",
            "cpfCnpj": "32040512004",
            "personType": "FISICA",
            "deleted": False,
            "additionalEmails": None,
            "externalReference": "3445434",
            "notificationDisabled": False,
            "observations": None,
            "city": 9365,
            "state": "BA",
            "country": "Brasil",
            "foreignCustomer": False,
        },
    )
    with prepare_client as client:
        response = client.customers.create({"id": "test"})
    assert response == response_create_new_customer


@pytest.mark.asyncio
async def test_async_create_new_customer(
    prepare_async_client: AsyncClient,
    httpx_mock: HTTPXMock,
    response_create_new_customer,
):
    httpx_mock.add_response(
        method="POST",
        json={
            "object": "customer",
            "id": "cus_000004802607",
            "dateCreated": "2022-02-10",
            "name": "Aldemir Alves",
            "email": "aldemiralves@gmail.com",
            "company": None,
            "phone": "7336125485",
            "mobilePhone": "73988652842",
            "address": "Rua Hérminio da Mota",
            "addressNumber": "3535",
            "complement": "Depois da avenida",
            "province": "Centro",
            "postalCode": "45600100",
            "cpfCnpj": "32040512004",
            "personType": "FISICA",
            "deleted": False,
            "additionalEmails": None,
            "externalReference": "3445434",
            "notificationDisabled": False,
            "observations": None,
            "city": 9365,
            "state": "BA",
            "country": "Brasil",
            "foreignCustomer": False,
        },
    )

    async with prepare_async_client as client:
        response = await client.customers.create({"id": "test"})
    assert response == response_create_new_customer
