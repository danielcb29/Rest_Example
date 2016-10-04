import requests

from django.shortcuts import render, redirect

from rest_client.models import EPS, EPSSerializable

# Por simplicidad se implementa vista basada en funcion


def buscar_EPS(request):

    codigo = request.GET['search']

    # Se realiza consulta
    query = '?codigo='+str(codigo) if codigo else ''
    respuesta = requests.get('http://localhost:8088/rest/eps/'+query) # Suponiendo que el servidor REST corre en local sobre el puerto 8088
    resultados = EPSSerializable(data=respuesta.json()[0])
    if not resultados.is_valid():
        resultados = []
    else:
        resultados = [resultados.validated_data]

    return render(request, 'index.html', {
        'resultados': resultados,
        'codigo': codigo
    })
