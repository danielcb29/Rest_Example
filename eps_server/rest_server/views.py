from django.shortcuts import render,get_object_or_404
from rest_framework import mixins,viewsets
from rest_framework import permissions
from rest_server.models import EPS, EPSSerializable
# Create your views here.


class EPSListView(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    Vista encargada de listar las eps y obtenerlas por código mediante GET con query
    """
    queryset = EPS.objects.all()
    serializer_class = EPSSerializable
    permission_classes = (permissions.AllowAny, )

    def list(self, request, *args, **kwargs):
        if 'codigo' in request.query_params:
            self.queryset = self.queryset.filter(codigo=request.query_params.get('codigo'))
        return super(EPSListView, self).list(request, *args, **kwargs)

