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

    path('datatable',DataTable.as_view(),name="datatable"),
    path('datatable/crud',datatable,name="datatable2"),

    path('datatable-custom',DataTableCustom.as_view(),name='datatable_custom'),

    path('bootstrap-table',BoostrapTable.as_view(),name="bootstrap_table"),
    path('crud/reload2',reload2,name="reload2"),
]