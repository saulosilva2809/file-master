from .models import User

from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import (
    AuthenticationForm as BaseAuthenticationForm
)


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AuthenticationForm(BaseAuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')
