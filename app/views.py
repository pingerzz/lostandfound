from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.http import HttpResponseRedirect


def home(request):
    item = Item.objects.all()
    return render(request, 'pages/home.html', {'item': item})


def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'pages/additem.html', {'form': form})


def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'pages/edititem.html', {'item': item, 'form': form})


def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/')


def view_item(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, 'pages/viewitem.html', {'item': item})