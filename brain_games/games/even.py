from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def game_round():
    number_rand = randint(1, 100)
    expression = f'Question: {number_rand}'
    correct_answer = 'yes' if number_rand % 2 == 0 else 'no'
    return expression, correct_answer
