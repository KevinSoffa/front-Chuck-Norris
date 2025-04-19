from django.shortcuts import render
from kafka import KafkaProducer
from datetime import datetime
import json as json_lib
import requests


def home_view(request):
    api_url = 'http://127.0.0.1:8001/api'

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            piada = data.get('joke', 'Sem piada no momento.')

            print('Piada recebida:', piada)

            # Envia para o Kafka
            try:
                producer = KafkaProducer(
                    bootstrap_servers=['localhost:9092'],
                    value_serializer=lambda v: json_lib.dumps(v).encode('utf-8')
                )
                producer.send('python_kafka_kevin', {'piada': piada})
                producer.flush()
                print("Piada enviada para o Kafka.")
            except Exception as e:
                print(f"Erro ao enviar para Kafka: {e}")

            return render(request, 'home.html', {'piada': piada})

        else:
            return render(request, 'home.html', {'error': 'Falha ao carregar a piada.'})

    except Exception as e:
        print(f"Erro na requisição à API: {e}")
        return render(request, 'home.html', {'error': 'Erro de conexão com a API.'})

# Função para converter formato de data
def formatar_data(data_str):
    # Convertendo a string de data para o formato datetime
    data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%S.%f')
    # Formatando a data no formato brasileiro e sem a hora
    return data.strftime('%d/%m/%Y')

# Views do Histórico
def piadas_historico_view(request):
    api_historico_url = 'http://127.0.0.1:8002/api/historico'

    # Pegando os valores da URL (começando de 1 por padrão)
    pagina_param = request.GET.get('paginacao_pagina', '1')
    limite = request.GET.get('paginacao_limite', '10')

    # Validando o valor da página
    if pagina_param.isdigit():
        pagina = int(pagina_param)
        if pagina < 1:
            pagina = 1
    else:
        pagina = 1

    # Validando limite
    if limite.isdigit() and int(limite) > 0:
        limite = int(limite)
    else:
        limite = 10

    # Enviando para a API com índice baseado em zero
    response = requests.get(
        api_historico_url,
        params={
            'paginacao_pagina': pagina - 1,  # <-- ajustado aqui!
            'paginacao_limite': limite
        }
    )

    if response.status_code == 200:
        dados_response = response.json()

        total_piadas = dados_response['total']
        paginas = dados_response['paginas']
        pagina_atual = dados_response['pagina'] + 1  # <-- ajustado aqui!

        piadas = dados_response['jokes']
        for piada in piadas:
            piada['data_get'] = formatar_data(piada['data_get'])

        # Gera lista de páginas (baseada em 1)
        lista_paginas = range(1, paginas + 1)

        return render(request, 'historico.html', {
            'total_piadas': total_piadas,
            'paginas': paginas,
            'pagina_atual': pagina_atual,
            'limite': limite,
            'piadas': piadas,
            'lista_paginas': lista_paginas
        })

    else:
        return render(request, 'historico.html', {'error': 'Falha ao carregar o histórico das piadas'})
