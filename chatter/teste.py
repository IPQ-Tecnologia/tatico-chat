# # Teste (validação)
# testes = {
#     "Oi": "Olá, tudo bem?",
#     "Qual seu nome?": "Meu nome é Thales.",
#     "Tchau": "Até logo!",
#     "Bom dia": "Olá, tudo bem?"  # aqui espero que ele associe
# }

# # Avaliação
# acertos = 0
# for pergunta, resposta_esperada in testes.items():
#     resposta_bot = str(chatbot.get_response(pergunta))
#     print(f"Pergunta: {pergunta}")
#     print(f"Esperado: {resposta_esperada}")
#     print(f"Bot: {resposta_bot}")
#     print("-"*30)
    
#     if resposta_bot == resposta_esperada:
#         acertos += 1

# acuracia = acertos / len(testes)
# print(f"Acurácia: {acuracia*100:.2f}%")
