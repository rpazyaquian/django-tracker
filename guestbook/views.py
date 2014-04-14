from django.shortcuts import render, HttpResponseRedirect
from models import GuestbookEntry
from forms import GuestbookEntryForm

# Create your views here.


def guestbook(request):

    if request.method == 'POST':

        entry = GuestbookEntry()

        form = GuestbookEntryForm(request.POST, instance=entry)

        if form.is_valid():

            form.save(commit=True)

            return HttpResponseRedirect('/guestbook')

        else:

            print form.errors

    else:

        form = GuestbookEntryForm()

    comments = GuestbookEntry.objects.order_by('-created_date')

    content = {'comments': comments, 'form': form}

    return render(request, 'guestbook/guestbook.html', content)