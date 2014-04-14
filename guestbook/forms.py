__author__ = 'rebecca'

from django import forms
from models import GuestbookEntry


class GuestbookEntryForm(forms.ModelForm):

    class Meta:

        model = GuestbookEntry

        fields = ('name', 'comment')