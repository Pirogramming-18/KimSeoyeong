from django.shortcuts import render, redirect
from server.apps.posts.models import Post, Devtool

# Create your views here.
def post_list(request, *args, **kwargs):
    posts=Post.objects.all()
    context={ "posts":posts, }
    return render(request,"posts/post_list.html",context=context)

def post_create(request,*args, **kwargs):
    tools = Devtool.objects.all()
    context={ "tools":tools, }
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            image=request.FILES.get("image"),
            devtool_id=request.POST["devtool"],
            interest=request.POST["interest"],
            content=request.POST["content"],
        )
        post_recent = Post.objects.last()
        return redirect(f"/posts/{post_recent.id}")
    return render(request, "posts/post_create.html",context=context)

def post_detail(request, pk, *args, **kwargs):
    post=Post.objects.get(id=pk)
    context={ 
        "post":post,
         }
    return render(request, "posts/post_detail.html", context=context)

def post_delete(request,pk,*args, **kwargs):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect("/")

def post_update(request,pk,*args, **kwargs):
    post=Post.objects.get(id=pk)
    tools=Devtool.objects.all()
    if request.method=="POST":
        post.title=request.POST["title"]
        post.image=request.FILES.get("image")
        post.devtool_id=request.POST["devtool"]
        post.interest=request.POST["interest"]
        post.content=request.POST["content"]
        post.save()
        return redirect(f"/posts/{post.pk}")
    context={ 
        "post":post,
        "tools":tools,
        "id":post.id,
        }
    return render(request, "posts/post_update.html",context=context)


def devtool_list(request, *args, **kwargs):
    tools=Devtool.objects.all()
    context={ "tools":tools, }
    return render(request, "posts/tool_list.html", context=context)

def devtool_create(request,*args, **kwargs):
    if request.method=="POST":
        Devtool.objects.create(
        name=request.POST["name"],
        kind=request.POST["kind"],
        content=request.POST["content"],
        )
        tool_recent = Devtool.objects.last()
        return redirect(f"/posts/devtool/{tool_recent.id}")
    return render(request, "posts/tool_create.html")

def devtool_detail(request,pk,*args, **kwargs):
    tool=Devtool.objects.get(id=pk)
    all_post=tool.post_set.all()
    context={
        "tool":tool,
        "all_post":all_post,
    }
    return render(request, "posts/tool_detail.html", context=context)

def tool_delete(request,pk,*args, **kwargs):
    tool=Devtool.objects.get(id=pk)
    tool.delete()
    return redirect("/")

def devtool_update(request, pk, *args, **kwargs):
    tool=Devtool.objects.get(id=pk)
    if request.method=="POST":
        tool.name=request.POST["name"]
        tool.kind=request.POST["kind"]
        tool.content=request.POST["content"]
        tool.save()
        return redirect(f"/posts/devtool/{tool.pk}")
    context={ 
        "tool":tool, 
    }
    return render(request, "posts/tool_update.html", context=context)