from django import forms
from django.contrib.auth.forms import UserCreationForm, User

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

    email = forms.CharField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
        for field_name in ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'):
            self.fields[field_name].help_text = ''

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
            }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
            }
    ))
    fields = ['username', 'password']

