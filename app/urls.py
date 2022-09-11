from django.urls import path

from .views import *


urlpatterns = [
    path('',ModeloView.as_view(),name="modelo_list"),   
    path('new',ModeloNew.as_view(),name="new"),
    path('edit/<int:pk>',ModeloEdit.as_view(),name="edit"), 
    path('crud',Crud.as_view(),name="crud"),
    path('crud/update',update1,name="update1"),
    path('crud/reload',reload,name="reload"),
    path('delete/<int:pk>',ModeloDel.as_view(),name="delete"), 

    path('crud/update2',update2,name="update2"),

    path('bootstable',BootsTable.as_view(),name="bootstable"),
]