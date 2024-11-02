from django.contrib import admin
from .models import *

# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=('user_id','phone_number','user_name','email','password','is_seller')

class selleradmin(admin.ModelAdmin):
    list_display= ('user_id','business_name','business_location','NID_number','verified')
       
admin.site.register(users, useradmin)
admin.site.register(seller, selleradmin)
