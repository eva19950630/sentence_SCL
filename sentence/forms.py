from django import forms
from .models import User

class AddUser(forms.Form):
    
    class Meta:
        model = User
        fields = ('uid', 'username', 'email', 'password', 'usericon', 'exp', 'money')
