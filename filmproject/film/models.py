
from django.db import models

#Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')
    actors=models.CharField(max_length=250,blank=True)
    release_date=models.DateField()
    category=models.CharField(max_length=250)

    def __str__(self):
        return self.name