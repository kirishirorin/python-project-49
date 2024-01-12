#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    global name
    welcome_user()


def check_answer(name, answer, correct_answer, correct_answers, point):
    if answer == correct_answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f'{str(answer)} is wrong answer ;(. Correct answer was {str(correct_answer)}.')
        print(f"Let's try again, {name}!")
        point += 1


if __name__ == '__main__':
    main()
