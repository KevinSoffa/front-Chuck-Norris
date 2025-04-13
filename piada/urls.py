from django.urls import path
from .views import home_view, piadas_historico_view


app_name = 'piada'

urlpatterns = [
    path('piadas/chuck-norris', home_view, name='piada'),
    path('piadas/chuck-norris/historico', piadas_historico_view, name='historico')
]