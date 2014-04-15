from django.shortcuts import render
from models import Game
import requests

# Create your views here.


def hangman(request):

    data = {}

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