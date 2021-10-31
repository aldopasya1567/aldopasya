from django import forms
from .models import Post

class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'nama_lengkap',
            'judul',
            'isi',
            'penulis'
        ]
