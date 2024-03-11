from django.db import models


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Service Model
class Dates(models.Model):
    name = models.CharField(max_length=100, verbose_name="Date name")
    description = models.TextField(verbose_name="About date")

    def __str__(self):
        return self.name


# Recent Work Model
class Galerie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Picture description")
    image = models.ImageField(upload_to="picture")

    def __str__(self):
        return self.title


# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
