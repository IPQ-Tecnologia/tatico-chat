from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from whatsapp_bot.main import send_message
from chatter.conversation import process_speech

dotenv_path = os.path.abspath("../.env")

load_dotenv(dotenv_path=dotenv_path)

app = FastAPI()

# VERIFY_TOKEN=os.getenv("TOKEN_WA")
VERIFY_TOKEN="senha_verify"

@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        return int(challenge)
    else:
        return {"error": "Token inválido"}

@app.post("/webhook")
async def webhook_handler(request: Request):
    data = await request.json()
    print("Mensagem recebida: ", data)

    try:
        entry = data['entry'][0]
        changes = entry['changes'][0]['value']

        if "messages" in changes:
            message = changes['messages'][0]
            number = message['from']
            received = message['text']['body']

            print(f'Cliente {number} disse: {received}')

            response = process_speech(number, received)

            send_message(number, response)
    
    except Exception as e:
        print("Erro ao processar: %s", e)

    finally:
        return {"status": "received"}
