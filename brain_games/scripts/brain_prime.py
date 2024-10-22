#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A "Prime game" runner."""

import sys

from brain_games import engine, games
from brain_games.games import prime

def main():
    """Run a game."""
    engine.run(games.prime)


if __name__ == '__main__':
    sys.exit(main() or 0)
