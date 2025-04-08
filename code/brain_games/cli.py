"""Prompt library usage example."""

import prompt

"""La idea es que al principio el estudiante cree brain-games
y cli.py para comprobar que todo está bien configurado.
Después, se pone a desarrollar los juegos y la lógica (el motor).
Al final, brain-games y cli.py siguen en el proyecto,
pero no se usan para nada más.
Una vez creados, ya no hace falta pensar en ellos."""


def run():
    """Interact with user."""
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
