from django.db import models

class Level(models.Model):
    name=models.CharField('Название',max_length=100)
    description=models.CharField("Описание", max_length=250)
    level=models.IntegerField(max_length=10)
    img=models.ImageField(upload_to="img/")
    imgClean = models.ImageField(upload_to="imgClean/")

