from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    qtty = models.FloatField(max_length=100)
    units = models.CharField(max_length=50)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.qtty} {self.units} of {self.name}"

class Cookie(models.Model):
    name = models.CharField(max_length=100)
    main_flavor = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    prep_time = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cookie_id': self.id})
    
    def done_for_today(self):
        return self.batch_set.filter(date=date.today()).count() >= len(TIMES)

class Batch(models.Model):
    date = models.DateField('Batch Date')
    time = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0])

    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']