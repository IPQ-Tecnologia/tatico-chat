from chatter.token_word import tokenizer


def pre_process(sentence):
    tokens = tokenizer(sentence)
    return " ".join(tokens)