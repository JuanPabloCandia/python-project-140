## Juego: «¿Par o impar?»

🎲 Vamos a crear un juego llamado _¿Par o impar?_. Se muestra un número aleatorio, y el jugador debe responder `yes` si el número es par o `no` si es impar.


```
Welcome to the Brain Games!
May I have your name? Bill
Hello, Bill!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: yes
```

Si la respuesta es incorrecta: el juego termina y aparece este mensaje:

```
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bill!
```

Si la respuesta es correcta: se muestra:

```
Correct!
```

¡Y se pasa a la siguiente pregunta! 

El jugador debe responder correctamente **tres preguntas seguidas**. Si lo logra, aparece este mensaje:

```
Congratulations, Bill!
```

Ejemplo completo del flujo del juego:

```
brain-even

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!
```
**Reglas**

- Cualquier entrada incorrecta cuenta como error, por ejemplo: si el jugador escribe `n` en lugar de `no`, se considera una respuesta equivocada.
- Si se comete un error, el juego termina.

### Enlaces útiles

* [Don’t repeat yourself](https://es.wikipedia.org/wiki/No_te_repitas)
* [YAGNI](https://es.wikipedia.org/wiki/YAGNI)
* [KISS](https://es.wikipedia.org/wiki/Principio_KISS)
* [Números mágicos](https://es.wikipedia.org/wiki/N%C3%BAmero_m%C3%A1gico_(inform%C3%A1tica))

### Tareas

1. Crear el script principal: En la carpeta `scripts`, crea un archivo llamado `brain_even.py`.
2. Implementar la lógica del juego: 
- Los archivos previos (`brain_games/cli.py` y `brain_games/scripts/brain_games.py`) no deben mezclarse con el nuevo código.
- Crea toda la lógica del juego en nuevos módulos.

3. Actualizar la configuración del proyecto: Agrega esta entrada en `[project.scripts]` del archivo `pyproject.toml`:



    ```toml
    [project.scripts]
    brain-games = "brain_games.scripts.brain_games:main"
    brain-even = "brain_games.scripts.brain_even:main"
    ```

4. Construir y probar el paquete:
- Compila el paquete.
- Asegúrate de que al ejecutar `brain-even` desde la terminal, el juego se inicie correctamente.
5. Grabar una demostración:
Usa [asciinema](https://asciinema.org) para grabar cómo instalas el paquete, inicias el juego, ganas y pierdes. Luego, incluye esta grabación en el archivo _README.md_.

### Consejos

- Los scripts solo deben usar lógica que esté bien estructurada en otros módulos.
- La carpeta `brain_games/scripts` debe contener solo scripts.
- **No usamos clases** en este proyecto, todo debe resolverse con funciones simples.
