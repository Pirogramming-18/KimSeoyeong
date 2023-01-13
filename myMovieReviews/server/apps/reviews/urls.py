from django.urls import path
from server.apps.reviews.views import reviews_list,reviews_create,reviews_detail

urlpatterns=[
    path('', reviews_list),
    path('reviews/create',reviews_create),
    path('reviews/<int:pk>',reviews_detail),
]