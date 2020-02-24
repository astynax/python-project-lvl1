# -*- coding:utf-8 -*-

"""cli.py module."""

import prompt


def greeting():
    """greeting."""
    print('Welcome to the Brain Games!')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
