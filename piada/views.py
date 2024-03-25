from django.shortcuts import render
import requests


def home_view(request):
    # URL da API do Chuck Norris
    api_url = 'http://127.0.0.1:8000/api'

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
