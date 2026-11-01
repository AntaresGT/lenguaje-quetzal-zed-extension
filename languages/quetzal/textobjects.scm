(declaracion_funcion
  cuerpo: (bloque
    "{"
    (_)* @function.inside
    "}")) @function.around

(declaracion_metodo
  cuerpo: (bloque
    "{"
    (_)* @function.inside
    "}")) @function.around

(declaracion_constructor
  cuerpo: (bloque
    "{"
    (_)* @function.inside
    "}")) @function.around

(declaracion_metodo_prototipo) @function.around

(declaracion_objeto
  miembros: (cuerpo_objeto
    "{"
    (_)* @class.inside
    "}")) @class.around

(declaracion_prototipo
  miembros: (cuerpo_prototipo
    "{"
    (_)* @class.inside
    "}")) @class.around

(comentario)+ @comment.around
