## Juego: «Calculadora» 🧮

Vamos a implementar el juego «Calculadora». La idea principal es simple: se le muestra al jugador una expresión matemática aleatoria, por ejemplo, `35 + 16`, y debe calcular el resultado y escribir la respuesta correcta. ¡Diviértete poniendo a prueba tus habilidades matemáticas! 🚀

### Ejemplo del flujo del juego:

```
brain-calc

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!
```

### Detalles importantes

- **Operaciones disponibles:** Implementaremos las operaciones básicas: `+`, `-` y `*`.
- **Aleatoriedad:** Tanto los números como las operaciones se seleccionarán de forma aleatoria.

## Qué sucede si hay una respuesta incorrecta: ❌

Si el jugador responde mal, se muestra el siguiente mensaje:

```
Question: 25 * 7
Your answer: 145
'145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Sam!
```

El juego finaliza inmediatamente si el jugador comete un error.

### Reglas del juego: 

- El jugador debe responder correctamente a tres **preguntas seguidas** para ganar.
- Si el jugador responde mal en cualquier momento, el juego termina.

### Enlaces útiles

* [Principio de apertura/cierre (OCP)](https://es.wikipedia.org/wiki/Principio_de_abierto/cerrado)
* [Diseño de interfaces (API)](https://es.wikipedia.org/wiki/API)
* [Efectos secundarios](https://es.wikipedia.org/wiki/Efecto_secundario_(inform%C3%A1tica))

### Tareas

1. Crear el script: En la carpeta _scripts_, crea un archivo llamado `brain_calc.py`.
2. Implementar la lógica: 
- Diseña el flujo que muestre las preguntas, valide las respuestas y determine si el jugador gana o pierde.
- Crea funciones reutilizables para evitar repetir código.
3. Actualizar el archivo de configuración: Agrega el siguiente contenido a la sección `[project.scripts]` en el archivo `pyproject.toml`:
```python
[project.scripts]
brain-games = "brain_games.scripts.brain_games:main"
brain-even = "brain_games.scripts.brain_even:main"
brain-calc = "brain_games.scripts.brain_calc:main"
```
4. Probar el juego:
- Asegúrate de que todo funcione correctamente.
- Graba una demostración con **asciinema**, mostrando:
    - Un escenario en el que el jugador gana.
    - Un escenario donde pierde.
- Agrega el enlace de la grabación al archivo **README.md**.

### Consejos

- **Unifica la lógica** común de los juegos:
Dado que ahora hay varias dinámicas, extrae las partes comunes (como mostrar preguntas, validar respuestas y llevar la cuenta del progreso) a un módulo central que pueda ser reutilizado.
- **Organización del proyecto:**
     - Coloca la lógica específica de cada juego en una carpeta llamada games.
     - Mantén la lógica compartida en un solo módulo para facilitar su mantenimiento y evitar duplicaciones.
- **Número de rondas:** Define un número fijo de rondas (`3`) para todos los juegos, garantizando consistencia y simplificando la estructura.

