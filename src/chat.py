import random
import json
# nltk.download('punkt')
from nltk.text import TokenSearcher
from nltk.util import tokenwrap
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('../data/intents.json', 'r') as f:
    intents = json.load(f)

FILE = "../data/data.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']
all_words = data['all_words']


model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def reply(message):
    while True:
        if message == 'stop':
            break

        message = tokenize(message)
        X = bag_of_words(message, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim = 1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    return random.choice(intent['responses'])
        else:
            return 'Não entendi. Você pode contatar o grupo PET...'