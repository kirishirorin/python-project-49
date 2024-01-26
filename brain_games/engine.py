#!/usr/bin/env python3
import prompt


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    correct_answers = 0
    while correct_answers != 3:
        game.game_round() # Выводится question и corrent_answer
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
    run(game)
