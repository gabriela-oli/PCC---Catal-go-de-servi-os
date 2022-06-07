from .models import Produto
from django.forms import ModelForm


class ProdutoForm(ModelForm):
    
    class Meta:
        model = Produto
        fields = "__all__"