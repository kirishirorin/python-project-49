import random


QUESTION = 'What is the result of the expression?'


def game_round():
    rand_num_1 = random.randint(1, 100)
    rand_num_2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f'Question: {rand_num_1} {operator} {rand_num_2}'
    correct_answer = str(eval(f'{rand_num_1} {operator} {rand_num_2}'))
    return expression, str(correct_answer)
