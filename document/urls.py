from django.urls import path
from . import  views

urlpatterns = [
    path('cntt/', views.cntt , name='document'),
    path('attt/', views.attt , name="document_ATTT"),
    path('dtvt/', views.dtvt , name="document_DTVT"),
    path('KT/', views.kt , name="document_KT"),
    path('mkt/', views.mkt , name="document_MKT"),
    path('qtkd/', views.qtkd , name="document_QTKD"),
]
