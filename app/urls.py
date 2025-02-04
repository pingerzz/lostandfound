<<<<<<< HEAD
from django.urls import path
from .views import HomePageView, AboutPageView, AddLostItem, LostItemView, LostItemList, UpdateLostItem, DeleteLostItem, LoginPageView, SignupPageView, ReportPageView, ItemPageView, update_status_to_found, FoundItemPageView, LogOutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('lost-item/', LostItemList.as_view(), name='lost-item'),
    path('lost-item/<int:pk>/', LostItemView.as_view(), name='lost-item-view'),
    path('lost-item/add', AddLostItem.as_view(), name='add-lost-item'),
    path('lost-item/<int:pk>/update', UpdateLostItem.as_view(), name='update-lost-item'),
    path('lost-item/<int:pk>/delete', DeleteLostItem.as_view(), name='delete-lost-item'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('reports/', ReportPageView.as_view(), name='reports'),
    path('item/', ItemPageView.as_view(), name='item'),
    path('update-status-to-found/<int:pk>/', update_status_to_found, name='update-status-to-found'),  # Only one path for this
    path('found-item/', FoundItemPageView.as_view(), name='found-item'),

    path('log-out/', LogOutPageView.as_view(), name='log-out'),
]
=======
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
>>>>>>> 747490cf7a9693f695fb9a8700a8c73271d7b9b7
