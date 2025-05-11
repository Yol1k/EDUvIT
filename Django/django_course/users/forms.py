from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["password"].label = ""

        self.fields["username"].widget = forms.TextInput(
            attrs={
                "placeholder": "Имя пользователя",
                "class": "form-control",
            }
        )

        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "class": "form-control",
            }
        )

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

        self.fields["username"].widget = forms.TextInput(
            attrs={
                "placeholder": "Имя пользователя",
                "class": "form-control",
            }
        )

        self.fields["password1"].widget = forms.TextInput(
            attrs={
                "placeholder": "Пароль",
                "class": "form-control",
            }
        )

        self.fields["password2"].widget = forms.TextInput(
            attrs={
                "placeholder": "Подтвердите пароль",
                "class": "form-control",
            }
        )