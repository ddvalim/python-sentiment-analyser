import json

from torch import nn
from transformers import BertModel

with open('config.json') as json_file:
    config = json.load(json_file)

class Classifier(nn.Module):
    def __init__(self, n_classes):
        super(Classifier, self).__init__()

        self.bert = BertModel.from_pretrained(config["BERT_MODEL"], return_dict=False)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self, ids, attention_mask):
        # O processo de tokenização transforma um texto em unidades menores chamadas tokens
        # Que facilitam o processamento da informação

        # ids = tokens da sequência de entrada
        # attention_mask = conjunto de tokens cujo modelo deve levar em consideração ao processar o dado  

        # Extração do vetor do token CLS, que se refere ao estado do token CLS. Representa o agregado de informações
        # acerca de uma sequência textual
        # O vetor do token CLS pode ser interpretado como um agregado de informações úteis ao processamento do dado
        _, pooled_output = self.bert(ids, attention_mask)

        # Camada responsável por desligar aleatoriamente e na proporção pré-determinada um conjunto de neurônios
        # Para regularizar o modelo e evitar o overfitting durante a fase de treinamento do modelo. 
        # Durante a fase de avaliação e inferência sobre os tokens de entrada, o dropout deve ser desativado
        output = self.drop(pooled_output)

        # O método self.out() aplica ao vetor do token CLS a camada de transformação linear, cujo objetivo é
        # Retornar as predições do modelo para as classes de saída
        return self.out(output)