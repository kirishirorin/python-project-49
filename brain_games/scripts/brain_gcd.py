#!/usr/bin/env python3
import prompt
from random import randint

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers < 3:
        rand_num_1 = randint(1, 100)
        rand_num_2 = randint(1, 100)
        print(f'Question: {rand_num_1} {rand_num_2}')
        answer = prompt.integer('Your answer: ')
        correct_answer = 0
        for i in range(max(rand_num_1, rand_num_2), 0, -1):
            if (rand_num_1 % i == 0) and (rand_num_2 % i == 0):
                correct_answer = i
                break
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f'{str(answer)} is wrong answer ;(. Correct answer was {str(correct_answer)}.')
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")



if __name__ == '__main__':
    main()
