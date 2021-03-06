from django.db.models.query import QuerySet
from .models import Categorias, Establecimientos, Reserva, Users, Contacto
from rest_framework import fields, serializers


class CategoriasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorias
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = '__all__'

class EstablecimientosSerializer(serializers.ModelSerializer):

    nombre_categoria = serializers.CharField(
        read_only=True, source='categoria.nombre')
    categoria = CategoriasSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorias.objects.all(), source='categoria')
    nombre = serializers.CharField(required=True, min_length=3)

    # def validate_nombre(self, value):
    #     existe = Producto.objects.filter(nombre=value).exists()

    #     if existe:
    #         raise serializers.ValidationError('Este producto ya existe')

    #     else:
    #         return value

    class Meta:
        model = Establecimientos
        fields = '__all__'
        #exclude = ['']

class ReservasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = '__all__'