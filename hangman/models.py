from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Game(models.Model):

    user = models.ForeignKey(User)

    word = models.CharField(max_length=64)
    current_guess = models.CharField(max_length=64, blank=True)
    guessed_letters = models.CharField(max_length=26)
    hits = models.IntegerField()
    misses = models.IntegerField()
    win_lose_state = models.NullBooleanField(default=None)

    def __unicode__(self):

        return "{0}'s game of Hangman".format(self.user)