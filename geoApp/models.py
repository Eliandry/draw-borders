from django.db import models
from PIL import Image

class Level(models.Model):
    name=models.CharField('Название',max_length=100)
    description=models.CharField("Описание", max_length=250)
    level=models.IntegerField(max_length=10)
    img=models.ImageField(upload_to="img/")
    imgClean = models.ImageField(upload_to="imgClean/")

    def save(self, *args, **kwargs):
        super().save()  # saving image first

        img = Image.open(self.img.path)  # Open image using self
        new_img = (1900, 1000)
        img.thumbnail(new_img)
        img.save(self.img.path)
        imgClean = Image.open(self.imgClean.path)  # Open image using self
        new_img = (1900, 1000)
        imgClean.thumbnail(new_img)
        imgClean.save(self.img.path)