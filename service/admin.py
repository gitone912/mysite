from django.contrib import admin

# Register your models here.
from service.models import Serve

class Serviceadmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')
    
admin.site.register(Serve,Serviceadmin)