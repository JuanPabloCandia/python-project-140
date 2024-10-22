#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A "Calc game" runner."""

import sys

from brain_games import engine, games
from brain_games.games import calc

def main():
    """Run a game."""
    engine.run(games.calc)


if __name__ == '__main__':
    sys.exit(main() or 0)
