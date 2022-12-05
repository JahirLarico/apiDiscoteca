from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.


class IndexView(APIView):
    def get(self, request):
        return Response( 'Servidor de la API de la discoteca')

class DiscotecaList(APIView):
    def get(self, request):
        discotecas = CustomUser.objects.all()
        serializer = DiscotecaSerializers(discotecas, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DiscotecaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DiscotecaDetail(APIView):
    def get(self, request, nombreDisco):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        serializer = DiscotecaSerializers(discoteca)
        return Response(serializer.data)
    def put(self, request, nombreDisco):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        serializer = DiscotecaSerializers(discoteca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, nombreDisco):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        discoteca.delete()
        return Response('Discoteca eliminada')

class ClientesByDiscoteca(APIView):
    def get(self, request, nombreDisco):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        clientes = Clientes.objects.filter(discoteca=discoteca)
        serializer = ClientesSerializers(clientes, many=True)
        return Response(serializer.data)
    def post(self, request, nombreDisco):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        serializer = ClientesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(discoteca=discoteca)
            return Response(serializer.data)
        return Response(serializer.errors)

class unClienteByDiscoteca(APIView):
    def get(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        serializer = ClientesSerializers(cliente)
        return Response(serializer.data) 
    def put(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        serializer = ClientesSerializers(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        cliente.delete()
        return Response('Cliente eliminado')


class ClientesActivosByDiscoteca(APIView):
    def get(self, request, nombreDisco):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        clientes = Clientes.objects.filter(discoteca=discoteca, estado=True)
        serializer = ClientesSerializers(clientes, many=True)
        return Response(serializer.data)





class historialByCliente(APIView):
    def get(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        historial = Historial.objects.filter(cliente=cliente)
        serializer = HistorialSerializers(historial, many=True)
        return Response(serializer.data)
    def post(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        serializer = HistorialSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(cliente=cliente)
            return Response(serializer.data)
        return Response(serializer.errors)


class unHistorialByCliente(APIView):
    def get(self, request, nombreDisco, dni, id):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        historial = Historial.objects.get(id=id, cliente=cliente)
        serializer = HistorialSerializers(historial)
        return Response(serializer.data)
    def put(self, request, nombreDisco, dni, id):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        historial = Historial.objects.get(id=id, cliente=cliente)
        serializer = HistorialSerializers(historial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, nombreDisco, dni, id):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        historial = Historial.objects.get(id=id, cliente=cliente)
        historial.delete()
        return Response('Historial eliminado')
        
class ultimoHistorialByCliente(APIView):
    def get(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        historial = Historial.objects.filter(cliente=cliente).order_by('-id')[0]
        serializer = HistorialSerializers(historial)
        return Response(serializer.data)
    
    def put(self, request, nombreDisco, dni):
        discoteca = CustomUser.objects.get(username=nombreDisco)
        cliente = Clientes.objects.get(dni=dni, discoteca=discoteca)
        historial = Historial.objects.filter(cliente=cliente).order_by('-id')[0]
        serializer = HistorialSerializers(historial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
