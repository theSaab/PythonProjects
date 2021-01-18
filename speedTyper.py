

# this program judges you based on your typing skills
# there seems to be a problem with the api call, the website is down maybe

import requests
import time

def intro():

    name = input('Hello traveler. What is your name? ')
    print('I have been waiting to judge a mortal soul.')
    print('You will be judged on your typing skills, ', name)
    print('Type the sentence as fast as possible')


def accuracy(sentence, input):

    characters = len(sentence)
    mistakes = 0

    for i in range(len(input)):
        if input[i] != sentence[i + mistakes]:
            mistakes += 1

    accuracy = (characters - mistakes)/characters*100
    return accuracy


def sentence():

    ready = input('Are you ready? Yes or no? The timer will start when you say yes. ')
    ready = ready.upper()

    if ready == 'YES':
        r = requests.get('https://quote-garden.herokuapp.com/api/v2/quotes/random')
        piece = r.json()
        phrase = str(piece['quote']['quoteText'])

        time_start = time.time()
        typer = input(phrase + '\n \n')

        if typer == phrase:
            response = 'Good job.'  

        else:
            response = 'You made a mistake, this is a failure.'            

        time_finish = time.time()
        time_taken = time_finish - time_start
        similarity = str(accuracy(phrase, typer))


        print('You typed at', str(len(typer)//time_taken), 'characters a second.')
        print('With an accuracy of', similarity + '%.')
        print('You took', str(time_taken//1.0), 'seconds.', response)

    else:
        print('Ok, goodbye.')

sentence()