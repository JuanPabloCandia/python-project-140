"""The game engine."""

import prompt

ROUNDS_COUNT = 3


# Lógica general de los juegos.
# Se encarga de la interacción con el usuario 
# y el proceso del juego (algoritmo)
# No sabe nada sobre juegos específicos.
# Solo entiende los conceptos de "descripción" y "pregunta" con "respuesta",
# que son proporcionados por el juego.
def run(game):
    """Run a game defined in game module."""
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}')

    count = ROUNDS_COUNT
    while count:
        # Desestructuración es opcional
        question, correct_answer = game.generate_round()

        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(
                f'{answer} is wrong answer ;(. '
                f'Correct answer was {correct_answer}.',
            )
            print(f"Let's try again, {name}!")
            return

        print('Correct!')
        count -= 1

    print(f'Congratulations, {name}!')
