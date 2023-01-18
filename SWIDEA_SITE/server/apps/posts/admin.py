from django.contrib import admin
from server.apps.posts.models import Post, Devtool

# Register your models here.
admin.site.register(Post)
admin.site.register(Devtool)