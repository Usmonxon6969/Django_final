from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    address = models.TextField()
    phone = models.CharField(max_length=20)
    paragraph = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Banner(models.Model):
    image = models.ImageField()
    tag = models.CharField(max_length=250)
    head = models.CharField(max_length=250)
    paragraph = models.CharField(max_length=250)

    def __str__(self):

        return self.tag


class Service(models.Model):
    name = models.CharField(max_length=250)
    paragraph = models.CharField(max_length=250)
    icon = models.ImageField()


class Worker(models.Model):
    image = models.ImageField()
    full_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    facebook = models.CharField(max_length=255)
    twinter = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)


class About(models.Model):
    title = models.CharField(max_length=250)
    paragraph = models.CharField(max_length=250)
