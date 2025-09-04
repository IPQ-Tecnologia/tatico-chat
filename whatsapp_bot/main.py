import os
from dotenv import load_dotenv
import requests
from whatsapp_bot.test import redis_get
# from chatter.conversation import process_speech

dotenv_path = os.path.abspath("../.env")
load_dotenv(dotenv_path=dotenv_path)


PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
# VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
WHATSAPP_TOKEN = 'EAASnWbWU1IcBPTP8PI9kfwe0x6sZCabuMC2i3nROz7ZA4idXZB9ZAUQOAmCvyb1DoGa7c6YUjVrjThKQZCZB1pcZAn1uoMxoYohcxsbFR4cNRGsUKQEZB9NzUZCHr1AJ8N8ZAT0SZAuNcdU6bpoP7hEXB4LFewMHxCyJPggD7PGZCBrtxWcNA2Oq6aQveAJHLyUyEGHpw8pOi6YpR2ZB0ZBCXm17O5BZBL8cOXTeAAEOWPosoHfByWXIwZDZD'

def send_message(to, message_response):
    url = f'https://graph.facebook.com/v22.0/733052589898926/messages'
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message_response}
    }

    response = requests.post(url, headers=headers, json=data)
    print("Resposta do envio: ", response.json())

# def send_image(to, key):
#         redis_get(key)
#         image = {
#         "messaging_product": "whatsapp",
#         "to": to,
#         "type": "image",
#         "image": {
#             "id":"644254858296609"
#         }
#     }

#     print("DATA * "*10)
#     print(url)
#     print(headers)
#     print(data)
#     print(image)