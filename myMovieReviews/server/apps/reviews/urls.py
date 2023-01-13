from django.urls import path
from server.apps.reviews.views import reviews_list

urlpatterns=[
    path('', reviews_list),
]