from django.contrib import admin
from .models import LoginUser

# Register your models here.

class LoginUserAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','user_pw')


admin.site.register(LoginUser, LoginUserAdmin)