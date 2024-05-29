import json

import torch
import torch.nn.functional as F

from transformers import BertTokenizer
from core.ports import classifier as c

with open("config.json") as json_file:
    config = json.load(json_file)

class Analyser_Service():
    def __init__(self) -> None:
        # Instância da classe tokenizer, responsável por transformar texto em unidades menores chamadas tokens
        self.tokenizer = BertTokenizer.from_pretrained(config['BERT_MODEL'])

        # Determina o dispositivo onde o modelo executará
        self.device = torch.device('cpu')

        # Instância da classe Classifier, responsável por processar a informação
        classifier = c.Classifier(len(config['CLASS_NAMES']))

        # Atribuí à instância Classifier o universo de vocabulário do modelo
        classifier.load_state_dict(torch.load(config['PRE_TRAINED_MODEL'], map_location=self.device))

        # Desativa o pooling do Classifier e configura o dispositivo onde o modelo executará
        self.classifier = classifier.eval().to(self.device)

    def analyse(self, text: str):
        # Tokenização: Processo de transformação do texto de entrada em partes menores, tokens, representados por tensores
        # Tensores são uma estrutura de dados multidimensional
        encoded_text = self.tokenizer.encode_plus(
            text,
            max_length=config["MAX_SEQUENCE_LEN"],
            add_special_tokens=True,
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors="pt",
        )
        
        # Processo de transferência dos tokens (tensores) para o dispositivo onde ocorrerá o processo de classificação
        input_ids = encoded_text["input_ids"].to(self.device)

        # Processo de transferência da attention_mask (conjunto de tokens essenciais ao processamento dos dados) ao 
        # Dispositivo onde ocorrerá o processo de classificação
        attention_mask = encoded_text["attention_mask"].to(self.device)

        # Desabilitando o processo de propagação de gradientes. Gradientes são a variação de uma função ante seus parâmetros
        with torch.no_grad():
            # Calculo de probabilidades da ocorrência de cada classe em um conjunto de tokens
            # A chamada de self.classifier() executa de forma implicícita a função forward() da classe Classifier.
            # No método forward, os inputs serão processados de maneira a retornar as predições do modelo para cada classe.
            # A função F.softmax() converte a saída do modelo em probabilidades
            probabilities = F.softmax(self.classifier(input_ids, attention_mask), dim=1)
        
        # Cálculo da confiança dos resultados do modelo ao longo de uma dimensão baseando-se no valor máximo de probabilidade
        # De ocorrência de cada classe. Retorna o índice de confiança e, com base na probabilidade máxima, a classe prevista
        confidence, predicted_class = torch.max(probabilities, dim=1)

        # Conversão dos resultados obtidos para um padrão human-readable
        predicted_class = predicted_class.cpu().item()
        probabilities = probabilities.flatten().cpu().numpy().tolist()

        return (
            config["CLASS_NAMES"][predicted_class],
            confidence,
            dict(zip(config["CLASS_NAMES"], probabilities)),
        )