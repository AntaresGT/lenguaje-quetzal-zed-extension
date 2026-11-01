#!/usr/bin/env python3

import argparse
import json
import re
import tomllib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def cargar_toml(ruta):
    with ruta.open("rb") as archivo:
        return tomllib.load(archivo)


def validar():
    analizador = argparse.ArgumentParser(description="Valida estáticamente la extensión Quetzal para Zed")
    analizador.add_argument("--gramatica", type=Path, help="Directorio de la revisión fijada de tree-sitter-quetzal")
    argumentos = analizador.parse_args()
    comprobaciones = 0

    ruta_manifiesto = RAIZ / "extension.toml"
    manifiesto = cargar_toml(ruta_manifiesto)
    config = cargar_toml(RAIZ / "languages/quetzal/config.toml")
    comprobaciones += 2

    assert manifiesto["id"] == "quetzal"
    assert manifiesto["schema_version"] == 1
    assert manifiesto["name"] == "Lenguaje Quetzal"
    assert manifiesto["description"] == "Language support for Quetzal"
    assert config["name"] == "Quetzal"
    assert config["path_suffixes"] == ["qz"]
    assert config["grammar"] == "quetzal"
    assert config["line_comments"] == ["// "]
    assert config["tab_size"] == 4
    assert config["hard_tabs"] is False
    assert set(manifiesto["grammars"]) == {"quetzal"}
    comprobaciones += 10

    gramatica = manifiesto["grammars"]["quetzal"]
    assert gramatica["repository"] == "https://github.com/AntaresGT/tree-sitter-quetzal"
    assert re.fullmatch(r"[0-9a-f]{40}", gramatica["rev"])
    assert gramatica["rev"] == "769de1c803cb00ba9863bb68735caf306d7857a1"
    assert "language_servers" not in manifiesto
    assert not (RAIZ / "Cargo.toml").exists()
    assert not (RAIZ / "src/lib.rs").exists()
    comprobaciones += 6

    rutas_snippets = manifiesto["snippets"]
    assert rutas_snippets == ["./snippets/quetzal.json"]
    ruta_snippets = RAIZ / rutas_snippets[0]
    assert ruta_snippets.resolve().is_relative_to(RAIZ)
    with ruta_snippets.open(encoding="utf-8") as archivo:
        snippets = json.load(archivo)
    assert snippets
    prefijos = set()
    for nombre, snippet in snippets.items():
        assert nombre and snippet["description"].isascii()
        assert snippet["prefix"] not in prefijos
        prefijos.add(snippet["prefix"])
        cuerpo = snippet["body"]
        assert isinstance(cuerpo, (str, list)) and cuerpo
        if isinstance(cuerpo, list):
            assert all(isinstance(linea, str) for linea in cuerpo)
    comprobaciones += 4 + len(snippets) * 4

    with (RAIZ / "icon_themes/quetzal.json").open(encoding="utf-8") as archivo:
        tema_iconos = json.load(archivo)
    assert tema_iconos["$schema"] == "https://zed.dev/schema/icon_themes/v0.3.0.json"
    assert tema_iconos["name"] == "Quetzal Icons"
    assert tema_iconos["author"] == "AntaresGT"
    assert len(tema_iconos["themes"]) == 2
    assert {tema["appearance"] for tema in tema_iconos["themes"]} == {"dark", "light"}
    assert (RAIZ / "imagenes/icono_archivos_qz.png").is_file()
    assert (RAIZ / "imagenes/logo_lenguaje_quetzal.png").is_file()
    comprobaciones += 7
    for tema in tema_iconos["themes"]:
        assert tema["name"] == "Quetzal Icons"
        assert tema["file_suffixes"] == {"qz": "quetzal"}
        ruta_icono = RAIZ / tema["file_icons"]["quetzal"]["path"]
        assert ruta_icono.resolve().is_relative_to(RAIZ)
        assert ruta_icono.is_file()
        datos_icono = ruta_icono.read_bytes()
        assert datos_icono[:8] == b"\x89PNG\r\n\x1a\n"
        assert int.from_bytes(datos_icono[16:20], "big") == 128
        assert int.from_bytes(datos_icono[20:24], "big") == 128
        assert datos_icono[24:26] == bytes([8, 6])
        comprobaciones += 8

    consultas = {
        "highlights.scm": {
            "attribute", "boolean", "comment", "comment.doc", "constant", "constant.builtin",
            "constructor", "embedded", "emphasis", "emphasis.strong", "enum", "function", "hint",
            "keyword", "label", "link_text", "link_uri", "number", "operator", "predictive", "preproc",
            "primary", "property", "punctuation", "punctuation.bracket", "punctuation.delimiter",
            "punctuation.list_marker", "punctuation.special", "string", "string.escape", "string.regex",
            "string.special", "string.special.symbol", "tag", "tag.doctype", "text.literal", "title",
            "type", "type.builtin", "variable", "variable.special", "variable.parameter", "variant",
        },
        "brackets.scm": {"open", "close"},
        "indents.scm": {"indent", "start", "end", "outdent"},
        "outline.scm": {"name", "item", "context", "context.extra", "annotation"},
        "textobjects.scm": {
            "function.around", "function.inside", "class.around", "class.inside",
            "comment.around", "comment.inside",
        },
    }
    textos_consultas = {}
    for nombre, capturas_permitidas in consultas.items():
        ruta = RAIZ / "languages/quetzal" / nombre
        texto = ruta.read_text(encoding="utf-8")
        textos_consultas[nombre] = texto
        capturas = set(re.findall(r"@([A-Za-z_][A-Za-z0-9_.]*)", texto))
        for captura in capturas:
            assert captura in capturas_permitidas or (
                nombre == "indents.scm" and captura.startswith("start.")
            ), f"Captura no documentada en {nombre}: @{captura}"
        comprobaciones += 1 + len(capturas)

    assert not (RAIZ / "languages/quetzal/folds.scm").exists()
    assert not (RAIZ / "languages/quetzal/injections.scm").exists()
    comprobaciones += 2

    if argumentos.gramatica:
        ruta_nodos = argumentos.gramatica / "src/node-types.json"
        with ruta_nodos.open(encoding="utf-8") as archivo:
            nodos = json.load(archivo)
        tipos = {nodo["type"] for nodo in nodos}
        for nombre, texto in textos_consultas.items():
            nombrados = set(re.findall(r"\(\s*([A-Za-z_][A-Za-z0-9_-]*)", texto))
            anonimos = set(re.findall(r'"([^"\\]*)"', texto))
            desconocidos = (nombrados | anonimos) - tipos - {"_"}
            assert not desconocidos, f"Nodos desconocidos en {nombre}: {sorted(desconocidos)}"
            comprobaciones += 1

    print(f"Validación estática aprobada: {comprobaciones} comprobaciones")


if __name__ == "__main__":
    validar()
