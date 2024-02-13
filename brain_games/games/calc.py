from random import choice


QUESTION = 'What is the result of the expression?'


def game_round():
    rand_num_1 = randint(1, 100)
    rand_num_2 = randint(1, 100)
    operator = choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    correct_answer = correct_answer = str(eval(expression))
    return expression, str(correct_answer)
