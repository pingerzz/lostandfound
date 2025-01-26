from django.shortcuts import render
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

