from django.db import models
from django.urls import reverse

# Create your models here.

class Kniha(models.Model):
    jmeno = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    recenze = models.TextField()

    def __str__(self):
        return self.jmeno

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Knihy"
    