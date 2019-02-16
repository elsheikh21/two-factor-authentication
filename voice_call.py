from twilio.rest import Client

account_sid = "AC5e6226d3ec01c1b13f9ab8a52e641beb"
auth_token = "485fccb21d77f3f7e1eb7b2fcc7ce7c5"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+201117091566",
    from_="+18285481610",
    url="https://demo.twilio.com/welcome/sms/reply/"
)

print("CALL SID: " + call.sid)