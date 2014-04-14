from django.db import models

# Create your models here.


class GuestbookEntry(models.Model):

    name = models.CharField(max_length=60)

    comment = models.CharField(max_length=140)

    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):

        return "{0}".format(self.comment)