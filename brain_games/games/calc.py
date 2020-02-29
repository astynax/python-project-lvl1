# -*- coding:utf-8 -*-

"""games/calc.py module."""

import operator
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def generate_round_data():  # noqa: WPS210
    """generate_round_data."""
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    sign, operation = choice(OPERATIONS)
    question = '{x} {sign} {y}'.format(x=num1, sign=sign, y=num2)
    answer = str(operation(num1, num2))
    return (question, answer)
