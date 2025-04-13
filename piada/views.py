from django.shortcuts import render
from datetime import datetime
import requests


def home_view(request):
    # URL da API do Chuck Norris
    api_url = 'http://127.0.0.1:8001/api'

    # Fazendo requisição [GET]
    response = requests.get(api_url)

    # Verificando status da response
    if response.status_code == 200:
        json = response.json()
        piada = json['joke']
        print('Piada: ', piada)

        return render(request, 'home.html', {'piada': piada})
    
    else:
        # Se a requisição falhar, retorna uma mensagem de erro
        return render(request, 'home.html', {'error': 'Falha ao carregar as piadas'})

# Função para converter formato de data
def formatar_data(data_str):
    # Convertendo a string de data para o formato datetime
    data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%S.%f')
    # Formatando a data no formato brasileiro e sem a hora
    return data.strftime('%d/%m/%Y')

# Views do Histórico
def piadas_historico_view(request):
    # URL da API históricos das piadas
    api_historico_url = 'http://127.0.0.1:8002/api/historico'

    # Obtendo os parâmetros de paginação da query string
    pagina = request.GET.get('paginacao_pagina', 0)
    limite = request.GET.get('paginacao_limite', 10)

    # Verifica se o limite é maior que 0
    if str(limite).isdigit() and int(limite) <= 0:
        limite = 10  # Definir limite padrão se for menor ou igual a 0

    # Fazendo requisição [GET] para a API de histórico das piadas
    response = requests.get(
        api_historico_url,
        params={
            'paginacao_pagina': pagina,
            'paginacao_limite': limite
        }
    )

    # Verificando status da response
    if response.status_code == 200:
        dados_response = response.json()

        total_piadas = dados_response['total']
        paginas = dados_response['paginas']
        pagina_atual = dados_response['pagina']
        limite = dados_response['limite']
        piadas = dados_response['jokes']

        # Formatando a data de cada piada
        piadas = dados_response['jokes']
        for piada in piadas:
            piada['data_get'] = formatar_data(piada['data_get'])

        # Cria uma lista de páginas para navegação
        lista_paginas = range(paginas)

        return render(request, 'historico.html', {
            'total_piadas': total_piadas,
            'paginas': paginas,
            'pagina_atual': pagina_atual,
            'limite': limite,
            'piadas': piadas,
            'lista_paginas': lista_paginas
        })
    else:
        # Se a requisição falhar, retorna uma mensagem de erro
        return render(request, 'historico.html', {'error': 'Falha ao carregar o histórico das piadas'})
