from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def game_round():
    rand_num_1 = randint(1, 100)
    list_num = []
    expression = f'Question: {rand_num_1}'
    for i in range(1, rand_num_1 + 1):
        if rand_num_1 % i == 0:
            list_num.append(i)
    if len(list_num) == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer
