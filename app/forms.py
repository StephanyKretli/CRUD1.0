from django.forms import ModelForm
from app.models import Usuarios

# Create the form class.
class UsuariosForm(ModelForm):
   class Meta:
        model = Usuarios
        fields = ['nome', 'data_nasc', 'cpf', 'data_cad']
