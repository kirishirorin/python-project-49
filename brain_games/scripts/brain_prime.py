#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        rand_num_1 = randint(1, 100)
        list_num = []
        for i in range(1, rand_num_1 + 1):
            if rand_num_1 % i == 0:
                list_num.append(i)
        if len(list_num) == 2:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {rand_num_1}')
        answer = prompt.string("Your answer: ")
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
