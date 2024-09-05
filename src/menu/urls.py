
from .views import edit_menu, menus, update_menu, delete_menu
from django.urls import path

app_name = 'menu'

urlpatterns=[
    path('', edit_menu, name ='edit_menu'),
    path('update/<str:pk>/', update_menu, name="update_menu"),
    path( 'menu' , menus , name=  'menus'),
    path('delete/<int:pk>/', delete_menu, name='delete_menu'),


]