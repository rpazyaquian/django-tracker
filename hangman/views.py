from django.shortcuts import render
from models import Game

# Create your views here.


def hangman(request):

    if request.method == 'POST':

        game = Game.objects.filter(user=request.user).latest('id')



        if request['letter'] in game.guessed_letters:

            data = {'game': game, 'message': 'You already guessed that letter!'}

            return render(request, 'hangman/hangman.html', data)

        else:

            if request['letter'] in game.word:

                game.hits += 1

                for i in range(len(game.word)):

                    if request['letter'] == game.word[i]:

                        game.current_guess[i] = request['letter']

                game.guessed_letters += request['letter']

                if game.current_guess == game.word:

                    game.win_lose_state = True

            else:

                game.misses +=1

                game.guessed_letters += request['letter']

                if game.misses >= 10:

                    game.win_lose_state = False


    else:

        word = 'apple'

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