from django.db.models.fields import NullBooleanField
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from authen.models import userProfile
from django.core.files.storage import  FileSystemStorage
# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')
    
@login_required(login_url='login')
def profile(request, id=None):
    if request.method=="POST":
        userprofile=userProfile.objects.get(user_id=id)
        image=request.FILES['upAvatar']
        userprofile.avatar=image
        userprofile.save()
        
    user=User.objects.get(id=id)
    userprofile=userProfile.objects.get(user_id=id)
    try:
        print(userprofile.avatar.url,"----------------check avatar-------------")
    except :
        userprofile.avatar='/user.jpg'
        userprofile.save()
    name=user.username
    # print(user.userprofile.avatar.url,"----------------12345-------------")
    post = Post.objects.filter(auth_id=id).order_by("-date")
    soPost=post.count()
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    pages_obj = paginator.get_page(page_number)
    return render(request, 'profile.html', {"pages_obj":pages_obj,
     "soPost":soPost, "User":user,"userprofile":userprofile, "id":id})
def edit(request):
    if request.method=="POST":
        user=request.user
        userprofile=userProfile.objects.get(user_id=user.id)
        image=request.FILES['avatar']
        userprofile.avatar=image
        userprofile.save()
        return redirect('profile', user.id)
    return render(request, 'editProfile.html')