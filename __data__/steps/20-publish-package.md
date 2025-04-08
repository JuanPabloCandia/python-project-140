## Preparación del paquete para su publicación

Al final de este paso, nuestro paquete será un programa que, tras su instalación, estará disponible con el nombre `brain-games` y mostrará un mensaje de bienvenida al ejecutarlo.

### Enlaces útiles

* [¿Qué es un Makefile y cómo empezar a usarlo?](https://codica.la/guias/makefile-as-task-runner/)
* [Paquete Python completamente configurado](https://github.com/hexlet-boilerplates/python-package). Si tienes dudas, compara tu solución con este template.

### Tareas

1. Crea un archivo _Makefile_ con el comando `install`, que ejecute `uv sync`. Este comando es útil al clonar el repositorio por primera vez o tras eliminar las dependencias. Nota: las líneas en un Makefile se separan con tabulaciones.
1. Agrega la carpeta `.venv` al archivo `.gitignore`. Las dependencias no deben almacenarse en el repositorio.
1. Añade al _Makefile_ el comando `brain-games`:

    ```Makefile
    brain-games:
        uv run brain-games
    ```

Escribir este comando manualmente puede ser lento, pero usar `make brain-games` es rápido y sencillo.

## Publicación

Subir el código a GitHub está bien, pero no es suficiente para que otros puedan usarlo. Es necesario empaquetarlo como un paquete instalable y publicarlo en un catálogo de paquetes. **PyPI** (_Python Package Index_) es uno de los catálogos más grandes y populares para paquetes de Python. También se le conoce como "el índice". Cada vez que ejecutas `uv add <package>`, la instalación se realiza desde este catálogo por defecto.

Existen otros catálogos y hasta repositorios como GitHub o GitLab que permiten publicar paquetes instalables.

Antes de publicar, el proyecto debe compilarse. Esto se logra con el comando `uv build`. Tras ejecutarlo, se creará una carpeta /dist en el proyecto con el paquete compilado. Luego, puedes instalar el paquete en tu sistema con `uv tool install dist/*.whl`. Este comando debe ejecutarse desde la raíz del proyecto.

### Enlaces útiles

* [Shebang](https://es.wikipedia.org/wiki/Shebang)
* [uv:cli](https://docs.astral.sh/uv/concepts/projects/config/#command-line-interfaces)
* [uv:build](https://docs.astral.sh/uv/concepts/projects/build/)
* [Versionado semántico](https://semver.org/lang/es//)

### Tareas

1. Agrega al Makefile el comando `build`, que ejecute `uv build`.
1. Añade al Makefile el comando `package-install`, que ejecute `uv tool install dist/*.whl`.
1. Compila el paquete. Si aparecen errores o advertencias, corrígelos.
1. Instala el paquete en tu sistema usando `make package-install` y verifica que funcione ejecutando `brain-games` en la terminal.
1. Sube los cambios al repositorio de GitHub y continúa con el siguiente paso.
