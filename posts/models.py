from django.db import models

# Create your models here.
from django.urls import reverse


class Post_table(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    image= models.ImageField(null=True,blank=True,upload_to='pics',default='pics/about.jpg')
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])







