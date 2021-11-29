from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from authen import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('login/', views.Login, name="login"),
    path('register/', views.Register, name="register"),
    path('logout/', views.LogoutUser, name="logout"),
    path('document/', include('document.urls')),
    path('link/', include('link.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
