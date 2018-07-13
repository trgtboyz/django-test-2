from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    vchr_name = models.CharField(max_length = 100)
    vchr_email = models.CharField(max_length = 100)
    txt_content = models.TextField()
