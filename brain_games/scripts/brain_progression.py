#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    correct_answers = 0
    while correct_answers < 3:
        rand_num_1 = randint(1, 100)
        rand_defferent = randint(1, 100)
        rand_len = randint(5, 10)
        rand_place = randint(0, rand_len - 1)
        progres = []
        range_2_param = rand_num_1 + 10 * rand_defferent
        progres.append(rand_num_1)
        for i in range(rand_num_1, range_2_param, rand_defferent):
            progres.append(i + rand_defferent)
        correct_answer = progres[rand_place]
        progres[rand_place] = '..'
        progres = progres[0:rand_len]
        progres_str = ''
        for i in progres:
            progres_str += str(i) + ' '
        print('Question: ' + progres_str.strip())
        answer = prompt.integer("Your answer: ")
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
