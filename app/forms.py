from django import forms
<<<<<<< HEAD
from .models import LostAndFoundItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostAndFoundItem
        fields = ['item', 'status', 'category', 'location', 'date', 'contact_name', 'contact_phone']  # Adjust based on your model fields
=======
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
>>>>>>> 747490cf7a9693f695fb9a8700a8c73271d7b9b7
