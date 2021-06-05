from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Youtuber)
class YoutuberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_featured')
    search_fields = ('id', 'name', 'category')
    list_filter = ('id', 'name', 'price', 'category')