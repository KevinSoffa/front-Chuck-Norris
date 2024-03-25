from django.urls import path
from .views import home_view


app_name = 'piada'

urlpatterns = [
    path('piadas/chuck-norris', home_view, name='piada')
]