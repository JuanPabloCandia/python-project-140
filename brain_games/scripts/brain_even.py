#!/usr/bin/env python


"""An "Even game" runner."""

import sys

from brain_games.games import engine, games


def main():
    """Run a game."""
    engine.run(even)


if __name__ == '__main__':
    sys.exit(main() or 0)
