from django.shortcuts import render
from server.apps.reviews.models import Review

# Create your views here.
def reviews_list(request, *args, **kwargs):
    reviews=Review.objects.all()
    return render(request, "reviews/reviews_list.html",{"reviews":reviews})