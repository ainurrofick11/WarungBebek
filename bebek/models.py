from django.db import models

# Create your models here.
class Menu(models.Model):
    nama_menu = models.CharField(max_length=255)
    harga = models.IntegerField()

    def __str__(self):
        return self.nama_menu
