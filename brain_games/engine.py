import prompt


def run(game):
    start_expression = "Question"
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    correct_answers = 0
    max_count_correct_answers = 3
    for i in range(0, 4):
        correct_answers = i
        if correct_answers == max_count_correct_answers:
            print(f"Congratulations, {name}!")
            break
        expression, correct_answer = game.generate_round(start_expression)
        print(expression)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break
