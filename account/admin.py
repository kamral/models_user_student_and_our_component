from django.contrib import admin

# Register your models here.
from .models import  User

class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email','first_name','second_name',
              'password','last_name','is_active','is_staff',)

admin.site.register(User,UserAdmin)