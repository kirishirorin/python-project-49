from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUM = 1
END_NUM = 100


def is_even(number_rand):
    return 'yes' if number_rand % 2 == 0 else 'no'


def generate_round(start_expression):
    number_rand = randint(START_NUM, END_NUM)
    expression = f'{start_expression}: {number_rand}'
    correct_answer = is_even(number_rand)
    return expression, correct_answer
