#!/usr/bin/env python


"""A "Progression game" runner."""

import sys

from brain_games.games import engine, progression


def main():
    """Run a game."""
    engine.run(progression)


if __name__ == '__main__':
    sys.exit(main() or 0)
