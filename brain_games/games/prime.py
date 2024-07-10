from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUM = 1
END_NUM = 100


def is_prime(rand_num_1):
    list_num = []
    for i in range(1, rand_num_1 + 1):
        if rand_num_1 % i == 0:
            list_num.append(i)
    if len(list_num) == 2:
        return 'yes'
    else:
        return 'no'


def generate_round(start_expression):
    rand_num_1 = randint(START_NUM, END_NUM)
    expression = f'{start_expression}: {rand_num_1}'
    correct_answer = is_prime(rand_num_1)
    return expression, correct_answer
