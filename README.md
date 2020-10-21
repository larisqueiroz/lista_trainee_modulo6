# Lista do Módulo 6 - Trainee

### Larissa Queiroz 
\
Observações:  
> As aplicações foram feitas usando Docker Toolbox e o padrão de acesso é o endereço "192.168.99.101", mas foram configuradas também para o acesso pelo localhost. As collections do Postman estão disponíveis para testes.
>
\
1ª QUESTÃO: Qual o motivo para realizar o carregamento do modelo fora dos endpoint na aplicação flask? Pergunta relativa ao iris-classifier-API. 

Carregando fora das rotas, o modelo pode ser acessado por mais de uma. Se o modelo é carregado em uma rota, há um custo maior de tempo na requisição.

\
2ª e 4ª QUESTÕES: Implemente o iris-classifier-API utilizando Django 2.0 e Django Rest Framework. Veja vídeo aula com explicações sobre esse exercício. Sirva o iris-classfier-API feito com Django 2.0 e Django Rest Framework utilizando docker. (Pasta API-docker-django)

```
(Acessar pasta "API-docker-django2")

docker-compose up --build
```

\
3ª e 5ª QUESTÕES: Implemente o iris-classifier-API utilizando FastAPI. Veja vídeo aula com explicações sobre esse exercício. Sirva o iris-classifier-API feito com FastAPI utilizando docker.

```
(Acessar a pasta "API-docker-fastapi/src")

docker-compose up --build
```

\
6ª QUESTÃO: Crie uma API que contenha um churn detector para os dados de utilização do
Globo Play. Não se preocupe com o resultado e assertividade de modelo de
ML nesse momento. Se preocupe em desenvolver um pipeline, servil-lo,
treinar um modelo de ML e servi-lo. Taxas de acerto não serão avaliadas
aqui, apenas a entrega da solução final. Seu pipeline pode ser diferente do
proposto pelo meu.

```
(Acessar a pasta "Churn_Detector/src")

uvicorn app:app --reload
```
