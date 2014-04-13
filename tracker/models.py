from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Application(models.Model):

    user = models.ForeignKey(User)

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=140)
    company = models.CharField(max_length=64)
    submitted_date = models.DateField(default=date.today())

    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)


class Interview(models.Model):

    app = models.ForeignKey(Application)

    scheduled_datetime = models.DateTimeField()

    contact_number = models.CharField(max_length=24, blank=True)
    contact_name = models.CharField(max_length = 32, blank=True)
    contact_email = models.EmailField(blank=True)

    thankyou_note_yesno = models.BooleanField()

    notes = models.TextField(max_length=256, blank=True)

    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):

        return u'Interview with {0} on {1}'.format(self.contact_name, self.scheduled_datetime)