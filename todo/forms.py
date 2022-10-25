from django.forms import ModelForm
from .models import Create
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ['task', 'status']


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


