import redis.asyncio as redis_async
# from chatterbot import ChatBot
from chatter.helpers import pre_process
from chatter.config_chatbot import chat_config
from whatsapp_bot.human_scaling import send_to_support
import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath("../.env")
load_dotenv(dotenv_path=dotenv_path)

redis_host = os.getenv("redis_host")
redis_password = os.getenv("redis_password")
redis_port = os.getenv("redis_port")


# r = redis_async.from_url(
#     f"redis://{redis_host}:{redis_port}, decode_response=True)

greetings = [
    "oi", "oi tales", "ola", "e ai", "eai", "eae", "oi, tudo bem", 
    "bom dia", "boa tarde", "boa noite", "saudacoes", "como vai", 
    "oi, assistente", "oi amigo", "fala ai", "tudo certo"
]

exit_conditions = ("quit", 'exit', 'sair', 'tchau', 'obrigada')

service = ("atendente", "humano")

def process_speech(number, speak):

    chatbot = chat_config()
    question = speak.lower().strip()

    if not question:
        return("Tales: Você precisa digitar uma mensagem válida")
        # continue

    question = pre_process(question)

    if question in greetings:
        question = 'saudacao'
        # print(question)
        # print('*-'*15)

    if question in exit_conditions:
        return ("Espero ter ajudado! Até a próxima")
    
    if question in service:
        send_to_support(number, speak)
        return("Transferindo seu atendimento para um de nossos atendentes de suporte")

    try:
        # question_preprocess = pre_process(question)
        response = chatbot.get_response(question)
        confidence = getattr(response, "confidence", 1.0)
        print(f"CONFIANÇA: {confidence}")

        if confidence < 0.3:
            cont_key = f'low_confidence:{number}'
            cont = int(r.get(cont_key) or 0) + 1
            r.set(cont_key, cont)

            if cont > 3:
                r.delete(cont_key)
                send_to_support(number, speak)
                return "Parece que infelizmente não consegui te ajudar. Estou transferindo o atendimento para o nosso suporte"
        
            return "Huum, não entendi o que quis dizer. Poderia repetir"
        return (f"Thales: {response}")
    except Exception as e:
        print("Erro: %s", e)
        return "Thales: Você precisa digitar uma mensagem válida."
    # if float(response.confidence) < 0.4:
    #     print("Não entendi... o que eu deveria responder?")
    #     correct_answer = input("Resposta correta: ")

    #     if correct_answer.strip() != "":
    #         chatbot.learn_response(correct_answer, question)
    #         print("Aprendi essa nova resposta!")