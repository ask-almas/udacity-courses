from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfcf5f4cac101e707e7dfb841b9b8d093"
# Your Auth Token from twilio.com/console
auth_token  = "f7fbf28ec9e8f52abc5d805beb2ebc59"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+77775664274", 
    from_="+17479980090",
    body="Hello from Python!")

print(message.sid)
