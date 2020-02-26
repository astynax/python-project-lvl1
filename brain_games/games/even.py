# -*- coding:utf-8 -*-

"""brain_games/even.py module."""
from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    """is_even."""
    return number % 2 == 0


def generate_round_data():
    """generate_round_data."""
    question = randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return (question, answer)
