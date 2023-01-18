from django.urls import path
from . import views

app_name="posts"

urlpatterns=[
    path("", views.post_list, name="idea-list"),
    path("posts/create", views.post_create, name="idea-create"),
    path("posts/<int:pk>/",views.post_detail, name="idea-detail"),
    path("posts/<int:pk>/delete",views.post_delete, name="idea-delete"),
    path("posts/<int:pk>/update",views.post_update, name="idea-update"),
    
    path("posts/devtool/", views.devtool_list, name="tool-list"),
    path("posts/devtool/create", views.devtool_create, name="tool-create"),
    path("posts/devtool/<int:pk>",views.devtool_detail, name="tool-detail"),
    path("posts/devtool/<int:pk>/delete",views.tool_delete, name="tool-delete"),
    path("posts/devtool/<int:pk>/update", views.devtool_update, name="tool-update"),
]