# Matriz de pruebas de la extensión Quetzal para Zed

Estados permitidos en los resultados: **aprobado**, **fallido** o **no ejecutado**. Una query que compila no demuestra por sí sola que la función correspondiente funcione en la interfaz de Zed.

| ID | Caso y procedimiento | Resultado esperado |
|---|---|---|
| QZ-001 | Abrir `pruebas/casos/declaraciones.qz` tras instalar la dev extension. | El selector identifica el archivo como Quetzal y el parser carga. |
| QZ-002 | Abrir `pruebas/casos/no-es-quetzal.txt`. | Zed no lo asocia automáticamente con Quetzal. |
| QZ-003 | Abrir `acentos-y-unicode.qz`; editar identificadores con `ñ` y tildes. | El texto se conserva y las palabras reservadas acentuadas se resaltan. |
| QZ-004 | Abrir `objetos-y-prototipos.qz` y revisar resaltado y outline. | Objetos, prototipos, métodos y constructor aparecen con sus nombres y contexto. |
| QZ-005 | Abrir `importaciones.qz`. | Importaciones, alias, exportaciones y rutas tienen resaltado coherente. |
| QZ-006 | En bloques y listas, pulsar Enter después de `{`, `[` y `(`; probar miembros tras una sección de visibilidad. | La línea nueva recibe un nivel de indentación de 4 espacios. |
| QZ-007 | Escribir `}`, `]` y `)` en líneas nuevas; insertar `sino` y otra sección de visibilidad. | Los cierres reducen indentación; `sino` y la nueva sección se alinean con su estructura. |
| QZ-008 | Editar la interpolación de `declaraciones.qz` y `acentos-y-unicode.qz`. | Texto, escapes, llaves y expresión interna conservan categorías distinguibles. |
| QZ-009 | Abrir y editar `incompletos.qz`; introducir y corregir errores parciales. | Zed permanece estable y el resaltado se recupera sin un fallo masivo persistente. |
| QZ-010 | Abrir archivos de aproximadamente 100, 1.000, 10.000 y 50.000 líneas; desplazarse y editar. | Interacción utilizable sin cierres ni bloqueos persistentes; registrar ambiente y observaciones, no un objetivo inventado. |
| QZ-011 | Revisar todos los casos con al menos un tema claro y uno oscuro. | Comentarios, tipos, funciones, variables, cadenas y operadores tienen contraste comprensible. |
| QZ-012 | Expandir `si` y después los demás snippets en un archivo `.qz`; usar Tab. | Solo se ofrecen en Quetzal, generan sintaxis válida y los tabstops funcionan. |
| QZ-013 | Usar la extensión sin `quetzal-lsp` en `PATH`. | Resaltado, estructura y snippets siguen funcionando; no aparece un LSP inexistente como requisito. |
| QZ-014 | Instalar mediante **Install Dev Extension**. | Zed reconoce la extensión y compila la revisión fijada. |
| QZ-015 | Desinstalar y reinstalar la dev extension tras un cambio de query. | No quedan fallos persistentes ni versiones contradictorias de la extensión. |
| QZ-016 | En modo Vim, probar `af`, `if`, `ac`, `ic` y `gc` en declaraciones y comentarios. | Se seleccionan las estructuras esperadas; si el modo Vim no se usa, registrar no ejecutado. |
| QZ-017 | Seleccionar **Quetzal Icons** en el selector de temas de iconos y revisar archivos `.qz` y de otros tipos con apariencia clara y oscura. | Los `.qz` muestran el icono Quetzal; el resto conserva el comportamiento de respaldo de Zed y no desaparece. |

## Preparación de archivos de rendimiento

Los archivos sintéticos no se distribuyen. Pueden generarse dentro de `.tmp/` con Python, repitiendo declaraciones sintácticamente válidas y variando sus nombres. Deben registrarse versión de Zed, sistema operativo, CPU, tamaño real, método de observación y si la medición corresponde a apertura, análisis o percepción de edición.

## Evidencia recomendada

- Versión exacta de Zed y tema utilizado.
- Archivo, pasos y resultado observado.
- Extracto relevante de `zed: open log` ante un fallo.
- Capturas solo si se generan realmente y el usuario decide conservarlas.
