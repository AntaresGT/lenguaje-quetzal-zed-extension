(declaracion_funcion
  nombre: (identificador) @name) @item

(declaracion_objeto
  nombre: (identificador) @name) @item

(declaracion_prototipo
  nombre: (identificador) @name) @item

(declaracion_objeto
  nombre: (identificador) @context
  miembros: (cuerpo_objeto
    (declaracion_metodo
      nombre: (identificador) @name) @item))

(declaracion_objeto
  nombre: (identificador) @context
  miembros: (cuerpo_objeto
    (declaracion_constructor
      nombre: (identificador) @name) @item))

(declaracion_prototipo
  nombre: (identificador) @context
  miembros: (cuerpo_prototipo
    (declaracion_metodo_prototipo
      nombre: (identificador) @name) @item))
