from django.db import models

# Create your models here.

class Poster(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    image = models.ImageField(upload_to='page/', verbose_name="صورة البوستر")
    description = models.TextField(verbose_name="الوصف الطبي")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class x(models.Model):
    name=models.CharField(max_length=22)
    

class StaticPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # هنا سنضع كود الـ HTML

