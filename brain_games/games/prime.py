# -*- coding:utf-8 -*-

"""games/prime.py module."""
import math
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

DIV_LOWER_BOUND = 3


def is_prime(number):
    """Check if number is prime."""
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False

    div_upper_bound = math.sqrt(number)

    def inner(div):
        if div >= div_upper_bound:
            return True
        return False if number % div == 0 else inner(div + 2)  # noqa: S001
    return inner(DIV_LOWER_BOUND)


def generate_round_data():
    """generate_round_data."""
    number = randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return (question, answer)
