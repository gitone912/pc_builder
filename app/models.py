from django.db import models

# Create your models here.
class processor(models.Model):
    processor_name = models.CharField(max_length=200 , null=False)
    processor_brand = models.CharField(max_length=200)
    processor_model = models.CharField(max_length=200)
    processor_speed = models.CharField(max_length=200)
    processor_cores = models.CharField(max_length=200)
    processor_socket_type = models.CharField(max_length=200)
    processor_image_url = models.CharField( max_length=200)
    processor_image_alt = models.CharField(max_length=200)
