#!/usr/bin/env python3
from random import randint


def game_round():
    #print('What is the result of the expression?'
    rand_num_1 = randint(1, 100)
    rand_num_2 = randint(1, 100)
    rand_oper = randint(1, 3)
    match rand_oper:
        case 1:
            print(f'Question: {rand_num_1} + {rand_num_2}')
            correct_answer = rand_num_1 + rand_num_2
            return correct_answer
        case 2:
            print(f'Question: {rand_num_1} - {rand_num_2}')
            correct_answer = rand_num_1 - rand_num_2
            return correct_answer
        case 3:
            print(f'Question: {rand_num_1} * {rand_num_2}')
            correct_answer = rand_num_1 * rand_num_2
            return correct_answer


if __name__ == '__main__':
    game_round()
