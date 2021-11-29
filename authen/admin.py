from django.contrib import admin
from .models import userProfile
# Register your models here.
class UserProfileInline(admin.ModelAdmin):
   list_display=['avatar' , 'user' ]
   search_fields=['user']

admin.site.register(userProfile, UserProfileInline)