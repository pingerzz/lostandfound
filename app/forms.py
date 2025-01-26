from django import forms
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item

        fields = ('name','desc')

        labels = {
            'name':'',
            'desc':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Item Name', 'class':'name'}),
            'desc': forms.Textarea(attrs={'placeholder':'Desc', 'class':'desc'}),
        }
