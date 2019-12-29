from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Name", max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = 'Actors'


class Genre(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField("Title", max_length=100)
    tagline = models.CharField("Tag Line", max_length=100, default=' ')
    description = models.TextField()
    poster = models.ImageField("Poster", upload_to="poster/")
    year = models.PositiveSmallIntegerField("Year", default=2019)
    country = models.CharField("Country", max_length=40)
    directors = models.ManyToManyField(Actor, verbose_name="Director", related_name='file_director')
    actors = models.ManyToManyField(Actor, verbose_name="Actors", related_name="file_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    world_premiere = models.DateField("Premier world", default=date.today)
    budget = models.PositiveSmallIntegerField("Budget", default=0, help_text="Enter sum in dollars")
    fees_in_usa = models.PositiveSmallIntegerField("Fees in USA", default=0)
    fees_in_world = models.PositiveSmallIntegerField("Fees in World", default=0)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField()
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Frame from movie"
        verbose_name_plural = "Frames from movie"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rating star"
        verbose_name_plural = "Rating stars"


class Rating(models.Model):
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Rating"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"





