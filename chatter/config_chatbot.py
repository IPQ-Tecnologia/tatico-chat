from chatterbot import ChatBot


def chat_config():
    chatbot = ChatBot(
    "Tales",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapter=[
        {
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"Desculpe, não consegui entender. Você pode reformular a pergunta?",
            "maximum_similarity_threshold":0.80
        }
    ],
    read_only=True
    )

    return chatbot