from django.contrib import admin
from .models import UserDetails

#Register your models here.
@admin.register(UserDetails)
class UserDeatilsAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','passw']
    list_editable = ['name','email','passw']

# admin.site.register(UserDetails, UserDeatilsAdmin)