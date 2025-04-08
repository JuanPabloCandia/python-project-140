#!/usr/bin/env python


"""A "GCD game" runner."""

import sys

from brain_games.games import engine, gcd


def main():
    """Run a game."""
    engine.run(gcd)


if __name__ == '__main__':
    sys.exit(main() or 0)
