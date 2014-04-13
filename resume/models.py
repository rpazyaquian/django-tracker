from django.db import models

# Create your models here.


#{% for section in sections.all %} {{ section.title }} {% for entry in section.entry_set.all %} {{ entry.title }} {% for detail in entry.detail_set.all %} {{ detail }} {% endfor %} {% endfor %} {% endfor %}

class Header(models.Model):

    name = models.CharField(max_length=36)

    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()

    github = models.URLField()

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Section(models.Model):

    title = models.CharField(max_length=36)

    def __unicode__(self):
        return u'{0}'.format(self.title)


class Entry(models.Model):

    section = models.ForeignKey(Section, related_name='entries')

    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True)

    url = models.URLField(blank=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.section, self.title)


class Detail (models.Model):

    entry = models.ForeignKey(Entry, related_name='details')

    content = models.CharField(max_length=256)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.entry, self.content)