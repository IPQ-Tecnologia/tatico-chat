import spacy 
#import pandas as pd
import unicodedata

nlp = spacy.load('pt_core_news_md')

ignore_words = ["!", "@", "#", "$", "%", "*", "?", ",", ".", ";"]


def remove_accent(text):
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


def tokenizer(word):
    doc = nlp(word)
    filtered_tokens = [token for token in doc if not token.is_stop and not token.is_punct]
    #print(filtered_tokens)
    #print('*-'*30)
    lemmas = [token.lemma_ for token in filtered_tokens]
    lemmas_accent = [remove_accent(lemma) for lemma in lemmas]
    #word = remove_accent(lemmas)
    # print(lemmas_accent)
    # print("*--"*10)
    
    return lemmas_accent

#tokenizer("Estou realizando um novo teste")
#tokenizer("como criar ocorrência com status de fechada?")
#tokenizer("Como criar ocorrência?")
#tokenizer("como criar relatório de registro de conexões?")
#tokenizer("como criar uma ocorrência a partir da localização de uma viatura?")
#tokenizer("como criar relatório de atendimentos por usuários?")
#tokenizer("Saudação")

greetings = [
    "Oi", "Oi Tales", "Olá", "E aí", "Oi, tudo bem?", 
    "Bom dia", "Boa tarde", "Boa noite", "Saudações", "Como vai?", 
    "Oi, assistente", "Oi amigo", "Eae", "Fala aí", "Tudo certo?"
]


def replace_greeting(greeting):
    if greeting in greetings:
        return 'saudacao'
