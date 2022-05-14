from django.contrib import admin
from .models import Categorias, Establecimientos, Contacto, Reserva

from .forms import EstablecimientosForm

# Register your models here.


class EstablecimientosAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'ciudad','departamento', 'categoria', 'parqueadero', 'tipo']
    search_fields = ['nombre', 'categoria', 'ciudad', 'departamento', 'parqueadero', 'tipo']
    list_filter = ['categoria', 'ciudad', 'departamento', 'tipo']
    list_per_page = 10


admin.site.register(Categorias)
admin.site.register(Establecimientos, EstablecimientosAdmin)
admin.site.register(Contacto)
admin.site.register(Reserva)

