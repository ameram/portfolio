from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='image/')
    summry = models.CharField(max_length=200)