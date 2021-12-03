from django.urls import path

from .views import *


urlpatterns = [
    path('',ModeloView.as_view(),name="modelo_list"),   
    path('new',ModeloNew.as_view(),name="new"),
    path('edit/<int:pk>',ModeloEdit.as_view(),name="edit"), 
]