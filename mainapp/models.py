from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models

class Bean(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return (self.name)

class Roast(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return (self.name)


class Syrup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return (self.name)

class Powder(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return (self.name)


class Coffee(models.Model):
    user=models.ForeignKey(User)
    name = models.CharField(max_length=200)
    bean = models.ForeignKey(Bean)
    roast = models.ForeignKey(Roast)
    syrup = models.ManyToManyField(Syrup,blank=True)
    powder = models.ManyToManyField(Powder, blank=True)
    espresso_shots=models.PositiveIntegerField(default=1)
    water=models.FloatField(default=0)
    steamed_milk=models.BooleanField(default=False)
    foam=models.FloatField(default=0)
    extra_instructions=models.TextField()
    def __str__(self):
        return (self.name)