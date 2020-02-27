# -*- coding:utf-8 -*-

"""brain_calc script."""
from brain_games.engine import engine
from brain_games.games.calc import DESCRIPTION, generate_round_data


def main():
    """Run this script."""
    engine(DESCRIPTION, generate_round_data)


if __name__ == '__main__':
    main()