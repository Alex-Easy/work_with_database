from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=255)
    price = models.FloatField()
    release_date = models.DateField()
    slug = models.SlugField(unique=True)





