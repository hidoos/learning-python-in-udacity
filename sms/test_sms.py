from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = '<ACCOUNT_SID>'
AUTH_TOKEN = '<auth_token>'
    
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
client.messages.create(
   to = '+<user mobile number>',
   from_ = '<from number>',
   body = 'learn python in udacity'
)
