from django.contrib import admin

# Register your models here.
from contactus.models import contactnow

class coni(admin.ModelAdmin):
    list_display=('name','email','des')
admin.site.register(contactnow,coni)