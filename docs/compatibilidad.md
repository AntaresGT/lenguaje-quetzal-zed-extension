# Compatibilidad y auditoría

Fecha de auditoría: 1 de noviembre de 2026.

## Entorno comprobado

- Zed: `1.26.2` (`c4273271092b0287f7d181f616bd5171e0a2f70c`), Linux.
- Esquema de manifiesto: `schema_version = 1`.
- La instalación como extensión de desarrollo se realiza desde **Extensions → Install Dev Extension**.
- Las extensiones que solo aportan lenguaje, gramática, queries y snippets no necesitan Rust.
- La gramática requiere que Zed descargue `wasi-sdk` o que el usuario defina `WASI_SDK_PATH`.

Fuentes: [desarrollo de extensiones](https://zed.dev/docs/extensions/developing-extensions), [lenguajes y queries](https://zed.dev/docs/extensions/languages) y [snippets](https://zed.dev/docs/extensions/snippets).

## Gramática fijada

- Repositorio: `AntaresGT/tree-sitter-quetzal`, usado como fuente de solo lectura.
- Revisión: `769de1c803cb00ba9863bb68735caf306d7857a1`.
- Versión de la gramática: `0.1.0`; ABI de Tree-sitter: 15.
- Nombre de gramática y sufijo: `quetzal` y `qz`.
- `src/parser.c` está presente en la revisión y su SHA-256 descargado es `0b3ae432661e0b741ae400cf3d26e6e7616ad25c8fbbe87b431e3395a0140fee`.
- Los nodos y campos de las queries se contrastan con `src/node-types.json` de esa misma revisión.

Zed admite `repository` y `rev` en `[grammars.quetzal]`; la revisión no apunta a una rama fluctuante.

## Decisiones de adaptación

- Se emplean las capturas documentadas por Zed. Las capturas específicas de otros editores, como `@function.method.call`, `@keyword.control`, `@variable.member` y `@number.float`, se traducen a `@function`, `@keyword`, `@property` y `@number`.
- La interpolación conserva el resaltado de las expresiones internas; solo sus llaves reciben `@punctuation.special`.
- `indents.scm` usa `@indent`, `@start`, `@end`, `@start.if` y `@start.visibility`, no las capturas de Neovim.
- `decrease_indent_patterns` alinea `sino` y las nuevas secciones de visibilidad. Una regla de aumento indenta los miembros después de `publico:` o `privado:`.
- No se incluye `folds.scm`: la documentación vigente de extensiones de Zed no lo declara como archivo consumido. El plegado debe comprobarse con el mecanismo nativo del editor.
- No se incluyen `locals.scm` ni `injections.scm`: no sustituyen a un LSP y Quetzal no define lenguajes incrustados. En particular, `jsn` es sintaxis nativa, no una inyección JSON.
- `textobjects.scm` usa las capturas documentadas y es útil en modo Vim.
- `icon_themes/quetzal.json` sigue el esquema `icon_themes/v0.3.0.json` y asocia el sufijo `qz` con `icons/quetzal.png`. Hay variantes clara y oscura. Zed no cambia automáticamente el tema de iconos del usuario: debe seleccionar **Quetzal Icons**.
- El icono del editor es una copia RGBA de 128×128 del recurso original de 1024×1024; el logo original permanece en `imagenes/` para documentación.

## Registro, licencia y texto visible

- El ID `quetzal` no aparece en `extensions.toml` del registro oficial consultado; no se detectó un conflicto de ID.
- El ID es kebab-case, no contiene `zed` ni `extension`, y coincide con el lenguaje.
- La extensión incluye licencia MIT propia, una de las licencias aceptadas por Zed.
- La gramática declara licencia MIT en `tree-sitter.json` y `package.json`. La revisión fijada no contiene un archivo `LICENSE` en su raíz; esta observación no cambia la atribución ni la licencia declarada.
- Los textos de la galería y las descripciones de snippets están en inglés. La documentación de desarrollo permanece en español.

Fuentes: [requisitos de publicación](https://zed.dev/docs/extensions/publishing/prerequisites), [licencias](https://zed.dev/docs/extensions/publishing/license-requirements) y [registro oficial](https://github.com/zed-industries/extensions).

## LSP y límites

`AntaresGT/lenguaje-quetzal/crates/lsp/Leeme.md` declara el servidor como **futuro**. No se ha comprobado un ejecutable `quetzal-lsp` operativo. Por ello no existen entradas `language_servers`, `Cargo.toml` ni `src/lib.rs` en este MVP.

Tree-sitter aporta análisis sintáctico incremental, no diagnósticos semánticos, comprobación de tipos ni completado semántico. La instalación, el resaltado visual, la indentación, el outline, el plegado, los snippets y los temas requieren validación manual en Zed; los resultados automatizados se registran aparte en `pruebas/resultados.md`.
