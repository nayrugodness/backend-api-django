from .models import Categorias, Establecimientos, Users, Contacto, Reserva
from rest_framework import viewsets
from .serializers import EstablecimientosSerializer, CategoriasSerializer, UsersSerializer, ContactoSerializer, ReservasSerializer


# Create your views here.
class EstablecimientosViewset(viewsets.ModelViewSet):
    queryset = Establecimientos.objects.all()
    serializer_class = EstablecimientosSerializer

    def get_queryset(self):
        establecimiento = Establecimientos.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            establecimiento = establecimiento.filter(nombre__contains=nombre)
            return establecimiento
        else:
            return establecimiento
class CategoriasViewset(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
class ContactoViewset(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
class ReservasViewset(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer

