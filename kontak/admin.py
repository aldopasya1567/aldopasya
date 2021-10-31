from django.contrib import admin
from .models import Post
# Register your models here.
class ActivateView(admin.ModelAdmin):
    readonly_fields = [
        'publish',
        'update',
        'slug',
    ]
admin.site.register(Post)