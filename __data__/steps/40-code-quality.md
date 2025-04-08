## Calidad del código

El seguimiento automático de la calidad del código es un componente esencial en el desarrollo moderno. En este paso, configuraremos algunos de los servicios más conocidos y un linter para verificar el estilo de codificación.

## CodeClimate

En un entorno de desarrollo bien organizado, la calidad del código se supervisa de manera automática. Existen servicios en línea, como **CodeClimate**, que realizan este seguimiento. Este servicio es gratuito para proyectos OpenSource y su integración se realiza en solo un par de clics tras registrarse.

### Enlaces

* [CodeClimate](https://codeclimate.com/)
* [¿Qué es Markdown?](https://codica.la/guias/markdown/)

### Tareas

1. Regístrate en [CodeClimate](https://codeclimate.com/) y, durante el registro, selecciona la rama **Quality**.
1. Conecta tu repositorio al servicio.
1. Agrega el insignia **Maintainability** de tu proyecto en el archivo **README** (consulta Repo _Settings -> Extras -> Badges_).


## ruff

En todos los lenguajes de programación existe algo llamado _estilo de codificación_. Sin embargo, no todos los desarrolladores lo conocen y algunos escriben código sin seguir reglas claras. Esto suele generar frustración entre los miembros del equipo y afecta negativamente la motivación. Aprender a escribir código siguiendo estándares desde el principio facilita la colaboración y la adaptabilidad.

Los empleadores valoran a los candidatos que aplican enfoques estándar en sus proyectos. Esto aumenta tus probabilidades de ser contratado frente a alguien que no sigue buenas prácticas.

Los programas encargados de verificar que el código cumpla con los estándares se llaman **linters**. Antes de escribir cualquier código, es importante configurar uno. En este proyecto utilizaremos **ruff**.


### Enlaces

* [ruff](https://docs.astral.sh/ruff/)
* [Double Dash](https://unix.stackexchange.com/questions/11376/what-does-double-dash-mean-also-known-as-bare-double-dash)

### Tareas

1. Añade **ruff** a las dependencias de desarrollo: `uv add --dev ruff`.
2. Configura [este archivo de configuración ](https://github.com/hexlet-boilerplates/python-package/blob/main/ruff.toml) en tu proyecto.
3. Verifica que la herramienta funcione con el comando:: `uv run ruff check brain_games`
4. Crea en el _Makefile_ una tarea `make lint`:

    ```Makefile
    make lint:
        uv run ruff check brain_games
    ```

5. Corrige todos los errores que detecte el linter.

