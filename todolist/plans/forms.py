from django import forms
from django.forms import TextInput

from .models import *

class AddDealForm(forms.ModelForm):
    class Meta:
        model = ActiveList
        fields = ['deal']

        widgets = {
            'deal':TextInput(attrs={
                'class':'form-control',
                'placeholder' : "Помыть посуду",
                'id' : "exampleFormControlInput2"
            })
        }

