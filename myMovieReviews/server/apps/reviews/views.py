from django.shortcuts import render
from server.apps.reviews.models import Review

# Create your views here.
def reviews_list(request, *args, **kwargs):
    reviews=Review.objects.all()
    return render(request, "reviews/reviews_list.html",{"reviews":reviews})

def reviews_detail(request, pk, *args,**kwargs):
    review = Review.objects.all().get(id=pk)
    return render(request, "reviews/reviews_detail.html",{"review":review})

def reviews_create(request, *args, **kwargs):
    return render(request, "reviews/reviews_create.html")