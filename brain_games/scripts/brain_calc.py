#!/usr/bin/env python3
import prompt
from random import randint
import brain_games.scripts.brain_games


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        rand_num_1 = randint(1, 100)
        rand_num_2 = randint(1, 100)
        rand_oper = randint(1, 3)
        match rand_oper:
            case 1:
                print(f'Question: {rand_num_1} + {rand_num_2}')
                correct_answer = rand_num_1 + rand_num_2
            case 2:
                print(f'Question: {rand_num_1} - {rand_num_2}')
                correct_answer = rand_num_1 - rand_num_2
            case 3:
                print(f'Question: {rand_num_1} * {rand_num_2}')
                correct_answer = rand_num_1 * rand_num_2
        answer = prompt.integer('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f'{str(answer)} is wrong answer ;(.'
                  f' Correct answer was {str(correct_answer)}.')
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
