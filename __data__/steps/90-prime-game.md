## Juego «¿Es un número primo?»

En este juego, se le pregunta al jugador si un número dado es primo. El jugador debe responder `yes` si el número es primo o `no` si no lo es.

```
brain-prime

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
```

La lógica para respuestas correctas o incorrectas debe seguir el mismo formato que en juegos anteriores.

### Enlaces útiles

* [Predicado](https://es.wikipedia.org/wiki/Predicado_(l%C3%B3gica))
* [Números primos](https://es.wikipedia.org/wiki/Anexo:N%C3%BAmeros_primos)

### Tareas

1. Crea un script llamado `brain_prime.py` en la carpeta _scripts_.
1. Implementa la lógica necesaria para que el juego funcione correctamente, verificando si un número es primo sin usar bibliotecas externas (como sympy).
1. Añade una nueva entrada en la sección `[project.scripts]` de _pyproject.toml_.
1. Verifica que el juego funcione como se espera.
1. En **README.md**, incluye una grabación de **asciinema** mostrando cómo se ejecuta el juego y los posibles resultados.


### Consejos

- La función para verificar si un número es primo debe implementarse manualmente, sin usar bibliotecas externas. 
- No utilices [sympy](https://www.sympy.org/en/index.html), ya que no es compatible con el proyecto
- Recuerda que un número primo solo es divisible entre 1 y sí mismo.
