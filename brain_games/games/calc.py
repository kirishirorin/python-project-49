import random


QUESTION = 'What is the result of the expression?'
START_NUM = 1
END_NUM = 100


def generate_round():
    rand_num_1 = random.randint(START_NUM, END_NUM)
    rand_num_2 = random.randint(START_NUM, END_NUM)
    operator = random.choice(['+', '-', '*'])
    expression = f'{rand_num_1} {operator} {rand_num_2}'
    if operator == '+':
        correct_answer = rand_num_1 + rand_num_2
    elif operator == '-':
        correct_answer = rand_num_1 - rand_num_2
    elif operator == '*':
        correct_answer = rand_num_1 * rand_num_2
    return expression, str(correct_answer)
