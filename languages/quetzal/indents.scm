(bloque
  "{" @start
  "}" @end) @indent

(cuerpo_objeto
  "{" @start
  "}" @end) @indent

(cuerpo_prototipo
  "{" @start
  "}" @end) @indent

(literal_lista
  "[" @start
  "]" @end) @indent

(literal_jsn
  "{" @start
  "}" @end) @indent

(lista_parametros
  "(" @start
  ")" @end) @indent

(lista_argumentos
  "(" @start
  ")" @end) @indent

(lista_importaciones
  "{" @start
  "}" @end) @indent

(lista_exportaciones
  "{" @start
  "}" @end) @indent

(parametros_tipo
  "<" @start
  ">" @end) @indent

(sentencia_condicional) @start.if
(seccion_visibilidad) @start.visibility
