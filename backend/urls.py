from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('establecimientos', views.EstablecimientosViewset)
router.register('categoria', views.CategoriasViewset)
router.register('usuarios', views.UsersViewset)
router.register('contacto', views.ContactoViewset)
router.register('reserva', views.ReservasViewset)

# localhost:8000/api/establecimiento/


urlpatterns = [
    path('api/', include(router.urls))
]
