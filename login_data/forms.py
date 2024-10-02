from django import forms
from .models import LoginData

class LoginDataForm(forms.ModelForm):
    class Meta:
        model = LoginData
        fields = '__all__'