import os
from dotenv import load_dotenv
import requests

PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


# def criticality_scheduling(criticality):
#     if criticality == 'baixa':





def send_to_support(customer_phone, last_message):
    support_phone_number = "5571952236525"
    whatsapp_token = os.getenv("WHATSAPP_TOKEN")

    url = f'https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages'
    headers = {
        "Authorization": f"Bearer {whatsapp_token}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": support_phone_number,
        "type": "text",
        "text": {
            "body": f"Novo pedido de atendimento humano"
                    f"Cliente: {customer_phone}"
                    f"Última mensagem: {last_message}"
                    f"Responda diretamente pelo WhatsApp Bussines para assumir a conversa"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print("Notificação de suporte enviada: ", response.json())

