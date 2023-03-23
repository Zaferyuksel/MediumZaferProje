from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Makale Başlık"), max_length=50)
    subject = models.CharField(("Makale Konu"), max_length=50, null=True)
    text = models.TextField(("Makale"))
    image = models.FileField(("Makale Görsel"), upload_to="", max_length=100)
    date_now = models.DateField(("Tarih"), auto_now_add=True)
    user_img = models.FileField(("User Foto"), upload_to=None, max_length=100)
    read_time = models.SmallIntegerField(("Okuma Süresi"),default=0, null=True)
    

    def __str__(self):
        return self.title