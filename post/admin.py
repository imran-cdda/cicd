from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "length"]
    search_fields = ["title"]
    list_filter = ['title']

admin.site.register(Post, PostAdmin)
