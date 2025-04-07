## Objetivo

### Configuración del entorno

El primer proyecto será tu primera experiencia creando un programa completo fuera del entorno de Códica. Aprenderás los pasos esenciales para iniciar cualquier proyecto: 

🐍 **Instalar el lenguaje** (_intérprete_)

⚙️ **Configurar el entorno** (_sistema operativo, editor, linters_)

📚 **Conectar bibliotecas adicionales**

🗂️ **Crear un repositorio en Git**

Este proyecto te ayudará a mejorar en el ecosistema de Python. Configurarás tu entorno de desarrollo, aprenderás a ejecutar programas y a usar el intérprete (_REPL_) para depurar y probar código. Además, trabajarás con [uv](https://docs.astral.sh/uv), una herramienta para gestionar proyectos: instalar bibliotecas, actualizar paquetes y más.

Por último, te familiarizarás con **GitHub** 🌐, el lugar principal para almacenar código y colaborar con otros programadores. Tener repositorios reales en GitHub te abrirá puertas al desarrollo de software de código abierto (_Open Source_) y mejorará tus oportunidades laborales.

Aunque configurar el entorno puede tomar varios días y dependerá de tu sistema, este paso es esencial. Una vez que lo domines, iniciar nuevos proyectos será rápido y fácil.

Si decides instalar Ubuntu como sistema adicional, podrás profundizar en los principios de los sistemas operativos, el uso de gestores de paquetes y el funcionamiento del sistema de archivos (archivos ejecutables, permisos). Muchos terminan adoptándolo como su sistema principal.

También desarrollarás una buena cultura de ingeniería. Una de las primeras tareas será configurar un linter ([ruff](https://docs.astral.sh/ruff)), que verificará automáticamente el estilo de tu código y detectará errores. Escribir código que cumpla con estándares lo hace más fácil de analizar y más valorado por otros programadores, algo crucial al presentar proyectos en entrevistas laborales.

### Código

A diferencia de los entornos en línea, los proyectos de Códica incluyen varios archivos. Aprenderás a gestionar módulos, importar funciones y dividir tu programa en partes. Incluso la estructura de directorios será importante.

Este proyecto incluye interacción desde la línea de comandos. Necesitarás instalar y usar una biblioteca adicional, lo que implicará leer documentación, como en el desarrollo real.

También deberás nombrar archivos, funciones y variables de forma clara, algo que puede ser un desafío incluso para programadores con experiencia.

La arquitectura del proyecto es clave. Aprenderás a aislar efectos secundarios, crear barreras de abstracción y mantener la modularidad. Resolverás preguntas como: "¿Quién interactúa con el usuario?" o "¿Cómo dividir responsabilidades?". Incluso si tienes experiencia, esta parte será un reto.


### ¿Puedes saltarte el primer proyecto?

❌ **No.** Cada proyecto en Códica es esencial. Este primer proyecto te enseñará prácticas de ingeniería, cómo estructurar tu código y cumplir con estándares de codificación. Incluso si ya tienes experiencia, será útil.

Tu mentor revisará tu código y, según tu nivel, podría proponerte tareas adicionales. No será un proceso fácil, incluso si completas las tareas rápido.

## Revisión de los mentores

Tu mentor evaluará estos aspectos:

✅ Configuración del proyecto y cumplimiento de estándares.

✅ Uso de nombres claros y adecuados.

✅ Soluciones simples. Evitarás complicar el código innecesariamente, algo común cuando falta experiencia.

✅ Arquitectura. Dividir correctamente las funciones y responsabilidades dentro del sistema es crucial.


## Descripción

**«Juegos mentales»** es un conjunto de cinco juegos de consola para entrenar el cerebro. Cada juego plantea preguntas que debes responder correctamente. Si aciertas tres veces, ganas. Un error termina el juego y te invita a intentarlo de nuevo. Los juegos son:

🎲 **Calculadora:** Resuelve expresiones aritméticas.

🎲 **Progresión:** Encuentra el número que falta en una secuencia.

🎲 **Números pares:** Determina si un número es par.

🎲 **Máximo común divisor:** Calcula el MCD de dos números.

🎲 **Números primos:** Identifica si un número es primo.

## Ejemplo

```bash
brain-progression
¡Bienvenido a Brain Game!
¿Qué número falta en esta progresión?
¿Cuál es tu nombre? Juan  
¡Hola, Juan!  
Pregunta: 14 .. 18 20 22 24 26 28  
Tu respuesta: 16 # El usuario ingresa la respuesta  
¡Correcto!  
Pregunta: 5 6 7 8 9 .. 11 12  
Tu respuesta: 10 # El usuario ingresa la respuesta  
¡Correcto!  
Pregunta: 12 15 18 21 .. 27 30 33  
Tu respuesta: 24 # El usuario ingresa la respuesta  
¡Correcto!  
¡Felicidades, Juan!  
```
