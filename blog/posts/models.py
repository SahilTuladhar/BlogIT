from django.db import models

# Create your models here.

class Blog(models.Model):
 title = models.CharField(max_length=100)
 category = models.CharField(max_length=80)
 description = models.TextField(max_length=1000)
 blog_image = models.ImageField(blank = 'true' , default= 'default.png' , upload_to='images/')


