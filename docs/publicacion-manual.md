# Publicación manual

Estas instrucciones están reservadas al usuario. La preparación de la extensión no incluye crear repositorios, ramas, commits, tags, pull requests ni releases.

## 1. Revisar antes de publicar

1. Completa las pruebas manuales de `pruebas/matriz-pruebas.md` con la revisión exacta que se publicará.
2. Actualiza `pruebas/resultados.md`, `CHANGELOG.md` y la versión si corresponde.
3. Confirma que `LICENSE` sigue en la raíz y que los textos visibles al usuario están en inglés.
4. Revisa que el ID `quetzal` siga disponible en el registro oficial.
5. Comprueba que la gramática permanece fijada a un commit completo y que `src/parser.c` existe en esa revisión.

Consulta los [requisitos vigentes](https://zed.dev/docs/extensions/publishing/prerequisites) y las [licencias aceptadas](https://zed.dev/docs/extensions/publishing/license-requirements) antes de continuar.

## 2. Crear y preparar el repositorio de la extensión

El usuario crea manualmente `AntaresGT/lenguaje-quetzal-zed-extension` en GitHub. La URL ya declarada en `extension.toml` es el destino previsto, no una confirmación de que el repositorio remoto exista.

Revisa el estado y los cambios:

```bash
git status
git diff
```

Conecta o corrige el remoto solo si hace falta. Después, el usuario decide y ejecuta personalmente sus operaciones de versión, por ejemplo:

```bash
git add extension.toml Cargo.toml Cargo.lock src languages snippets icon_themes icons imagenes pruebas docs README.md CHANGELOG.md LICENSE .gitignore
git commit -m "Add Quetzal language support for Zed"
git push -u origin main
```

Si decide crear una etiqueta para la versión:

```bash
git tag v0.1.0
git push origin v0.1.0
```

La versión del tag, `extension.toml` y la entrada futura del registro deben ser coherentes. Verifica el commit exacto:

```bash
git rev-parse HEAD
git status
```

Instala y prueba manualmente la dev extension desde ese mismo commit antes de enviarla.

## 3. Preparar el registro oficial

Sigue la [guía oficial de publicación](https://zed.dev/docs/extensions/publishing/publishing-guide). El usuario realiza manualmente estos pasos:

1. Crea un fork de `zed-industries/extensions`, preferiblemente en una cuenta personal si desea permitir cambios de los mantenedores.
2. Clona su fork e inicializa los submódulos existentes.
3. Añade esta extensión como submódulo HTTPS en `extensions/quetzal`; el commit debe estar disponible en una rama pública.
4. Añade la entrada en el `extensions.toml` del registro:

```toml
[quetzal]
submodule = "extensions/quetzal"
version = "0.1.0"
```

5. Ejecuta `pnpm sort-extensions` para ordenar `extensions.toml` y `.gitmodules`.
6. Revisa el diff y prueba de nuevo el commit del submódulo que se enviará.
7. Crea personalmente el commit, push y pull request.

Cada PR debe agregar o actualizar exactamente una extensión. Consulta también el límite vigente de PR abiertos y el plazo para responder revisiones en la guía oficial. No combines esta publicación con cambios en otras extensiones.

## 4. Revisiones y versiones posteriores

- Atiende los comentarios de los mantenedores en el PR.
- Para una versión posterior, actualiza primero la extensión y sus pruebas; después actualiza el submódulo y la versión en otro PR manual.
- Los releases, tags y anuncios quedan a decisión del usuario.
- No automatices publicaciones desde esta documentación ni agregues workflows de release como parte de este MVP.
