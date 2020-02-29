# -*- coding:utf-8 -*-

"""games/gcd.py module."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    """gcd."""
    return num2 if num1 % num2 == 0 else gcd(num2, num1 % num2)


def generate_round_data():
    """generate_round_data."""
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = '{x} {y}'.format(x=num1, y=num2)
    answer = str(gcd(num1, num2))
    return (question, answer)
