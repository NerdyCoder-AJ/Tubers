from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    fb_link = models.CharField(max_length=200)
    insta_link = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    cerated_date = DateTimeField(auto_now_add=True)


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%y/')
    created_date = models.DateTimeField(auto_now_add=True)
