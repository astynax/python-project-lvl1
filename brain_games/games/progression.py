# -*- coding:utf-8 -*-

"""games/progression.py module."""
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(length, first_element, step, position):
    """generate_progression."""
    progression = ''
    for index in range(length):
        element = '..' if index == position else first_element + step * index
        progression = '{p} {el}'.format(p=progression, el=element)

    return progression.strip()


def generate_round_data():
    """generate_round_data."""
    length = 10
    first_element = randint(-10, 10)
    hidden_element_position = randint(0, length - 1)
    step = randint(-10, 10)
    question = generate_progression(length, first_element, step, hidden_element_position)
    answer = str(first_element + step * hidden_element_position)
    return (question, answer)
