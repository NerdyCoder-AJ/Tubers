from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.
# admin.site.register(Slider)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'subtitle','photo', 'created_date')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def TeamPhoto(self, object):
        return format_html('<img src="{} "width="40">'.format(object.photo.url))

    list_display = ('id', 'TeamPhoto', 'first_name', 'role', 'cerated_date')
    search_fields = ('id', 'first_name', 'role',)
    list_filter = ('role',)
    