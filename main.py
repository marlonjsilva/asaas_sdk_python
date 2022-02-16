from asaas.sdk import Client


client = Client(auth="23206d8dc43d19a36fe82da32a21dc0884539eb80ed442fa8df31db048422948")


print(
    client.payment_links.upload_image(
        payment_link_id="727571566345", image="/home/msilva/Downloads/210888.jpg"
    )
)
