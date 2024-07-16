from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUM = 1
END_NUM = 100


def is_even(number_rand):
    return True if number_rand % 2 == 0 else False


def generate_round():
    number_rand = randint(START_NUM, END_NUM)
    expression = f'{number_rand}'
    correct_answer = 'yes' if is_even(number_rand) else 'no'
    return expression, correct_answer
