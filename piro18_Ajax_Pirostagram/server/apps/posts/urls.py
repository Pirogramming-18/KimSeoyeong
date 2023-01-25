from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('', views.post_base, name='post_base'),
    path('post_new', views.post_new, name='post_new'),  
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('delete_comment_ajax/', views.delete_comment_ajax, name='delete_comment_ajax'),
]