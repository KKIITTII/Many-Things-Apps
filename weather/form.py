# from django import forms
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
        

# class CityForm(forms.Form):
    
    # name = forms.CharField(max_length=40, 
    #             widget=forms.TextInput(
    #                 attrs={'class': 'form-control', 
    #                        'placeholder': 'Add',
    #                        'aria-label': 'Todo', 
    #                        'aria-describedby': 'add-btn'}
    #                        ))