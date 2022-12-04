from django import urls
from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'backend'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #Ver todas las discotecas 
    path('discoteca', views.DiscotecaList.as_view(), name='discotecas'),
    #http://127.0.0.1:8000/discoteca

    #Ver todos los clientes activos o no de una discoteca
    path('discoteca/<str:nombreDisco>', views.DiscotecaDetail.as_view(), name='discoteca'),
    #http://127.0.0.1:8000/discoteca/"nombre de la discoteca"


    #Ver todos los clientes de una discoteca
    path('discoteca/<str:nombreDisco>/clientes', views.ClientesByDiscoteca.as_view(), name='clientes'),
    #http://127.0.0.1:8000/discoteca/"nombre de la discoteca"/clientes

    #Ver todos los clientes activos de una discoteca
    path('discoteca/<str:nombreDisco>/clientesActivos', views.ClientesActivosByDiscoteca.as_view(), name='clientesActivos'),
    #http://127.0.0.1:8000/discoteca/"nombre de la discoteca"/clientesActivos


    #Ver solo un cliente de una discoteca para editar elimnar
    path('discoteca/<str:nombreDisco>/clientes/<str:dni>', views.unClienteByDiscoteca.as_view(), name='unCliente'),
    #http://127.0.0.1:8000/discoteca/"nombre de la discoteca"/clientes/"dni del cliente"



    #Ver historial de un cliente de una discoteca
    path('discoteca/<str:nombreDisco>/clientes/<str:dni>/historial', views.historialByCliente.as_view(), name='historial'),
    #http://localhost:8000/discoteca/"nombre discoteca"/clientes/" dni cliente"/historial

    #Editar un historial de un cliente 
    path('discoteca/<str:nombreDisco>/clientes/<str:dni>/historial/<int:id>', views.unHistorialByCliente.as_view(), name='unHistorial'),

    #Ultimo historial
    path('discoteca/<str:nombreDisco>/clientes/<str:dni>/historial/ultimo', views.ultimoHistorialByCliente.as_view(), name='ultimoHistorial'),
]