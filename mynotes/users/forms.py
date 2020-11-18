from django import forms
from .models import User

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    password = forms.CharField(max_length=20,widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=20,widget=forms.PasswordInput())

    # overwrite the clean method to confirm if password and confirm_password are the same password
    def clean(self):
        cleaned_data = super(signupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

