from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        self.user_cache = None

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Credenciales incorrectas")
            self.user_cache = user

        return cleaned_data


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El usuario ya existe")
        return username

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data["username"],
        )
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user
