from django.db import models

# Create your models here.
class Hydjobs(models.Model):

    date = models.DateField()
    company = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    eligibility = models.CharField(max_length=264)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.company

class Chennaijobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    eligibility = models.CharField(max_length=264)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.company


class Punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    eligibility = models.CharField(max_length=264)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.company


class Blrjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    eligibility = models.CharField(max_length=264)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.company
