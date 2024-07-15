from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)





