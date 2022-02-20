from django.contrib import admin
from news.models import News
# Register your models here.

class newsadmin(admin.ModelAdmin):
    list_display=('news_title','news_desc')
    
admin.site.register(News,newsadmin)