from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import Application
from forms import ApplicationForm


# Create your views here.


def index(request):

    return render(request, 'tracker/index.html')


def apps(request, username):

    user = User.objects.get(username=username)

    if request.user == user:

        application_list = Application.objects.filter(user=user).order_by('title')

        past_applications = len(Application.objects.filter(user=user).filter(submitted_date__gte=datetime.today()-timedelta(days=30)))

        content = { 'applications': application_list, 'past_apps': past_applications, 'username': username }

        return render(request, 'tracker/apps.html', content)

    else:

        return HttpResponseRedirect('/tracker/')


@login_required(login_url='/tracker/login/')
def addapp(request):

    if request.method == 'POST':

        app = Application(user=request.user)

        form = ApplicationForm(request.POST, instance=app)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect('/tracker/user/{0}/'.format(request.user.username))

        else:
            print form.errors

    else:

        form = ApplicationForm()

    content = { 'form': form }

    return render(request, 'tracker/addapp.html', content)


def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(username=username, password=password)

            login(request, user)

            return HttpResponseRedirect('/tracker/')

        else:
            print form.errors

    else:

        form = UserCreationForm()

    content = { 'form': form }

    return render(request, 'tracker/register.html', content)


def user_login(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/tracker/')
                else:
                    return HttpResponse('Your account is currently disabled.')

        else:
            print form.errors

    else:
        form = AuthenticationForm()

    content = { 'form': form }

    return render(request, 'tracker/login.html', content)


@login_required(login_url='/tracker/login/')
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/tracker/')


@login_required(login_url='/tracker/login/')
def delete(request, app_id):
    if request.method == 'POST':
        user = request.user

        app = Application.objects.get(pk=app_id)

        if app.user == user:

            app.delete()

            return HttpResponseRedirect('/tracker/user/{0}/'.format(user.username))

        else:

            return HttpResponse('User mismatch, application not deleted.')

    else:
        return HttpResponseRedirect('/tracker/')


@login_required(login_url='/tracker/login/')
def edit(request, app_id):

    user = request.user
    app = Application.objects.get(pk=app_id)

    if app.user == user:

        form = ApplicationForm(request.POST or None, instance=app)

        if request.method == 'POST':

            if form.is_valid():

                obj = form.save(commit=False)

                obj.save()

                return HttpResponseRedirect('/tracker/user/{0}/'.format(user.username))

            else:

                print form.errors

        else:

            form = ApplicationForm(instance=app)

    else:
        return HttpResponse('User mismatch, permission denied.')

    content = { 'form': form, 'app': app }

    return render(request, 'tracker/edit.html', content)