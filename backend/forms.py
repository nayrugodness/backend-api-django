from django import forms
from .models import Contacto, Reserva, Establecimientos, Categorias, Users
from django.db.models import fields
from django.forms import widgets, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator