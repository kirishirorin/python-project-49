from random import randint


QUESTION = 'What is the result of the expression?'

def game_round():
    rand_num_1 = randint(1, 100)
    rand_num_2 = randint(1, 100)
    rand_oper = randint(1, 3)
    match rand_oper:
        case 1:
            expression = f'Question: {rand_num_1} + {rand_num_2}'
            correct_answer = rand_num_1 + rand_num_2
            return expression, correct_answer
        case 2:
            expression = f'Question: {rand_num_1} - {rand_num_2}'
            correct_answer = rand_num_1 - rand_num_2
            return expression, correct_answer
        case 3:
            expression = f'Question: {rand_num_1} * {rand_num_2}'
            correct_answer = rand_num_1 * rand_num_2
            return expression, correct_answer
