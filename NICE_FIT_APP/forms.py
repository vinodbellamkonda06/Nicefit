from django import forms
from .models import User


class Signupform(forms.ModelForm):
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'
