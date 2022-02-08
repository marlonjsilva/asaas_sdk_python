from asaas.sdk import Client


client = Client(auth="23206d8dc43d19a36fe82da32a21dc0884539eb80ed442fa8df31db048422948")

print(client.customer.list(query={"limit": 5}))
