from django.shortcuts import get_object_or_404,render, redirect
from django.views.decorators.csrf import csrf_exempt
from server.apps.posts.models import Post, Comment
from server.apps.posts.forms import PostForm, CommentForm
from django.http.response import JsonResponse
import json
# Create your views here.

def post_base (request, *args, **kwargs):  #메인페이지
    posts = Post.objects.all()
    form = CommentForm()
    ctx={
        'posts': posts,
        'form': form
    }
    return render (request, 'posts/base.html', ctx)

def post_new(request, *args, **kwargs):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_base')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'posts/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'posts/post_new.html', ctx)

# 좋아요 기능
@csrf_exempt
def like_ajax(reqeust, *args, **kwargs):
    req = json.loads(reqeust.body)
    post_id=req['id']

    post = Post.objects.get(id=post_id)

    if post.like==True:
        post.like = False
    else:
        post.like = True
    
    post.save()

    status=post.like
    return JsonResponse({'id':post_id, 'status':status})

# 댓글 작성
@csrf_exempt
def comment_ajax(request, *args, **kwargs):
    req = json.loads(request.body)
    
    post_id = req['id']
    comment_content = req['comment']
    comment = Comment()
    comment.post = get_object_or_404(Post, pk=post_id)
    comment.comment = comment_content
    comment.save()
    return JsonResponse({'id': post_id, 'comment': comment_content, 'comment_id': comment.id})


# 댓글 지우기
@csrf_exempt
def delete_comment_ajax(request, *args, **kwargs):
    req = json.loads(request.body)
    comment_id = req['id']
    post_id = req['post_id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id, 'post_id': post_id})