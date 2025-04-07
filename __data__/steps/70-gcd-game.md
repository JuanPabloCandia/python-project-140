## Juego: «Máximo Común Divisor»

Debes implementar el juego llamado **«Máximo Común Divisor»** (_MCD_). La idea del juego es la siguiente: se mostrarán dos números aleatorios al usuario, por ejemplo, `25 50`. El usuario debe calcular e ingresar el máximo común divisor de esos números.

### Ejemplo del flujo del juego

```
brain-gcd

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!
```

Si el usuario da una respuesta incorrecta, el mensaje debe ser el siguiente:

```
Question: 25 50
Your answer: 1
'1' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!
```

### Tareas

1. Crea un nuevo script en la carpeta _scripts_ con el nombre `brain_gcd.py`.
1. Implementa la lógica necesaria para que el juego funcione correctamente.
1. Añade una nueva entrada en la sección `[project.scripts]` del archivo `pyproject.toml`.
1. Verifica que el nuevo juego funcione como se espera.
1. Incluye en **README.md** una grabación de **asciinema** que muestre cómo se ejecuta el juego y los diferentes resultados posibles.


### Consejos

* ¿La forma de encontrar el MCD depende de cómo se usa la función que lo calcula?
