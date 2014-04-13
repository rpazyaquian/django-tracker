__author__ = 'rebecca'

from django import forms
from models import Application, Interview


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('title', 'description', 'company', 'submitted_date')


class InterviewForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = ('scheduled_datetime', 'contact_name', 'contact_number', 'contact_email', 'thankyou_note_yesno',
                  'notes')