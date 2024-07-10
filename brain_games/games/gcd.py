from random import randint
import math


QUESTION = 'Find the greatest common divisor of given numbers.'
START_NUM = 1
END_NUM = 100

def generate_round(start_expression):
    rand_num_1 = randint(START_NUM, END_NUM)
    rand_num_2 = randint(START_NUM, END_NUM)
    expression = f'{start_expression}: {rand_num_1} {rand_num_2}'
    correct_answer = str(math.gcd(rand_num_1, rand_num_2))
    return expression, correct_answer
