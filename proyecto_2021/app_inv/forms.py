from django import forms

from .models import Categoria, SubCategoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'descripcion', 'estado'
        ]

        labels = {
            "descripcion": "Descripción de la Categoría",
            "estado": "Estado"
        }

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    #para que no muestre los que tienen estado false
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:

        model = SubCategoria

        fields = [
            'categoria', 'descripcion', 'estado'
        ]

        labels = {
            "descripcion": "Sub Categoría",
            "estado": "Estado"
        }

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Descripción de la SubCategoría'
            })
        
        self.fields['categoria'].empty_label = "Seleccione la Categoría"
