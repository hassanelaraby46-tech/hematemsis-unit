from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poster(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    image = models.ImageField(upload_to='page/', verbose_name="صورة البوستر")
    description = models.TextField(verbose_name="الوصف الطبي")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class StaticPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # هنا سنضع كود الـ HTML



class GaharChecklist(models.Model):
    department = models.CharField(max_length=100, verbose_name="القسم")
    date = models.DateField(auto_now_add=True, verbose_name="تاريخ المراجعة")
    inspector = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المراجع")
    
    # بنود المعايير
    patient_id_verified = models.BooleanField(default=False, verbose_name="التأكد من هوية المريض")
    policies_updated = models.BooleanField(default=False, verbose_name="السياسات محدثة")
    hand_hygiene_followed = models.BooleanField(default=False, verbose_name="الالتزام بغسل الأيدي")
    waste_segregation_correct = models.BooleanField(default=False, verbose_name="فصل النفايات صحيح")
    
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات إضافية")

    def __str__(self):
        return f"{self.department} - {self.date}"