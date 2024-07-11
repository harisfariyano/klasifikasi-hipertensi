import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN_WA')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER_WA')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(to_number, message_body):
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=f'whatsapp:{to_number}'
        )
        return {'status': 'Message sent', 'sid': message.sid}
    except TwilioRestException as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': 'An unexpected error occurred: ' + str(e)}