from django.db import models


class Tables(models.Model):
    name = models.CharField(max_length=100,unique = True)

    def __str__(self):
        return self.name

class Legs(models.Model):
    tables = models.ForeignKey(Tables,on_delete = models.CASCADE)

class Feet(models.Model):
    length = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    radius = models.IntegerField(null=True, blank=True)
    legs = models.ManyToManyField(Legs)