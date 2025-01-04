from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.add_item, name='add-item'),
    path('edititem/<item_id>', views.edit_item, name='edit-item'),
    path('deleteitem/<item_id>', views.delete_item, name='delete-item'),
    path('viewitem/<item_id>', views.view_item, name='view-item'),
]