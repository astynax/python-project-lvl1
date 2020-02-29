# -*- coding:utf-8 -*-

"""engine.py module."""
import prompt

NUMBER_OF_ROUNDS = 3


def engine(game):  # noqa: WPS213
    """engine."""
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    print()

    for _ in range(NUMBER_OF_ROUNDS):
        question, answer = game.generate_round_data()
        print('Question: {question}'.format(question=question))
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(
                "Answer '{wrong}' is wrong answer ;(. "
                "Correct answer was '{correct}'.".format(  # noqa: WPS326
                    wrong=user_answer,
                    correct=answer,
                ),
                 )
            print("Let's try again, {name}!".format(name=name))
            break
        print('Correct!')
    else:
        print('Congratulations, {name}!'.format(name=name))
