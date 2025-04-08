## Cómo revisar el proyecto

Al revisar, sigue:

- Checklist del proyecto.
- Referencias y prácticas de Códica.
- Este documento.

## Orden recomendado

Revisa el proyecto en este orden:

1. Formato y estructura del código.
1. Pruebas (si existen).
1. Punto de entrada del proyecto.
1. Interfaces principales.

Si detectas errores importantes, detén la revisión y pide correcciones.

## Consejos técnicos rápidos

- **Binarios:** Ejecutan funciones, no deben importar ni ser importados.
- **Funciones:** [Usa verbos claros al nombrarlas](https://codica.la/blog/naming-in-programming).
- **Números mágicos:** [Reemplázalos por constantes descriptivas](https://refactoring.guru/es/replace-magic-number-with-symbolic-constant).
- **Shebang:** Siempre utiliza env para compatibilidad.
- **Código duplicado:** Evítalo centralizando la lógica común.
- **Efectos secundarios:** Sepáralos claramente del código puro.
- **Funciones tipo `is-`:** Deben retornar solo booleanos.
- **Fixtures:** Colócalas en una carpeta específica llamada fixtures.
- **Condiciones múltiples:** Implementa polimorfismo para mayor claridad.
- **Parsing:** Usa funciones puras independientes del origen de los datos.
- **Comparación de objetos:** Unifica claves antes de evaluarlas.
- **Textos complejos:** Usa fixtures para gestionar resultados esperados.
- **Configuraciones globales:** Adminístralas desde archivos específicos.
- **Impresión en consola:** Solo desde código invocador, no desde bibliotecas.
- **Artefactos y secretos:** Nunca los subas al repositorio; utiliza variables de entorno.
- **Rutas:** Evita rutas absolutas o específicas del entorno local.

