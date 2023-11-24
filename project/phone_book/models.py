from django.db import models


class Record(models.Model):
    family = models.ForeignKey('Family', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    otchestvo = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30, blank=True)
    house = models.CharField(max_length=10, blank=True)
    korp = models.CharField(max_length=10, blank=True)
    apartments = models.IntegerField(null=True, blank=True)
    mob = models.CharField(max_length=25)


class Family(models.Model):
    value = models.CharField(max_length=30)

    def __str__(self):
        return self.value
