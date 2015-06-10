__author__ = 'willflowers'

from django.db import models

# Create your models here.
class Rater(models.Model):
    gender = models.CharField(max_length=7)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zipcode = models.CharField(max_length=12)

    def all_movies(self):
        return self.movie_set.all()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def all_ratings(self):
        return self.rating_set.all()

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating_value = models.IntegerField()
