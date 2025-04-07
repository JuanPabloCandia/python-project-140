## Inicialización del paquete

Antes de escribir los juegos, prepararemos un paquete en Python.

### Tareas

1. Lee los [consejos para completar proyectos](https://soporte.codica.la:443/link/140#bkmrk-en-la-descripci%C3%B3n-de). Estos consejos te ayudarán a mantenerte enfocado y a saber qué hacer en situaciones difíciles.
1. Instala Python versión `3.10` o superior. Aprende más en la [lección sobre instalación](https://app.codica.la/courses/python_setup_environment_course/lessons/setup/theory_unit).
1. Instala el gestor de paquetes [uv](https://docs.astral.sh/uv/).
1. Clona el repositorio del proyecto en tu máquina local. Esto creará una carpeta raíz del proyecto donde colocarás todos los archivos. Por defecto, esta carpeta tendrá el nombre del repositorio, pero puedes cambiarlo si lo deseas.
1. Inicializa tu proyecto con `uv init` y edita el nombre del proyecto en `pyproject.toml` a `hexlet-code` (necesario para las pruebas).
1. Dentro de la carpeta raíz, crea una carpeta `brain_games` y dentro de ella, una subcarpeta scripts.
1. Añade un archivo vacío `__init__.py` en cada carpeta para definirlas como paquetes. Tu estructura debería verse así:

    ```bash
    tree brain_games
    brain_games/
    ├── __init__.py
    └── scripts
        └── __init__.py
    ```

8. En `brain_games/scripts`, agrega un módulo llamado `brain_games.py`.

9. Haz que al ejecutar este módulo como programa, muestre en pantalla:


    ```bash
    uv run python -m brain_games.scripts.brain_games
    Welcome to the Brain Games!
    ```

10. Define una función `main()` en el módulo y asegúrate de que solo se llame si el módulo se ejecuta como programa. Aprende más en la lección [Punto de entrada](https://app.codica.la/courses/python_setup_environment_course/lessons/entry-point/theory_unit).

11. Configura un punto de entrada en el archivo `pyproject.toml`:

    ```toml
    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [tool.hatch.build.targets.wheel]
    packages = ["brain_games"]
    ```

12. Agrega el punto de entrada:

    ```toml
    [project.scripts]
    brain-games = "brain_games.scripts.brain_games:main"
    ```

13. Instala el paquete usando `uv sync`. Este comando creará un entorno virtual e instalará el paquete.

14. Verifica que el script funcione ejecutando:


    ```bash
    uv run brain-games
    Welcome to the Brain Games!
    ```

### Resultado 

🏁 Ahora tienes la funcionalidad mínima: un archivo que muestra un mensaje de bienvenida cuando se ejecuta desde la línea de comandos. 
