from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name
