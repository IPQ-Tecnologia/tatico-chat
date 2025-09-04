from chatterbot import ChatBot
from chatterbot import languages
languages.POR.ISO_639_1 = 'pt_core_web_sm'
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatter.config_chatbot import chat_config
from chatter.helpers import pre_process


chatbot = chat_config()

# chatbot = ChatBot(
#                     "Tales",
#                     storage_adapter="chatterbot.storage.SQLStorageAdapter",
#                     database_URI="sqlite:///database.sqlite3",
#                     read_only=False)


# chatbot = ChatBot(
#     "Tales",
#     storage_adapter="chatterbot.storage.SQLStorageAdapter",
#     database_uri="sqlite:///database.sqlite3",
#     logic_adapter=[
#         {
#             "import_path":"chatterbot.logic.BestMatch",
#             "default_response":"Desculpe, não consegui entender. Você pode reformular a pergunta?",
#             "maximum_similarity_threshold":0.80
#         }
#     ],
#     read_only=True
#     )

# exit_conditions = ("quit", 'exit', 'sair', 'tchau', 'obrigada')

# service = ("atendente", "humano")

# greetings = [
#     "oi", "oi tales", "ola", "e ai", "eai", "eae", "oi, tudo bem", 
#     "bom dia", "boa tarde", "boa noite", "saudacoes", "como vai", 
#     "oi, assistente", "oi amigo", "fala ai", "tudo certo"
# ]

# def pre_process(sentence):
#     tokens = tokenizer(sentence)
#     return " ".join(tokens)

conversations = {
            pre_process("saudacao"):"Olá, eu sou Tales, seu assistente virtual! Como posso ajudar?",
            pre_process("Como criar ocorrencia?"):"Clique no primeiro ícone do painel > 'Atendimento' > Na barra inferior clique o ícone + (soma) > Insira os dados > Clique no ícone de salvar — Último ícone da barra inferior. Pronto, ocorrência criada",
            pre_process("como criar ocorrencia com status de fechada?"): "Clique no primeiro ícone do painel > 'Atendimento' > Na barra inferior clique o ícone + (soma) > Insira os dados — é essencial preencher a localização, cidade, tipo e subtipo (se necessário) para concluir a criação > Selecione o grupo de despacho > Clique no ícone de salvar — Último ícone da barra inferior > Clique 'gerar ocorrência fechada' — penúltimo ícone da barra inferior > Adicione o comentário de fechamento e clique em 'Enviar'",
            pre_process("como criar uma ocorrencia a partir da localização de uma viatura?"):"Clique no segundo ícone 'Despacho' > Selecione a viatura desejada > 'Criar Ocorrência' > Selecione 'Tipo', 'Subtipo' e escreva o comentário > 'Enviar'",
            pre_process("como criar relatorio de registro de conexoes?"):"Clique no ícone 'Relatórios' > 'Dispositivos' > 'Registro de conexões' > Selecione as opções de filtro desejadas > Caso queira um filtro detalhado marque a opção 'Relatório detalhado' > Clique em 'Gerar relatório' para visualizar ou 'Exportar CSV' para salvar o relatório.",
            pre_process("como criar relatorio de atendimentos por usuarios?"):"Clique no ícone 'Relatórios' > 'Atendimento' > 'Total de atendimentos por usuários' > selecione os filtros desejados > Clique em 'Gerar relatório' para visualizar ou 'Exportar CSV' para salvar o relatório."
}

# print(talk)

#corpus_trainer = ChatterBotCorpusTrainer(chatbot)
#corpus_trainer.train("chatterbot.corpus.portuguese")


trainer = ListTrainer(chatbot)
print("iniciando treinamento")
# for dialog in conversations:
#     trainer.train(dialog)
for quest, answer in conversations.items():
    trainer.train([quest, answer])

print("Treinamento concluído com sucesso!")

# while True:
#     question = input("> ").lower().strip()
#     if not question:
#         print("Tales: Você precisa digitar uma mensagem válida")
#         continue

#     question = pre_process(question)

#     # print("question")
#     # print(question)
#     # print('****'*10)

#     if question in greetings:
#         question = 'saudacao'
#         # print(question)
#         # print('*-'*15)

#     if question in service:
#         #! VER O QUE VAI SER COLOCADO AQUI
#         print("Transferindo seu atendimento para um de nossos atendentes de suporte")
#         break

#     if question in exit_conditions:
#         print("Espero ter ajudado! Até a próxima")
#         break
#     try:
#         # question_preprocess = pre_process(question)
#         response = chatbot.get_response(question)
#         print(f"CONFIANÇA: {response.confidence}")
#         print(f"Thales: {response}")
#     except Exception as e:
#         print("Thales: Você precisa digitar uma mensagem válida.")
#         print("Erro: %s", e)
#     # if float(response.confidence) < 0.4:
#     #     print("Não entendi... o que eu deveria responder?")
#     #     correct_answer = input("Resposta correta: ")

#     #     if correct_answer.strip() != "":
#     #         chatbot.learn_response(correct_answer, question)
#     #         print("Aprendi essa nova resposta!")