## Bibliotecas externas

En este paso aprenderemos a trabajar con una biblioteca para interactuar con el usuario. Le pediremos su nombre y lo saludaremos.

Para leer las entradas del usuario desde la entrada estándar, se puede usar la función estándar `input`. Si queremos que el usuario introduzca algún texto, el código sería algo así:

```python
print('May I have your name? ', end='')
name = input()
```

Si necesitamos asegurarnos de que el texto se introdujo correctamente, tendríamos que hacer algo como esto:

```python
name = ''
while name == '':
    print('May I have your name? ', end='')
    name = input()
```

A continuación, el mismo ejemplo pero utilizando una biblioteca:


```python
import prompt

name = prompt.string('May I have your name? ')
```
Este método es mucho más claro. La biblioteca **prompt** proporciona funciones para solicitar la entrada de texto, números o contraseñas. Además, las contraseñas introducidas no se mostrarán en la consola.

Cada función imprime automáticamente un "mensaje de entrada", es decir, el texto que precede la entrada del usuario. En nuestro caso, sería la cadena `'May I have your name? '`.
Por defecto, si el usuario no escribe nada y simplemente presiona Enter, la función repetirá la solicitud. Esto elimina la necesidad de usar un ciclo para solicitar la entrada, como en el segundo ejemplo.

### Enlaces

* [Biblioteca prompt](https://prompt.readthedocs.io/en/latest/)

### Tareas

1. Añade la biblioteca prompt a las dependencias usando el comando `uv add prompt`.
1. Saluda al usuario en el juego. Pídele su nombre y salúdalo personalmente:


    ```bash
    brain-games
    Welcome to the Brain Games!
    May I have your name? John
    Hello, John!
    ```

Luego, el programa se cerrará.

Crea un archivo llamado `brain_games/cli.py` y define la lógica de la función de saludo dentro de una función llamada `welcome_user()`. Coloca la llamada a esta función en el script `brain_games/scripts/brain_games.py`.

3. Compila una nueva versión del paquete.
4. Reinstala la nueva versión del paquete en tu sistema operativo.
