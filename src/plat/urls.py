
from .views import edit_plat, plats, update_plat, delete_plat
from django.urls import path

app_name = 'plat'

urlpatterns=[
    path('', edit_plat, name ='edit_plat'),
    path('update/<str:pk>/', update_plat, name="update_plat"),
    path( 'plat' , plats , name=  'plats'),
    path('delete/<int:pk>/', delete_plat, name='delete_plat'),


]