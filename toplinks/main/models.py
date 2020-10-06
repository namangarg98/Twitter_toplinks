from django.db import models

# Create your models here.


class Tweet(models.Model):
    actual_tweet = models.CharField(max_length=200)
