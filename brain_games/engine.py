import prompt


COUNT_ROUNDS = 3
START_WORD = "Question"


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    correct_answers = 0
    for i in range(0, COUNT_ROUNDS):
        expression, correct_answer = game.generate_round()
        print(f'{START_WORD}: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
