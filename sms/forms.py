from django import forms
from django.forms import ModelForm
from .models import StudentModel


class StdModelForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email', 'password': 'Password'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }
        