# -*- coding:utf-8 -*-

"""games/prime.py module."""
import math
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def inner(div, number, div_upper_bound):
    """inner."""
    if div >= div_upper_bound:
        return True
    if number % div == 0:  # noqa: S001
        return False
    return inner(div + 2, number, div_upper_bound)


def is_prime(number):
    """Check if number is prime."""
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False

    div_lower_bound = 3
    div_upper_bound = math.sqrt(number)
    return inner(div_lower_bound, number, div_upper_bound)


def generate_round_data():
    """generate_round_data."""
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return (question, answer)
