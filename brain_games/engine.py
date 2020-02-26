# -*- coding:utf-8 -*-

"""engine.py module."""
import prompt

NUMBER_OF_ROUNDS = 3


def engine(description, get_round_data):
    """engine."""
    print('Welcome to the Brain Games!')
    print(description)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    print()

    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = get_round_data()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(
                "Answer '{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
                    .format(wrong=user_answer, correct=answer),
                 )
            print("Let's try again, {0}!".format(name))
            return

    print('Congratulations, {0}!'.format(name))
