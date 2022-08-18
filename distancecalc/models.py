from django.db import models
import pandas as pd


# Create your models here.
class Ports(models.Model):
    starting_point = models.CharField(max_length=100)
    ending_point = models.CharField(max_length=100)
    speed = models.DecimalField(decimal_places=1, max_digits=3)


class Post(models.Model):
    title= models.CharField(max_length=300)
    slug= models.SlugField(max_length=300, unique=True, blank=True)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)


    def __str__(self):
        return self.title