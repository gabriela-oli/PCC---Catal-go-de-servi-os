from .models import Empresa
from django.forms import ModelForm


class EmpresaForm(ModelForm):
    
    class Meta:
        model = Empresa
        fields = "__all__"