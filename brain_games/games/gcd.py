# -*- coding:utf-8 -*-

"""games/gcd.py module."""
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):  # noqa: WPS111
    """gcd."""
    return abs(y) if x % y == 0 else gcd(y, x % y)  # noqa: S001, WPS221


def generate_round_data():
    """generate_round_data."""
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = '{x} {y}'.format(x=first_num, y=second_num)
    answer = str(gcd(first_num, second_num))
    return (question, answer)
