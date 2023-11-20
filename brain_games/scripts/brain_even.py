#!/usr/bin/env python3
import prompt
from random import randint
import brain_games.scripts.brain_games


def main():
    brain_games.scripts.brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number_rand = randint(1, 100)
        print(f'Question: {number_rand}')
        answer = prompt.string('Your answer: ')
        if (number_rand % 2 == 0) and (answer == 'yes'):
            print("Correct!")
            correct_answers += 1
        elif (number_rand % 2 != 0) and (answer == 'no'):
            print("Correct!")
            correct_answers += 1
        else:
            if answer == 'yes' or answer == 'no':
                if answer == 'yes':
                    correct_answer = 'no'
                else:
                    correct_answer = 'yes'
            else:
                if number_rand % 2 == 0:
                    correct_answer = 'yes'
                else:
                    correct_answer = 'no'
            print(f'{answer} is wrong answer;(.'
                  f' Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
