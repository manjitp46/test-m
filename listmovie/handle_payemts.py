from instamojo_wrapper import Instamojo
api = Instamojo(api_key="b565f0ac306fc912432fd955b3c87773",
                auth_token="0d19a92ae3ef9b67a9104c1bce037de2")

# Create a new Payment Request
response = api.payment_request_create(
    amount='3499',
    purpose='FIFA 16',
    send_email=True,
    email="foo@example.com",
    redirect_url="http://www.example.com/handle_redirect.py"
    )
# print the long URL of the payment request.
print(response['payment_request']['longurl'])
# print the unique ID(or payment request ID)
print(response['payment_request']['id'])