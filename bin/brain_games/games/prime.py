"""The "Prime" game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# El concepto de es_primo está separado de la validación
# de la entrada del usuario.
# La función predicado devuelve un valor booleano.

def is_prime(number):
    """Return True if @number is Prime, otherwise return False."""
    # Casos límite: 1, 0 y números negativos
    if number <= 1:
        return False
    divisor = 2
# Optimización: introducimos una restricción al buscar divisores.
    while divisor <= number // 2:
        if not number % divisor:
            return False
        divisor += 1
    return True


def generate_round():
    """Generate data for the one round of "Prime game"."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return str(question), correct_answer
