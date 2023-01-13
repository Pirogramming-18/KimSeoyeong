from django.shortcuts import render,redirect
from server.apps.reviews.models import Review

# Create your views here.
def reviews_list(request, *args, **kwargs):
    reviews=Review.objects.all()
    # 백엔드 챌린지 정렬
    sort=request.GET.get('sort','최신개봉순')
    if sort == '가나다순':
        reviews=Review.objects.order_by("title")
    elif sort == '별점높은순':
        reviews=Review.objects.order_by("-starRating")
    elif sort == '상영시간순':
        reviews=Review.objects.order_by("-runningTime")
    elif sort=='최신개봉순':
        reviews=Review.objects.order_by("-releaseYear")

    return render(request, "reviews/reviews_list.html",{"reviews":reviews, "sort":sort})

def reviews_detail(request, pk, *args,**kwargs):
    review = Review.objects.all().get(id=pk)
    # 백엔드 챌린지 러닝타임 단위 변환
    hour = review.runningTime // 60
    minute = review.runningTime % 60
    return render(request, "reviews/reviews_detail.html",{"review":review, "hour":hour, "minute":minute})

def reviews_create(request, *args, **kwargs):
    review=Review
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
    return render(request, "reviews/reviews_create.html",{"review":review})

def reviews_update(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)
    if request.method=="POST":
        review.title=request.POST["title"]
        review.releaseYear=request.POST["releaseYear"]
        review.genre=request.POST["genre"]
        review.starRating=request.POST["starRating"]
        review.runningTime=request.POST["runningTime"]
        review.reviewContent=request.POST["reviewContent"]
        review.director=request.POST["director"]
        review.mainActor=request.POST["mainActor"]
        review.save()
        return redirect(f"/reviews/{review.id}")
    return render(request, "reviews/reviews_update.html", {"review":review})

def reviews_delete(request, pk, *args, **kwargs):
    if request.method=="POST":
        review=Review.objects.all().get(id=pk)
        review.delete()
    return redirect("/")