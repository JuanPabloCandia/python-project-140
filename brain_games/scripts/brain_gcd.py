#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A "GCD game" runner."""

import sys

from brain_games import engine, games
from brain_games.games import gcd

def main():
    """Run a game."""
    engine.run(games.gcd)


if __name__ == '__main__':
    sys.exit(main() or 0)
