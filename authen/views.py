from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authen.models import userProfile
# Create your views here.
from . import form
def index(request):
    return render(request, 'login.html')

# @login_required(login_url='login')
# def profile(request):
#     return render(request, 'profile.html')
#ham dang ky
def Register(request):
    if request.method =='POST':
        user_name=None
        email=None
        pass_word1=None
        pass_word2=None
        if "user_digit" in request.POST:
            user_name = request.POST['user_digit']
            #kiem tra username da ton tai hay chua
            if User.objects.filter(username=user_name).exists():
                return render(request, 'register.html',{"loi":"Tên người dùng đã tồn tại!"})
        if "email_digit" in request.POST:
            email = request.POST['email_digit']
            #kiem tra email da ton tai hay chua
            if User.objects.filter(email=email).exists():
                return render(request, 'register.html',{"loi":"Email đã tồn tại!"})
            if "@gmail.com" not in email:
                return render(request, 'register.html',{"loi":"Email không đúng định dạng!"})
        if "pass1_digit" in request.POST:
            pass_word1 = request.POST['pass1_digit']
            #kiem tra do dai mat khau
            if len(pass_word1)<8:
                return render(request, 'register.html',{"loi":"Mật khẩu cần 8 ký tự trở lên!"})
        if "pass2_digit" in request.POST:
            pass_word2 = request.POST['pass2_digit']
        if pass_word1==pass_word2  :
            #kiem tra xac nhan mat khau co dung hay khong
            user = User.objects.create_user(user_name, email, pass_word1)
            u=userProfile.objects.create(user=user,)
            u.avatar='/user.jpg'
            u.save()
            return redirect('login')
        else:
            return render(request,'register.html',{"loi":"Xác nhận mật khẩu không chính xác!"})
        
    return render(request,'register.html',{"loi":""})

#ham dang nhap
def Login(request, id=None):
    if id!=None:
        return redirect('home')
    loi=""
    if request.method =='POST':
        user_name=None
        pass_word=None
        if "username" in request.POST:
            user_name = request.POST['username']
        if "password" in request.POST:
            pass_word = request.POST['password']
        user=authenticate(request,username= user_name,password= pass_word)
        if user is not  None:
            login(request,user)
            return redirect('home')
        else:
            loi+="Sai thông tin đăng nhâp!"
    
    return render(request,'login.html', {'loi':loi})
#ham dang xuat
@login_required(login_url='login')
def LogoutUser(request):
	logout(request)
	return redirect('login')