from django.db import models

# Create your models here.

class UploadFileForm(models.Model):
    title = models.CharField(max_length=50),
    file = models.FileField()