
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

class UserRegistratinForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['username', 'email', 'password1', 'password2']


