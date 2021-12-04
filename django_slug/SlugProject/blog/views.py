from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
import blog

def postlist(request):
    posts=Post.objects.all()
    return render(request,"blog/post_list.html",{"posts":posts})

def postDetails(request,slug):
    posts=Post.objects.filter(slug=slug)
    if posts.exists():
        post=posts.first()
    context={
        'post':post
    }
    return render(request,"blog/post_details.html",context)

def postsave(request):
    if request.method=="POST":
        postForm=PostForm(request.POST)
        if postForm.is_valid():
            post = Post(title=postForm.cleaned_data['title'],
                        content =postForm.cleaned_data['content'],
                        author_id =1)
            post.save()
            return HttpResponseRedirect(reverse(blog.views.postlist))
    else:
        postForm=PostForm()
    context={
        "formData":postForm
    }
    return render(request,"blog/post_save.html",context)
