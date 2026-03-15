from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "categoria", "publicado"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "categoria": forms.TextInput(attrs={"class": "form-control"}),
            "publicado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
