from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from models import Game
import requests

# Create your views here.


def hangman(request):

    data = {}

    if request.user.is_anonymous():

        return render(request, 'hangman/hangman.html')

    if request.method == 'POST':

        game = Game.objects.filter(user=request.user).latest('id')

        letter = request.POST['letter']

        if not letter.isalpha():

            data['game'] = game

            data['message'] = 'Please enter a valid letter.'

            return render(request, 'hangman/hangman.html', data)

        elif letter in game.guessed_letters:

            data['game'] = game

            data['message'] = 'You already guessed that letter!'

            return render(request, 'hangman/hangman.html', data)

        else:

            if letter in game.word:

                game.hits += 1
                game.guessed_letters += letter

                current_guess = ''

                for i in game.word:

                    if i in game.guessed_letters:

                        current_guess += i

                    else:

                        current_guess += '_'

                game.current_guess = current_guess

                if game.current_guess == game.word:

                    game.win_lose_state = True

                    data['message'] = 'You win!'

                game.save()

                data['game'] = game

                return render(request, 'hangman/hangman.html', data)

            else:

                game.misses +=1

                game.guessed_letters += letter

                if game.misses >= 10:

                    game.current_guess = game.word

                    game.win_lose_state = False

                    data['message'] = 'You lose!'

                game.save()

                data['game'] = game

                return render(request, 'hangman/hangman.html', data)


    else:

        r = requests.get('http://randomword.setgetgo.com/get.php')

        word = r.text.strip()

        current_guess = '_'*len(word)

        guessed_letters = ''

        hits = 0

        misses = 0

        user = request.user

        game = Game(word=word, current_guess=current_guess, guessed_letters=guessed_letters,
                    hits=hits, misses=misses, user=user)

        data = {'game': game}

        game.save()

        return render(request, 'hangman/hangman.html', data)


def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            username = request.POST['username']
            password = request.POST['password1']

            user = authenticate(username=username, password=password)

            login(request, user)

            return HttpResponseRedirect('/hangman/')

        else:
            print form.errors

    else:

        form = UserCreationForm()

    content = { 'form': form }

    return render(request, 'hangman/register.html', content)


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
                    return HttpResponseRedirect('/hangman/')
                else:
                    return HttpResponse('Your account is currently disabled.')

        else:
            print form.errors

    else:
        form = AuthenticationForm()

    content = { 'form': form }

    return render(request, 'hangman/login.html', content)

@login_required(login_url='/hangman/login/')
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/hangman/')