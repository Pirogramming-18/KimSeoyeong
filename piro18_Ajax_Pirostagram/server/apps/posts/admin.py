from django.contrib import admin
from server.apps.posts.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
