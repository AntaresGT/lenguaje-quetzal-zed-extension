# Changelog

Todos los cambios notables de esta extensión se documentarán aquí.

## 0.1.0 - 2026-11-01

### Agregado

- Asociación de archivos `.qz` con el lenguaje Quetzal.
- Gramática `tree-sitter-quetzal` 0.1.0 fijada en la revisión `769de1c803cb00ba9863bb68735caf306d7857a1`.
- Resaltado adaptado a las capturas documentadas por Zed, incluidos Unicode, interpolación, tipos, objetos y prototipos.
- Emparejamiento de `()`, `[]` y `{}`.
- Indentación sintáctica y reglas para `sino` y secciones de visibilidad.
- Outline de funciones, objetos, prototipos, métodos y constructores, con contexto para miembros.
- Objetos de texto para funciones, clases y comentarios en modo Vim.
- Trece snippets limitados a Quetzal y basados en su sintaxis tipada, con nombres y descripciones en español.
- Tema opcional `Quetzal Icons`, con variantes clara y oscura e icono para archivos `.qz`.
- Logo del lenguaje en el README y recurso PNG optimizado para el editor.
- Integración con `quetzal-lsp` externo para diagnósticos, autocompletado, hover e ir a definición.
- Casos de prueba, validación estática y documentación de instalación y publicación manual.

### Pendiente de verificación manual

- Comportamiento interactivo del LSP en Zed.
- Apariencia en temas claros y oscuros, indentación, plegado, snippets y rendimiento en el editor.
