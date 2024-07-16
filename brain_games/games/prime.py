from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUM = 1
END_NUM = 100


def is_prime(rand_num_1):
    for i in range(2, rand_num_1):
        if rand_num_1 % i == 0:
            return False
    return True


def generate_round():
    rand_num_1 = randint(START_NUM, END_NUM)
    expression = f'{rand_num_1}'
    correct_answer = 'yes' if is_prime(rand_num_1) else 'no'
    return expression, correct_answer
