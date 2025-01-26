from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LostAndFoundItem
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class LostItemList(ListView):
    model = LostAndFoundItem
    context_object_name = 'lostitem'
    template_name = 'app/lostitemlist.html'

class LostItemView(DetailView):
    model = LostAndFoundItem
    context_object_name = 'lostitem'
    template_name = 'app/lostitemdetail.html'

class AddLostItem(CreateView):
    model = LostAndFoundItem
    fields = ['item','description','category','status','location','date','contact_name','contact_phone','image']
    template_name = 'app/addlostitem.html'

class UpdateLostItem(UpdateView):
    model = LostAndFoundItem
    fields = ['item','description','category','status','location','date','contact_name','contact_phone','image']
    template_name = 'app/updatelostitem.html'

class DeleteLostItem(DeleteView):
    model = LostAndFoundItem
    template_name = 'app/deletelostitem.html'
    success_url = reverse_lazy('lost-item')

=======
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
>>>>>>> 99fd0ab869c0cdfd9b146f3a3b0f1108d21af5d3
