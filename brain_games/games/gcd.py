from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'


def game_round():
    rand_num_1 = randint(1, 100)
    rand_num_2 = randint(1, 100)
    expression = f'Question: {rand_num_1} {rand_num_2}'
    for i in range(max(rand_num_1, rand_num_2), 0, -1):
        if (rand_num_1 % i == 0) and (rand_num_2 % i == 0):
            correct_answer = str(i)
            break
    return expression, correct_answer
