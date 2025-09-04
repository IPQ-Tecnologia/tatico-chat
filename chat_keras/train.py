import json
import pickle
import nltk
import random
import numpy as np
import unicodedata
from transform_json import transform_json

from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Input, Dropout
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping

nltk.download('punkt')
# nltk.download("punkt_tab")
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

transform_json()

def remove_accent(text):
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


# inicializaremos nossa lista de palavras, classes, documentos e 
# definimos quais palavras serão ignoradas
words = []
documents = []
intents = json.loads(open('chat_keras/intents.json').read())
# adicionamos as tags em nossa lista de classes
classes = [i['tag'] for i in intents['intents']]
ignore_words = ["!", "@", "#", "$", "%", "*", "?"]

# é feita a leitura do arquivo intents.json e transformado em json
# intents = json.loads(open('intents.json').read())


# percorremos nosso array de objetos
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # com ajuda no nltk fazemos aqui a tokenizaçao dos patterns 
        # e adicionamos na lista de palavras
        # print(pattern)
        word = remove_accent(pattern)
        print(word)
        print("WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORD")
        word_tok = nltk.word_tokenize(word)
        print(word_tok)
        print('WORD TOKKKKKKKKKKKKKKKKKKKK')
        words.extend(word_tok)
        # adiciona aos documentos para identificarmos a tag para a mesma
        print(words)
        print("WORDSSSSSSSSSSSSSSSS")
        documents.append((word_tok, intent['tag']))
        print(documents)
        print("DOCUMENTSSSSSSSSSSS")

# print(documents)
# print("DOCUMMMMMMEEEEENT" *5)
# lematizamos as palavras ignorando os palavras da lista ignore_words
words = sorted(list(set([lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words])))
classes = sorted(list(set(classes)))

# salvamos as palavras e classes nos arquivos pkl
pickle.dump(words, open('chat_keras/words.pkl', 'wb'))
pickle.dump(classes, open('chat_keras/classes.pkl', 'wb'))


# inicializamos o treinamento
training = []
output_empty = [0] * len(classes)
for document in documents:
    # inicializamos o saco de palavras 
    bag = []

    # lematizamos cada palavra 
    # na tentativa de representar palavras relacionadas
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in document[0]]

    # criamos nosso conjunto de palavras com 1, 
    # se a correspondência de palavras for encontrada no padrão     atual
    for w in words:
        bag.append(1 if w in pattern_words else 0)

    # output_row atuará como uma chave para a lista, 
    # onde a saida será 0 para cada tag e 1 para a tag atual
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1

    training.append([bag, output_row])

# embaralhamos nosso conjunto de treinamentos e transformamos em numpy array
random.shuffle(training)
training = np.array(training, dtype=object)

# criamos lista de treino sendo x os patterns e y as intenções
x = np.array(list(training[:, 0]))
y = np.array(list(training[:, 1]))

# Criamos nosso modelo com 3 camadas. 
# Primeira camada de 128 neurônios, 
# segunda camada de 64 neurônios e terceira camada de saída 
# contém número de neurônios igual ao número de interesse para prever a intenção de saída com softmax
model = Sequential() 
model.add(Input(shape=(len(x[0]),)))
model.add(Dense(128, activation='relu')) 
model.add(Dropout(0.3)) 
model.add(Dense(64, activation='relu')) 
model.add(Dropout(0.3)) 
model.add(Dense(len(y[0]), activation='softmax')) 

# O modelo é compilado com descida de gradiente estocástica 
# com gradiente acelerado de Nesterov. 
# A ideia da otimização do Momentum de Nesterov, ou Nesterov Accelerated Gradient (NAG), 
# é medir o gradiente da função de custo não na posição local, 
# mas recomendado à frente na direção do momentum. 
# A única diferença entre a otimização de Momentum é que o gradiente é medido em θ + βm em vez de em θ.
# sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True) 

model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(learning_rate=0.001), 
    metrics=['accuracy'])


# # ajustamos e salvamos o modelo 
# m = model.fit(np.array(x), np.array(y), epochs=200, batch_size=5, verbose=1)

# Divide dados em treino (80%) e validação (20%)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

# Early stopping: para quando não há melhora em 10 épocas
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

# Treinamento
history = model.fit(
    x_train, y_train,
    epochs=200,
    batch_size=5,
    validation_data=(x_val, y_val),
    callbacks=[early_stop],
    verbose=1
)

model.save('chat_keras/model.keras')
with open("chat_keras/training_history.pkl", "wb") as f:
    pickle.dump(history.history, f)

print("Treinamento concluido")