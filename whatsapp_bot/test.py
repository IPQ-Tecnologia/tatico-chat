import redis.asyncio as redis_async
import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath("../.env")
load_dotenv(dotenv_path=dotenv_path)

redis_host = os.getenv("redis_host")
redis_password = os.getenv("redis_password")
redis_port = os.getenv("redis_port")

phone_number = os.getenv("phone_number")
token = os.getenv("token")

#! FAZER UPLOAD DA IMAGEM:

# curl -X POST "https://graph.facebook.com/v22.0/733052589898926/media" \
#   -H "Authorization: Bearer EAASnWbWU1IcBPRiy0ZCXUJvD0fpH1S013vlZAPshDm6r5GHOu0xCEqiOIS8ZCzLqtPPfzaGMpJzJehPxO3sIcpxECiKD0II5dh25jSB8NuUySLGnynx7BpojzdjvJlEgrqzoH1ZBKmRmP9TooLl1NwDUYfqxtZBojS8ZCYZBJdpSJbf60dPVeWY1BmQnyezsOVjiZAMvTaq1ZCvNJXUlvBISZBS18oyEIujoLvBMGBdQKjAoZBUmQZDZD" \
#   -F "file=@/home/julia/Imagens/Capturas de tela/testando.png" \
#   -F "type=image1/jpeg"



def send_image_drive(file_path, media_type, token, phone_number_id):
    url = f'https://graph.facebook.com/v22.0/{phone_number_id}/media'
    headers = {
        "Authorization": f'Bearer {token}'
    }
    files = {
        'file': (file_path, open(file_path, "rb"), media_type),
        'type': (None, media_type),
        'messaging_product': (None, "whatsapp")
    }

    response = requests.post(url, headers=headers, files=files)

    print(response.json())

    redis_set("relatorio_teste", response.json())

    # print(response[0])

    return response.json


send_image_drive("/home/julia/Imagens/Capturas de tela/testando.png", "image/jpeg",token, phone_number)


def get_redis_client():
    """ Iniciar client redis """
    try:
        r = redis_async.from_url(
            f"redis://{redis_host}:{redis_port}",
            password=redis_password,
            decode_response=True
        )
        return r
    except Exception as err:
        print("Erro ao se conectar ao redis: %s", err)

def redis_set(key:str, value:str):
    """ Enviar ao redis """
    try:
        r = get_redis_client()
        r.set(key, value)
    except Exception as err:
        print("Erro: %s", err)

def redis_get(key:str):
    """ Puxa do redis """
    try:
        r = get_redis_client()
        value = r.get(key)
        return value
    except Exception as err:
        print("Erro: %s", err)


#! FAZER UPLOAD DE VIDEO:

# curl -X POST "https://graph.facebook.com/v22.0/733052589898926/media" \
#   -H "Authorization: Bearer EAASnWbWU1IcBPeZBthl0nTg4OfGFsrmLhsiVu8V0qeIiZCaPyY1AncjmdH6KCO1igl7P6dvNrtCeKhOsysSRUq9TzswbzAeyLuZBEoZBUG3iDlfCa5U1ah4QPISxLfmHbRFbak4SqKA3TCSCqP6KSk6Uej7Nxrx9yasVh4a06As3DErZC1ZCOZB8afTkQMThaVIRkoiNJjKR8Vzvabi9MovGRZAZAZBzIDWWHduiTxX8pcmZC0y9gZDZD" \
#   -F "file=@/home/julia/Downloads/criar_ocorrencia.mp4" \
#   -F "type=video/mp4" \
#   -F "messaging_product=whatsapp"
