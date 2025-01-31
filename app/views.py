from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LostAndFoundItem
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class LostItemList(ListView):
    model = LostAndFoundItem
    context_object_name = 'lostitem'
    template_name = 'app/lostitemlist.html'

    def get_queryset(self):
        # Get only items marked as "Lost"
        return LostAndFoundItem.objects.filter(status='lost')

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

class LoginPageView(TemplateView):
    template_name = 'app/templates/registration/login.html'

class SignupPageView(TemplateView):
    template_name = 'app/templates/registration/signup.html'

class ReportPageView(TemplateView):
    template_name = 'app/reports.html'

class ItemPageView(TemplateView):
    model = LostAndFoundItem
    context_object_name = 'lostitem'
    template_name = 'app/item.html'

class FoundItemPageView(ListView):
    model = LostAndFoundItem
    context_object_name = 'founditems'  # This must match what the template uses
    template_name = 'app/founditem.html'  # Ensures this template is used

    def get_queryset(self):
        # Filter only items with status='found'
        return LostAndFoundItem.objects.filter(status__iexact='found')



def update_status_to_found(request, pk):
    # Get the lost item or return a 404 error if it doesn't exist
    lost_item = get_object_or_404(LostAndFoundItem, pk=pk)

    # Check if the item is "Lost" before changing it to "Found"
    if lost_item.status == 'Lost':
        # Update the status to "Found"
        lost_item.status = 'Found'
        lost_item.save()  # Save the change

    # Redirect to the "Found Items" page
    return redirect('found-item')

class LogOutPageView(TemplateView):
    template_name = 'app/logout page.html'

