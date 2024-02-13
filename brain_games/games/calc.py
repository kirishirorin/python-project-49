import random


QUESTION = 'What is the result of the expression?'


def game_round():
    rand_num_1 = random.randint(1, 100)
    rand_num_2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f'{rand_num_1} {operator} {rand_num_2}'
    correct_answer = str(eval(expression))
    return expression, str(correct_answer)
