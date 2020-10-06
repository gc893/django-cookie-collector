from django.db import models

# Create your models here.

class Cookie(models.Model):
    name = models.CharField(max_length=100)
    main_flavor = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    prep_time = models.IntegerField()

    def __str__(self):
        return self.name