from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import *
from .forms import *

class ModeloView(generic.ListView):
    permission_required = "app.view_modelo"
    model = Modelo
    template_name = "app/modelo_list.html"
    context_object_name = "obj"

class ModeloNew(generic.CreateView):
    permission_required="app.add_modelo"
    model=Modelo
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=ModeloForm
    success_url=reverse_lazy("app:modelo_list")
    

class ModeloEdit(generic.UpdateView):
    permission_required="app.change_modelo"
    model=Modelo
    template_name="app/modelo_form.html"
    context_object_name = "obj"
    form_class=ModeloForm
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ModeloDel(generic.DeleteView):
    permission_required="app.delete_modelo"
    model=Modelo
    template_name='app/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Eliminado Satisfactoriamente"