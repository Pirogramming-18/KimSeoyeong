from django.urls import path
from server.apps.reviews.views import reviews_list, reviews_create,reviews_detail, reviews_update,reviews_delete 

urlpatterns=[
    path('', reviews_list),
    path('reviews/create',reviews_create),
    path('reviews/<int:pk>',reviews_detail),
    path('reviews/<int:pk>/update',reviews_update),
    path('reviews/<int:pk>/delete',reviews_delete),
]