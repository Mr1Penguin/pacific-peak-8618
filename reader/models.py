from django.db import models

# Create your models here.

class User(models.Model):
    user_email = models.EmailField()
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True)
    def __unicode__ (self):
        return self.user_email

class Site(models.Model):
    url = models.URLField()
    add_date = models.DateTimeField()
    user = models.ForeignKey(User)

class Image(models.Model):
    url = models.URLField()
    site = models.ForeignKey(Site)
    add_date = models.DateTimeField()

#check add date string if none exists
class Collect(models.Model):
    collect_date = models.DateTimeField()
