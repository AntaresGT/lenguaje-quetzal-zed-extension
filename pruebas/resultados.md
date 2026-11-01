# Resultados de pruebas

Fecha: 1 de noviembre de 2026.

Ambiente automatizado: Linux, Zed CLI 1.26.2 (`c4273271092b0287f7d181f616bd5171e0a2f70c`), Python 3.14.8, Node.js 24.21.0, Tree-sitter CLI 0.27.1 y GCC 16.2.1. Gramática `769de1c803cb00ba9863bb68735caf306d7857a1`.

## Pruebas automatizadas ejecutadas

| Prueba | Resultado | Evidencia |
|---|---|---|
| `tree-sitter build` en la fuente temporal de la gramática | Aprobado | Parser generado cargado y biblioteca compilada sin errores. |
| `tree-sitter test` | Aprobado | 62/62 pruebas de corpus, incluidos errores y Unicode. |
| `python3 pruebas/validar.py --gramatica .tmp/tree-sitter-quetzal-769de1c803cb00ba9863bb68735caf306d7857a1` | Aprobado | 120 comprobaciones: TOML, JSON, IDs, rutas, revisión fija, ausencia de Rust/LSP, capturas y nodos. |
| `python3 pruebas/validar.py` tras añadir los recursos gráficos | Aprobado | 138 comprobaciones; incluye esquema declarado, variantes clara/oscura, asociación `qz`, rutas y PNG RGBA de 128×128. |
| `tree-sitter parse --paths ../../rutas-oficiales.txt --quiet` | Aprobado | 36/36 ejemplos oficiales de la revisión fijada. |
| `tree-sitter parse --paths ../../rutas-casos.txt --quiet` | Aprobado | 5/5 casos propios válidos; `incompletos.qz` se evalúa aparte. |
| `tree-sitter query <query> --paths <rutas> --quiet` para las cinco queries | Aprobado | `highlights`, `brackets`, `indents`, `outline` y `textobjects` compilaron y se evaluaron sobre los 36 ejemplos oficiales y 5 casos propios. |
| Consulta `outline.scm` sobre `objetos-y-prototipos.qz` y `declaraciones.qz` | Aprobado | 12 capturas de elementos: funciones, objetos, prototipos, métodos y constructor, con contexto en miembros. |
| Análisis de `.tmp/snippets-expandidos.qz` | Aprobado | 13/13 snippets expandidos con sus valores por defecto; 1/1 análisis exitoso. |
| `tree-sitter parse ../../pruebas/casos/incompletos.qz --quiet --stat` | Aprobado como caso negativo | Estado 1 esperado, nodo `ERROR` localizado y análisis finalizado sin bloqueo. |

Las rutas `../../rutas-oficiales.txt` y `../../rutas-casos.txt` eran archivos temporales con las rutas de los 36 ejemplos y los 5 casos válidos. Las pruebas se ejecutaron desde el directorio temporal de la gramática. No se ejecutó código Quetzal.

## Correcciones verificadas durante la ejecución

| Problema inicial | Corrección | Verificación posterior |
|---|---|---|
| `declaraciones.qz` usaba `vacio` como identificador reservado y producía `ERROR`. | Se renombró a `valor_nulo`. | Los 5 casos válidos analizan sin errores. |
| El validador consideraba `_` de `textobjects.scm` un nombre de nodo. | Se excluyó el comodín Tree-sitter de esa comprobación. | Las 120 comprobaciones pasan; la query también compila con el CLI. |
| El CLI no encontró el parser al lanzar la prueba de snippets desde la raíz. | Se ejecutó desde el directorio temporal de la gramática. | Los 13 snippets expandidos analizan correctamente. |

## Pruebas manuales en Zed

No se controló la GUI de Zed. Todos estos casos quedan **no ejecutados**, no aprobados:

| ID | Estado | Causa |
|---|---|---|
| QZ-001 a QZ-008 | No ejecutado | Requieren instalar la dev extension y observar o editar en la interfaz. |
| QZ-009 | No ejecutado en Zed | La recuperación del parser sí se comprobó; la estabilidad del editor requiere GUI. |
| QZ-010 | No ejecutado | Requiere archivos grandes, interacción y registro del ambiente gráfico. |
| QZ-011 | No ejecutado | Requiere temas claros y oscuros en Zed. |
| QZ-012 | No ejecutado en Zed | La sintaxis expandida está aprobada; oferta, ámbito y tabstops requieren GUI. |
| QZ-013 | No ejecutado | Debe comprobarse la dev extension sin `quetzal-lsp` en el entorno del usuario. |
| QZ-014 y QZ-015 | No ejecutado | Instalación, desinstalación y reinstalación son operaciones manuales de Zed. |
| QZ-016 | No ejecutado | Requiere modo Vim en Zed. |
| QZ-017 | No ejecutado | Requiere seleccionar el tema de iconos y revisar archivos en la interfaz. |
| QZ-018 | No ejecutado | Requiere reinstalar la dev extension y probar el LSP desde la interfaz de Zed. |

## Verificación de la integración LSP

- `cargo check`: aprobado para el componente Rust con `zed_extension_api` 0.7.0.
- `cargo fmt --check`: aprobado.
- `python3 pruebas/validar.py`: aprobado, 141 comprobaciones.
- Ejecutable `quetzal-lsp --stdio`: aprobado mediante mensajes LSP reales de inicialización, apertura de documento, autocompletado y cierre. La solicitud para `hola.lon` incluyó `longitud` y el servidor negoció UTF-16.
- `cargo check --target wasm32-wasip2`: bloqueado porque el target no está instalado. Se decidió dejar que Zed lo instale durante la reinstalación de la dev extension.

## Bloqueos y límites

La compilación WebAssembly final y la integración del LSP con la interfaz de Zed quedan pendientes de reinstalar la dev extension. El CLI no ofrece un comando de instalación de dev extensions y esta sesión no controla la GUI.

No se midió rendimiento en Zed. Los tiempos del parser de otros archivos o del repositorio de gramática no se presentan como tiempos de apertura o edición en Zed.
