import json

def transform_json():
    intents = {
        "intents": [
            {
                "tag": "welcome",
                "patterns": [
                    "Oi", 
                    # "Olá", #! Não entende -- fallback
                    "E aí", "Oi, tudo bem?", "Bom dia", "Boa tarde", "Boa noite",
                    "Hello", "Hi", "Oi Tales", "Saudações", "Como vai?", "Oi, assistente", "Oi amigo", "Oi robô"
                ],
                "responses": [
                    "Olá, eu sou Tales, seu assistente virtual! Como posso ajudar hoje?",
                    "Oi! Seja bem-vindo(a). Me diga, como posso te ajudar?",
                    "Olá! Estou aqui para te ajudar com suporte. O que você precisa?"
                ],
                "context": [""]
            },
            {
                "tag": "login",
                "patterns": [
                    "Não consigo entrar na minha conta",
                    "Esqueci meu login",
                    "Erro ao acessar o sistema",
                    "Não lembro meu usuário",
                    "Não consigo logar",
                    "Minha conta não entra",
                    "Problema para acessar",
                    "Erro de autenticação",
                    # "Minha senha está certa mas não consigo entrar", #!Está caindo no reset_password
                    "Minha conta sumiu",
                    # "Tela de login não funciona", #! Bot não entendeu -- caiu no fallback
                    "Meu e-mail não entra",
                    "Não consigo acessar meu cadastro",
                    "Problema no login",
                    "O site não deixa eu logar"
                ],
                "responses": [
                    "Tente clicar em *Esqueci minha senha* na tela de login.",
                    "Verifique se o e-mail e senha estão corretos.",
                    "Caso ainda não consiga, recomendo limpar o cache do navegador ou usar outro dispositivo."
                ],
                "context": [""]
            },
            {
                "tag": "reset_password",
                "patterns": [
                    "Esqueci minha senha",
                    "Não lembro minha senha",
                    "Quero trocar a senha",
                    "Como redefinir senha?",
                    "Preciso recuperar minha senha",
                    "Senha incorreta",
                    "Quero cadastrar uma nova senha",
                    "Alterar senha",
                    "Reiniciar senha",
                    "Perdi minha senha",
                    "Me manda o link para nova senha",
                    "A senha não funciona mais",
                    "Minha senha não é aceita",
                    "Senha inválida",
                    "Trocar a senha da minha conta"
                ],
                "responses": [
                    "Você pode redefinir sua senha clicando em *Esqueci minha senha* na tela de login.",
                    "Enviamos um e-mail com instruções de recuperação, verifique sua caixa de entrada ou spam.",
                    "Se preferir, posso enviar novamente o link de redefinição."
                ],
                "context": [""]
            },
            {
                "tag": "order_status",
                "patterns": [
                    # "Quero saber como está meu pedido", #! Caindo no link de pagamento -- payment
                    "Qual o status do meu pedido?",
                    "Onde está minha compra?",
                    "Meu pedido já foi enviado?",
                    "Pedido em andamento",
                    "Rastreamento do pedido",
                    "Quando chega meu pedido?",
                    "Meu pedido foi aprovado?",
                    "Meu pedido está atrasado",
                    "Qual o prazo de entrega?",
                    "Pedido ainda não chegou",
                    "Minha entrega está demorando",
                    "Como vejo o status do pedido?",
                    "Me dá informações do meu pedido",
                    "Preciso rastrear minha compra"
                ],
                "responses": [
                    "Me informe o número do pedido para consultar o status.",
                    "Você pode acompanhar o status pelo link de rastreamento enviado no seu e-mail.",
                    "Normalmente os pedidos levam de 3 a 7 dias úteis para entrega."
                ],
                "context": [""]
            },
            {
                "tag": "payment",
                "patterns": [
                    "Quero pagar meu pedido",
                    "Quais formas de pagamento aceitam?",
                    "Aceita cartão de crédito?",
                    "Posso pagar com PIX?",
                    "Quero segunda via do boleto",
                    "Como pago minha compra?",
                    "Preciso pagar de novo",
                    "Perdi o boleto",
                    "Tem como parcelar?",
                    "Aceita débito?",
                    "Aceita transferência?",
                    "Quais são os métodos de pagamento?",
                    "Quero emitir outro boleto",
                    # "Vocês aceitam PayPal?", #!Não compreende -- fallback
                    "Posso pagar na entrega?"
                ],
                "responses": [
                    "Aceitamos cartão de crédito, débito, boleto e PIX.",
                    "Você pode acessar sua área do cliente e emitir a segunda via do boleto.",
                    "Se preferir, posso te enviar novamente o link de pagamento."
                ],
                "context": [""]
            },
            {
                "tag": "human_support",
                "patterns": [
                    "Quero falar com atendente",
                    "Preciso de um humano",
                    "Posso falar com suporte?",
                    "Quero atendimento humano",
                    "Me passa para um atendente",
                    "Preciso de uma pessoa de verdade",
                    "Quero falar com alguém",
                    "Falar com humano",
                    "Falar com suporte real",
                    "Me transfere para atendente",
                    "Preciso de ajuda com alguém real",
                    "Pode chamar um atendente?",
                    "Transferir para humano",
                    "Preciso de atendimento humano",
                    "Quero falar com suporte técnico"
                ],
                "responses": [
                    "Certo! Estou transferindo você para um atendente. Um momento, por favor.",
                    "Um atendente humano assumirá seu atendimento em instantes."
                ],
                "context": [""]
            },
            {
                "tag": "goodbye",
                "patterns": [
                    "Tchau",
                    "Até logo",
                    # "Valeu", #! Não entendeu e pulou para fallback
                    "Obrigado",
                    "brigado",
                    "Obrigada",
                    "Falou",
                    "Até mais",
                    # "Até amanhã", #! Não entendeu e pulou para fallback
                    "Fui",
                    "Nos vemos depois",
                    # "Boa noite", #! Já está em hello
                    "Até breve",
                    "Tenha um bom dia",
                    "Até a próxima",
                    "Obrigado pela ajuda",
                    # "Gratidão" #! Não entendeu e pulou para fallback
                ],
                "responses": [
                    "Foi um prazer ajudar você! Até logo 👋",
                    "Obrigada pelo contato! Estou sempre por aqui.",
                    "Tchau, tenha um ótimo dia!"
                ],
                "context": [""]
            },
            {
                "tag": "fallback",
                "patterns": [
                    "asdfgh",
                    "??",
                    "Não entendi nada",
                    "Hein?",
                    "O que você falou?",
                    "Não faz sentido",
                    "Responde direito",
                    "Hã?",
                    "???",
                    "Não entendi sua resposta",
                    "Fala melhor",
                    "Está confuso",
                    "Explica de novo",
                    "Você não respondeu",
                    # "Repete por favor" #! Não entendeu e pula pra goodbye
                ],
                "responses": [
                    "Desculpe, não entendi. Pode reformular sua pergunta?",
                    "Não consegui compreender sua solicitação. Pode tentar de outro jeito?",
                    "Pode explicar de forma diferente para que eu possa te ajudar melhor?"
                ],
                "context": [""]
            }
        ]
    }

    with open('chat_keras/intents.json', 'w') as f:
        json.dump(intents, f)

    print('Json treino criado')