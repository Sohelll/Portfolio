from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    progress_percent = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    site = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Photo(models.Model):
    photo_name = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo_name
    

