# -*- coding:utf-8 -*-

"""games/calc.py module."""
from random import randint

DESCRIPTION = 'What is the result of the expression?'


def generate_round_data():
    """generate_round_data."""
    first_num = randint(1, 10)
    second_num = randint(1, 10)

    operation_signs = ['+', '-', '*']
    sign = operation_signs[randint(0, len(operation_signs) - 1)]
    question = '{x} {sign} {y}'.format(x=first_num, sign=sign, y=second_num)

    if sign == '+':
        answer = first_num + second_num
    elif sign == '-':
        answer = first_num - second_num
    else:
        answer = first_num * second_num

    return (question, str(answer))
