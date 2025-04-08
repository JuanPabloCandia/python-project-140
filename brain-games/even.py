"""The "Even" game."""

from random import randint

# La descripción se define a nivel del módulo (y no dentro de las funciones),
# así es más fácil ver las partes clave del juego.
# La descripción no puede tener saltos de línea,
# y no está vinculada con la salida en pantalla.
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


# https://ru.hexlet.io/blog/posts/sovershennyy-kod-proektirovanie-funktsiy
def is_even(number):
    return number % 2 == 0


def generate_round():
    """Generate a question for the one game's round."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), correct_answer
