from twilio.rest import Client

account_sid = 'ACef6adfe3a7e3335cf1ce75b9179765a3'
auth_token = '2447599e85020be6b90a64222bf25e16'

client = Client(account_sid, auth_token)

call = client.calls.create(twiml='<Response><Say>Hi there. Just testing something.</Say></Response>',from_='+12029331685',to='+917892394912')
print(call.sid)