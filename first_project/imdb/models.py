from django.db import models

from django.views import generic

# Create your models here.


class Actor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.CharField(max_length=3)
    about = models.CharField(max_length = 256)

    def __repr__(self):
        return '<Actor {}: {} {} {}>'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.first_name + " " + self.last_name
     

      
class Producer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.CharField(max_length=3)
    about = models.CharField(max_length = 256)

    def __repr__(self):
        return '<Producer {}: {}>'.format(self.first_name, self.last_name)
 
    def __str__(self):
        return self.first_name + " " + self.last_name
      
class Director(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.CharField(max_length=3)
    about = models.CharField(max_length = 256)
    def __repr__(self):
        return '<Director {}: {} {} {}>'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.first_name + " " + self.last_name
     

class Movie(models.Model):
    name = models.CharField(max_length=64)
    rating = models.FloatField(blank=True)
    description = models.CharField(max_length=1000, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)

    def __repr__(self):
        return '<Book {}: {}>'.format(self.name)

    def __str__(self):
        return self.name


 

# Create your models here.
