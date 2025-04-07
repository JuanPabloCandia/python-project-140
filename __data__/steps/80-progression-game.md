## Juego: «Progresión Aritmética» 

En este juego, se le muestra al jugador una **progresión aritmética** con un número faltante, representado por dos puntos. El jugador debe adivinar qué número falta.

- Se recomienda que la progresión tenga `10` números. La longitud puede variar aleatoriamente, pero debe contener al menos `5` números.
- La posición del número faltante cambiará en cada ronda de forma aleatoria.

### Ejemplo:


```
brain-progression

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
```

Si el usuario responde incorrectamente, el mensaje será:


```
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 1
'1' is wrong answer ;(. Correct answer was '15'.
Let's try again, Sam!
```

### Tareas

1. Crea un script llamado `brain_progression.py` en la carpeta _scripts_.
1. Programa la lógica necesaria para que el juego funcione correctamente.
1. Añade una nueva entrada en la sección `[project.scripts] `del archivo pyproject.toml.
1. Verifica que el juego funcione sin problemas.
1. En **README.md**, incluye una grabación de **asciinema** mostrando cómo se ejecuta el juego y los posibles resultados.
