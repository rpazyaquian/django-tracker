from django.shortcuts import render
from models import Section, Header

# Create your views here.


def resume(request):

    header = Header.objects.get(pk=1)

    sections = Section.objects.select_related('entries', 'entries__details')

    content = {'header': header, 'sections': sections}

    return render(request, 'resume/resume.html', content)