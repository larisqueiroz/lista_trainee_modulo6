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

docker-compose up
```

\
3ª e 5ª QUESTÕES: Implemente o iris-classifier-API utilizando FastAPI. Veja vídeo aula com explicações sobre esse exercício. Sirva o iris-classifier-API feito com FastAPI utilizando docker.

```
(Acessar a pasta "API-docker-fastapi")

docker-compose up
```
