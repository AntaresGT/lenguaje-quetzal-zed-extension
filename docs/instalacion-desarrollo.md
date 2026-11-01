# Instalación de desarrollo

## Requisitos

- Zed compatible con `schema_version = 1`; el entorno auditado usa Zed 1.26.2 en Linux.
- Acceso de red para que Zed obtenga la gramática fijada y, si hace falta, `wasi-sdk`.
- Un compilador C proporcionado por el entorno de Zed para la gramática. Esta extensión no contiene código Rust ni requiere compilar un componente WebAssembly propio.

No se necesita instalar el intérprete de Quetzal ni `quetzal-lsp`.

## Instalar la dev extension

1. Abre Zed y ve a **Extensions**.
2. Pulsa **Install Dev Extension** o ejecuta la acción `zed: install dev extension`.
3. Selecciona la carpeta que contiene `extension.toml`.
4. Espera a que termine la descarga y compilación de `tree-sitter-quetzal`.
5. Abre `pruebas/casos/declaraciones.qz`.
6. Comprueba que el selector de lenguaje muestra **Quetzal**.
7. Para ver el icono de los archivos `.qz`, abre el selector de temas de iconos de Zed y elige **Quetzal Icons**. La extensión no cambia automáticamente tu tema de iconos actual.

Si cambias el manifiesto, las queries, los snippets o el tema de iconos y Zed no refleja el cambio, vuelve a instalar la dev extension. Revisa el estado anterior antes de desinstalar para poder distinguir un fallo nuevo de uno persistente.

## Diagnóstico de carga

- Ejecuta `zed: open log` y busca errores de manifiesto, descarga, WASI o compilación de la gramática.
- Para registros más detallados, cierra Zed y ábrelo manualmente desde una terminal con `zed --foreground`.
- Si `wasi-sdk` ya está instalado, `WASI_SDK_PATH` debe señalar al directorio que contiene `bin/clang`.
- Un error de una query suele indicar el archivo y la posición; verifica que coincida con los nodos de la revisión fijada, no con otra versión de la gramática.

## Pruebas interactivas

Sigue `pruebas/matriz-pruebas.md` y registra el resultado en `pruebas/resultados.md`. Como mínimo:

1. Abre cada archivo de `pruebas/casos/` y comprueba el resaltado.
2. Escribe una línea nueva después de `{`, `[` y `(`, y comprueba el aumento de indentación.
3. Escribe los cierres en líneas nuevas y comprueba el dedent.
4. En un objeto, comprueba que los miembros posteriores a `publico:` o `privado:` reciben un nivel adicional y que la sección siguiente se alinea con la anterior.
5. Inserta `sino` en una línea nueva y comprueba su alineación con `si`.
6. Abre el outline y localiza funciones, objetos, prototipos, métodos y constructores.
7. Prueba el plegado nativo de Zed, sin asumir que exista una query `folds.scm`.
8. Expande cada snippet y desplázate por sus campos con Tab.
9. Repite el resaltado con un tema claro y otro oscuro.
10. En modo Vim, si lo utilizas, prueba `af`, `if`, `ac`, `ic` y `gc`.

## Validación estática local

Desde la raíz de la extensión:

```bash
python3 pruebas/validar.py
```

Para validar también nodos y tokens contra `src/node-types.json`, descarga la revisión fijada sin crear un repositorio adicional:

```bash
mkdir -p .tmp
curl --fail --location \
  'https://codeload.github.com/AntaresGT/tree-sitter-quetzal/tar.gz/769de1c803cb00ba9863bb68735caf306d7857a1' \
  --output .tmp/tree-sitter-quetzal.tar.gz
tar -xzf .tmp/tree-sitter-quetzal.tar.gz -C .tmp
python3 pruebas/validar.py \
  --gramatica .tmp/tree-sitter-quetzal-769de1c803cb00ba9863bb68735caf306d7857a1
```

`.tmp/` está ignorado y puede eliminarse después. La revisión contiene las herramientas npm fijadas para compilar y consultar el parser si necesitas repetir las pruebas completas documentadas en `pruebas/resultados.md`.
