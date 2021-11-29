from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def cntt(request):
    return render(request, 'document.html')

@login_required(login_url='login')
def attt(request):
    return render(request, 'document_ATTT.html')

@login_required(login_url='login')
def dtvt(request):
    return render(request, 'document_DTVT.html')

@login_required(login_url='login')
def mkt(request):
    return render(request, 'document_MKT.html')

@login_required(login_url='login')
def kt(request):
    return render(request, 'document_KT.html')

@login_required(login_url='login')
def qtkd(request):
    return render(request, 'document_QTKD.html')