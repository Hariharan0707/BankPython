from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name



class District(models.Model):
    districtname = models.CharField(max_length=100)

    def __str__(self):
        return self.districtname


class Branch(models.Model):
    distid = models.ForeignKey(District, on_delete=CASCADE)
    branchname = models.CharField(max_length=100)

    def __str__(self):
        return self.branchname


class Service(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name