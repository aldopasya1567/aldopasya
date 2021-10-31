from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {
        'title':'Home',
        'judul':'Aldopasya'
    }

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
    
class MusicView(TemplateView):
    template_name = 'music.html'
    extra_context = {
        'title':'music',
        'judul':'Music'
    }

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

class VideoView(TemplateView):
    template_name = 'Editing Video.html'
    extra_context = {
        'title':'video',
        'judul':'Video Cinematic'
    }

    def get_context_data(self, *args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)