from django.db import models

from django.shortcuts import render

# Create your views here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    publisher = models.CharField(max_length=250, blank=True)
    user_favorites = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors

    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=2, blank=True, null=True)
    cast = models.CharField(max_length=250, blank=True)
    plot = models.TextField(blank=True)
    year =  models.IntegerField(max_length=4, blank=True, null=True)
    genre = models.CharField(max_length=100)
    user_favorites = models.ManyToManyField(User, related_name="liked_movies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Director(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    movies = models.ManyToManyField(Movie, related_name="directors")
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Game(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=2, blank=True, null=True)
    cast = models.CharField(max_length=250, blank=True)
    plot = models.TextField(blank=True)
    year =  models.IntegerField(max_length=4, blank=True, null=True)
    director = models.CharField(max_length=100)
    developer = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250, blank=True)
    genre = models.CharField(max_length=100)
    user_favorites = models.ManyToManyField(User, related_name="liked_games")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Developer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    software = models.ManyToManyField(Game, related_name="developers")
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Publisher(models.Model):
    name = models.CharField(max_length=250)
    books = models.ManyToManyField(Book, related_name="publisher")
    games = models.ManyToManyField(Game, related_name="publisher")
    user_favorites = models.ManyToManyField(User, related_name="liked_publisher")
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)