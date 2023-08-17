from django import forms
from .models import Reg_Data

class Reg_Data_Form(forms.ModelForm):
    class Meta:
        model = Reg_Data
        fields = ['name', 'email', 'phone', 'address', 'img']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'img': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
