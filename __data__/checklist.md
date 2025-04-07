## Cómo revisamos los proyectos

Los proyectos se revisan usando **pruebas automatizadas**. Puedes ver el estado de estas pruebas en el **repositorio de GitHub**. Si alguna prueba falla, podrás ver un informe con la descripción del error en la pestaña **Actions** (mira el flujo de trabajo `hexlet-check`) en tu repositorio. Si quieres saber más sobre la revisión automática, puedes [leer aquí](https://soporte.codica.la:443/link/82#bkmrk-para-ejecutar-las-pr).

La revisión automática consta de **dos** etapas:

🔍 **Revisión de la lógica** de la aplicación 

📏 **Revisión del estilo de código** - linter 

Durante la revisión, el proyecto se compila y se prueba ejecutando los juegos. Las pruebas analizan la salida de la consola de tu aplicación. Para cada juego se verifican todos los posibles resultados: victoria o derrota del jugador.

💡 El trabajo en el proyecto se asemeja al desarrollo real. Por lo tanto, es importante revisar y analizar cuidadosamente los mensajes proporcionados por las pruebas.

## Requisitos para el proyecto

Revisa tu código según los puntos que se indican a continuación. Si es necesario, haz las correcciones en el proyecto:

- Cumplimiento visual de los requisitos 
- Cumplimiento con los estándares de codificación 
- Código que ejecuta los juegos 
- Estructura de los juegos específicos 


## Formato

✅ El archivo **README.md** debe incluir lo siguiente:

- Una descripción del proyecto.
- Los requisitos mínimos.
- Instrucciones claras de instalación y ejecución.
- Un asciinema integrado que muestre cada paso. En la grabación, debes mostrar cómo instalar la aplicación y jugar, incluyendo tanto un resultado exitoso como uno fallido.
- En la parte superior de README.md deben aparecer los badges de _CodeClimate_ y _GitHub Actions_. Estos indicadores muestran la calidad del código cuando alguien ve el proyecto por primera vez.
- Cuando instales el paquete usando `uv tool install`, asegúrate de que todos los comandos funcionen sin necesidad de usar `uv run`. Solo debe escribirse `brain-calc`, no `uv run brain-calc`.

✅ El archivo **pyproject.toml** debe estar configurado correctamente, con los siguientes campos completos:
- name 
- description 
- authors 
- readme 

✅ Las dependencias están en las secciones correctas 

✅ No debe haber archivos ni carpetas innecesarios o temporales en el repositorio. Cualquier archivo innecesario debe ser añadido al archivo `.gitignore` ([consulta](https://github.com/hexlet-boilerplates/python-package)).

## Servicios

🟢 La insignia de **CodeClimate** es verde 

## Código

- El proyecto **no** usa clases. Las tareas planteadas se pueden resolver fácilmente sin ellas.
- Todos los scripts están organizados según las [recomendaciones](https://app.codica.la/courses/python_setup_environment_course/lessons/entry-point/theory_unit).
- El código **no** contiene números mágicos.
- **No** se utiliza la [biblioteca sympy](https://www.sympy.org/en/index.html) para encontrar números primos.

## Estructura de archivos

📂 En el directorio que representa el paquete `brain_games`, no hay archivos innecesarios, solo subpaquetes y archivos con la extensión `.py`.

📂 La lógica general se ha extraído a un módulo separado.

📂 El código de cada juego está en un **módulo separado**.

📂 Se ha creado un paquete **games** para los módulos de los juegos.

📂 Se ha creado un directorio **scripts** para los scripts.


## Nombres

- Los nombres de las constantes siguen el estilo `UPPER_SNAKE_CASE`.
- Los nombres de funciones y variables siguen el estilo `snake_case`.
- Los nombres son semánticos y reflejan el contenido de las entidades que describen.

