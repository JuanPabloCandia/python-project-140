#!/usr/bin/env python


"""A "Prime game" runner."""

import sys

from brain_games.games import engine, prime


def main():
    """Run a game."""
    engine.run(prime)


if __name__ == '__main__':
    sys.exit(main() or 0)
