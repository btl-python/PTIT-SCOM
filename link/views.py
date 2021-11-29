from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def link(request):
    return render(request, 'link.html')

@login_required(login_url='login')
def link_club(request):
    return render(request, 'link_club.html')
    
@login_required(login_url='login')
def link_page(request):
    return render(request, 'link_page.html')