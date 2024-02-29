from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome",]
        

class ProdutoEditForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome",]
    