#!/usr/bin/env python


"""A "Calc game" runner."""

import sys

from brain_games.games import engine, calc


def main():
    """Run a game."""
    engine.run(calc)


if __name__ == '__main__':
    sys.exit(main() or 0)
