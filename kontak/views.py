from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from .form import Form
# Create your views here.
class KontakView(ListView):
    model = Post
    template_name = 'kontak.html'
    extra_context = {
        'judul':'Blogger'
    }
    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class HomeView(TemplateView):
    template_name = 'home.html'

class FormViews(FormView):
    template_name = 'create.html'
    form_class = Form
    success_url = reverse_lazy('kontak:list')
    extra_context = {
        'judul':'Buat Post'
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DetailViews(DetailView):
    model = Post
    template_name = 'detail.html'
    extra_context = {
        'title':'Post',
        'judul':'Postingan'
    }

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class UpdateViews(UpdateView):
    model = Post
    form_class = Form
    success_url = reverse_lazy('kontak:list')
    template_name = 'create.html'
    extra_context = {
        'title':'Update',
        'judul':'Update Postingan'
    }

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class DeleteViews(DeleteView):
    model = Post
    template_name = 'confirm delete.html'
    success_url = reverse_lazy('kontak:list')
    extra_context = {
        'title':'Hapus',
        'judul':'Hapus Posting'
    }

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)