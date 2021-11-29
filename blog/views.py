from django.core.files.base import File
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from authen.models import userProfile
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.files.storage import  FileSystemStorage
from django.urls import reverse
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.

@login_required(login_url='login')
def listing(request):
    post = Post.objects.all().order_by("-datetime")
    paginator = Paginator(post, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method=="POST" and "title" in request.POST:
        title=request.POST['title']
        bodyBlog=request.POST['bodyBlog']
        image=request.FILES['upFile']
        dateTime=datetime.now()
        form=Post()
        form.date=dateTime.strftime(" Vào: %H:%M ngày: %d/%m/%Y ")
        form.bodyBlog=bodyBlog
        form.image=image
        form.title=title
        form.auth=request.user
        thLine=""
        if len(bodyBlog)>40:
            thLine=bodyBlog[:40:]+" ...."
        else:
            thLine=bodyBlog
        form.threeLine = thLine
        if form is not None:
            form.save()
            return render(request, 'blog.html', {'page_obj': page_obj, "loi":""})
    if request.method=="POST" and "keySearch" in request.POST:
        key=request.POST["keySearch"]
        p=Post.objects.filter(title__contains=key).order_by('-datetime')
        paginator = Paginator(p, 5)
        page_number = request.GET.get('page')
        pages_obj = paginator.get_page(page_number)
        return render(request, 'blog.html', {'page_obj': pages_obj, "loi":""})
    # xoa bai viet
    # if request.method=="POST" and "delete" in request.POST:
    #     id=request.POST["delete"]
    #     if Post.objects.filter(id=id).exists():
    #         post=get_object_or_404(Post, id=id)
    #         print(post.title)
    #         print(id)
    #         try:
    #             post.delete()
    #         except:
    #             return render(request, 'blog.html', {'page_obj': page_obj, "loi":"khong the xoa!"})
    return render(request, 'blog.html', {'page_obj': page_obj, "loi":""})
@login_required(login_url='login')
def delete_post(request, pk=None):
    if Post.objects.filter(pk=pk).exists:
        post=get_object_or_404(Post, pk=pk)
        post.delete()
    post = Post.objects.all().order_by("-date")
    paginator = Paginator(post, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return HttpResponseRedirect(reverse('blog'))
@login_required(login_url='login')
def post(request, pk):
    post=get_object_or_404(Post, pk=pk)
    id=post.auth_id
    uProfile=userProfile.objects.all()
    userprofile=userProfile.objects.get(user_id=id)
    form=CommentForm()
    if request.method=="POST":
        # form=CommentForm(request.POST,author=request.user, post=post)
        dateTime=datetime.now()
        comment= Comment()
        comment.date=dateTime.strftime(" Vào: %H:%M ngày: %d/%m/%Y ")
        comment.auth=request.user
        comment.body=request.POST["comment"]
        comment.post= post
        if comment is not None:
            comment.save()
            return HttpResponseRedirect(request.path)
    return render(request, "post.html", {"post":post, "form":form, 'userprofile':userprofile,"uProfile":uProfile})

@login_required(login_url='login')
def delete_comment(request, pk=None):
    comment=get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post', comment.post.id)