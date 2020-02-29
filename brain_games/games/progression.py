# -*- coding:utf-8 -*-

"""games/progression.py module."""
from random import randint

DESCRIPTION = 'What number is missing in the progression?'

LENGTH = 10


def generate_question(first_element, step, position):
    """generate_question."""
    question = ''
    for index in range(LENGTH):
        element = '..' if index == position else first_element + step * index
        question = '{p} {el}'.format(p=question, el=element)
    return question.strip()


def generate_round_data():
    """generate_round_data."""
    first_element = randint(-10, 10)
    hidden_element_position = randint(0, LENGTH - 1)
    step = randint(-10, 10)
    question = generate_question(
        first_element, step, hidden_element_position,
    )
    answer = str(first_element + step * hidden_element_position)
    return (question, answer)
