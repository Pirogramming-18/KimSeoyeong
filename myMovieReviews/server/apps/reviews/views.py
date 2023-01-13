from django.shortcuts import render,redirect
from server.apps.reviews.models import Review

# Create your views here.
def reviews_list(request, *args, **kwargs):
    reviews=Review.objects.all()
    return render(request, "reviews/reviews_list.html",{"reviews":reviews})

def reviews_detail(request, pk, *args,**kwargs):
    review = Review.objects.all().get(id=pk)
    return render(request, "reviews/reviews_detail.html",{"review":review})

def reviews_create(request, *args, **kwargs):
    if request.method =="POST":
        Review.objects.create(
            title=request.POST["title"],
            releaseYear=request.POST["releaseYear"],
            director=request.POST["director"],
            mainActor=request.POST["mainActor"],
            genre=request.POST["genre"],
            starRating=request.POST["starRating"],
            runningTime=request.POST["runningTime"],
            reviewContent=request.POST["reviewContent"],
        )
        # 리뷰 리스트 페이지로 이동하도록
        return redirect('/')
    return render(request, "reviews/reviews_create.html")

def reviews_delete(request, pk, *args, **kwargs):
    if request.method=="POST":
        review=Review.objects.all().get(id=pk)
        review.delete()
    return redirect("/")