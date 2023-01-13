from django.urls import path
from server.apps.reviews.views import reviews_list,reviews_detail

urlpatterns=[
    path('', reviews_list),
    path('reviews/<int:pk>',reviews_detail),
]