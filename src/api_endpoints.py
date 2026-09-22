import requests

base_url = "https://dragonball-api.com/api"

# Criar as funcoes que irao pegar os dados da api
# nome da funcao deve ter o prefixo get, post ou put


def get_itens():
    # 1 - Definir o endpoint que vai ser consumido
    url = f'{base_url}/itens'

    # 2 - Fazer a requisição (pedindo os dados)
    dados = requests.get(url)

    # 3 - Retornar os dados
    return dados.json()



def get_meus_itens():
    # 1 - Definir o endpoint que vai ser consumido
    url = f'{base_url}/itens'

    # 2 - Fazer a requisição (pedindo os dados)
    dados = requests.get(url)

    # 3 - Retornar os dados
    return dados.json()



def get_notificacao():
    url = f'{base_url}/notificacao'
    dados = requests.get(url)