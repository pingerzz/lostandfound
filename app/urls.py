from django.urls import path
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
