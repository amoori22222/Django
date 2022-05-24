from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=1000)
    service_name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

class Project(models.Model):
    image = models.CharField(max_length=1000)
    service = models.CharField(max_length=500)
    title = models.CharField(max_length=50)

class Contact(models.Model):
    icon = models.CharField(max_length=1000)
    method = models.CharField(max_length=50)
    info = models.CharField(max_length=100)

