from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User

class HistorialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = ('id','fechaEntrada','horaEntrada','fechaSalida','horaSalida')
        extra_kwargs = {
            'horaEntrada': {'format': '%H:%M:%S'} ,
            'horaSalida':  {'format': '%H:%M:%S'},
        }

class ClientesSerializers(serializers.ModelSerializer):
    historial = HistorialSerializers(many=True, read_only=True)
    class Meta:
        model = Clientes
        fields = ('id', 'nombre', 'dni', 'edad', 'estado','historial')

class DiscotecaSerializers(serializers.ModelSerializer):
    #Añadir las subclases dentro del array
    clientes = ClientesSerializers(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username','password','UbicacionDiscoteca','clientes')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password', instance.password))
        instance.UbicacionDiscoteca = validated_data.get('UbicacionDiscoteca', instance.UbicacionDiscoteca)
        instance.save()
        return instance
    