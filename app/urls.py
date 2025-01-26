from django.urls import path
<<<<<<< HEAD
from .views import HomePageView, AboutPageView, AddLostItem, LostItemView, LostItemList, UpdateLostItem, DeleteLostItem

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('lost-item/', LostItemList.as_view(), name='lost-item'),
    path('lost-item/<int:pk>', LostItemView.as_view(), name='lost-item-view'),
    path('lost-item/add', AddLostItem.as_view(), name='add-lost-item'),
    path('lost-item/<int:pk>/update', UpdateLostItem.as_view(), name='update-lost-item'),
    path('lost-item/<int:pk>/delete', DeleteLostItem.as_view(), name='delete-lost-item'),

]
=======
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.add_item, name='add-item'),
    path('edititem/<item_id>', views.edit_item, name='edit-item'),
    path('deleteitem/<item_id>', views.delete_item, name='delete-item'),
    path('viewitem/<item_id>', views.view_item, name='view-item'),
]
>>>>>>> 99fd0ab869c0cdfd9b146f3a3b0f1108d21af5d3
