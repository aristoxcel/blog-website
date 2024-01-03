from django.db import models

# Create your models here.
class Blogging(models.Model):
    blog_title = models.CharField(max_length=100,)
    blog_about = models.CharField(max_length=80,)
    blog_detail = models.CharField(max_length=2000,)
    image = models.ImageField(upload_to='pic/',)


    def __str__(self):
        return self.blog_title