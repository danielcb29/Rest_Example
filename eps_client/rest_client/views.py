import requests

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from rest_client.models import EPS, EPSSerializable

# Por simplicidad se implementa vista basada en funcion


class InicioView(TemplateView):
    """
    Vista encargada de incializar la aplicación, trae todos los resulados y muestra los 6 primeros
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(InicioView, self).get_context_data(**kwargs)

        # Suponiendo que el servidor REST corre en local sobre el puerto 8088
        respuesta = requests.get('http://localhost:8088/rest/eps/')

        resultado = EPSSerializable(data=respuesta.json(), many=True)
        if resultado.is_valid():
            context['resultados'] = resultado.validated_data[:6]
            context['total'] = len(resultado.validated_data)
        else:
            context['resultados'] = []
            context['total'] = 0
        context['codigo'] = 'Todos'
        return context

class BuscarEPSView(TemplateView):
    """
    Vista encargada de la busqueda, soporta busquedas por codigo o vacia para traer todos
    """
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET['search']
        if not codigo:
            return redirect('client:inicio')  # Si no se ingresa código se redirige al inicio
        return super(BuscarEPSView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BuscarEPSView, self).get_context_data(**kwargs)
        codigo = self.request.GET['search']

        # Suponiendo que el servidor REST corre en local sobre el puerto 8088
        respuesta = requests.get('http://localhost:8088/rest/eps/?codigo=' + str(codigo))

        resultado = EPSSerializable(data=respuesta.json(), many=True)  # La API siempre retorna un arreglo
        if resultado.is_valid():
            context['resultados'] = resultado.validated_data
            context['total'] = len(resultado.validated_data)
        else:
            context['resultados'] = []
            context['total'] = 0
        context['codigo'] = codigo
        return context

