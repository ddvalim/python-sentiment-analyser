# python-sentiment-analyser

### Objetivo

O objetivo do projeto é implementar uma API que utiliza o algoritmo de aprendizado de máquina BERT para análise de sentimento em texto.

Para poupar tempo e recurso, foi usado um modelo pré-treinado para classificar o texto de entrada entre os rótulos de `negative`, `neutral` & `positive`. 

### Tecnologias

Este projeto foi desenvolvido utilizando a linguagem de programação __Python__ junto do uso do algoritmo de aprendizado de máquina __BERT__ como um modelo pré-treinado.

### Pré-requisitos

- [Python versão 3.10.6 - Linguagem de Programação](https://www.python.org/downloads/)
- [pip - Gerenciador de Pacotes](https://pip.pypa.io/en/stable/installation/)
- [python3-venv - Gerenciador de Ambientes Virtuais](https://medium.com/@LogeshSakthivel/python-virtual-env-in-windows-and-linux-4a2d4a6030cf)
- [Modelo BERT pré-treinado](https://drive.google.com/uc?id=1V8itWtowCYnb2Bc9KlK9SxGff9WwmogA)

### Instalação

1. Clone o repositório do [python-sentiment-analyser](https://github.com/ddvalim/python-sentiment-analyser).
2. Certifique-se de que as ferramentas citadas anteriormente já estejam instaladas e configuradas na sua máquina.
3. Ative o ambiente virtual Python.
4. Instale os *requirements* do projeto com o comando `pip install -r requirements.txt`
5. Baixe o Modelo BERT pré-treinado e o adicione à pasta `assets`


### Executando o programa

1. Em um terminal, execute o programa principal utilizando o comando `FLASK_APP=main.py flask run`.

### Coleção de Requisições

1. Análise de sentimento em texto
   
```
curl --request POST \
  --url http://localhost:5000/analyse \
  --header 'Content-Type: application/json' \
  --data '{
	"text": "hello, world!"
}'
```

### Autora

A autora do projeto é Diovana Rodrigues Valim, bacharela em Sistemas de Informação pela Universidade Federal de Santa Catarina e engenheira de software no Mercado Livre. Este projeto
é baseado no tutorial `Deploy BERT for Sentiment Analysis as REST API using PyTorch, Transformers by Hugging Face and FastAPI`, disponível [aqui](https://curiousily.com/posts/deploy-bert-for-sentiment-analysis-as-rest-api-using-pytorch-transformers-by-hugging-face-and-fastapi/).
