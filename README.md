# Correduria-seguros
Proyecto escrito en lenguaje python para gestionar un supuesto para una correduría de seguros de pólizas para vehículos.
Tiene diferentes funcionalidades que permiten al usuario manejarse por un CLI sencillo y operar con distintos tipos de datos.
Incluye una función de carga y guardado de datos.


## Actualizaciones

26/01/2025
1. Se ha formateado el archivo para que `Polizas.py`sea lógicamente correcto con el requerimiento de tener al menos un archivo registrado 
en `tomadores.py`. 
2. Se ha impuesto la condición de que el `id_tomador` en `Polizas.py` deba estar entre la base de datos de `tomadores` y además que no se repita. 
3. Se ha añadido una funcionalidad agregada que recoge una lista de `id_tomador` no permitidos para la creación de nuevas pólizas.
4. Se ha empezado a añadir la funcionalidad `ModificarPoliza()`. Actualmente recoge los `nro_poliza` y se permite trabajar con ellos. Queda
pendiente la implementación de la validación de cada uno de los datos.
5. Se ha empezado a añadir la funcionalidad `ModificarTomador()`y `EliminarTomador()` a falta de probarlas ya que no detecta `CrearPoliza`. Los `import Tomadores y recibo` asi que no se puede probar hay que revisarlo.
27/01/2025
1. Se ha corregido parcialmente la funcionalidad `ModificarTomador()` y se han agregado funcionalidades nuevas a `CrearTomador()` de tal manera que ahora identifica una lista de tomadores ya creados con el fin de evitar duplicidad de identificaciones y documentos de identididad. 
2. Ahora `ModificarTomador()` puede listar los campos modificables correctamente debido a un error que provocaba un comportamiento indeseado en la impresión de los campos. 
3. Ahora `ModificarTomador()` empareja adecuadamente los documentos de identificacion del tomador `id_tomador`. Esta acción es necesaria para trabajar con los campos a modificar y para que la acción repercuta solamente a la identificación seleccionada por el usuario. 
4. Ahora `ModificarTomador()`es capaz de modificar denominaciones antiguas que pudiera tener un tomador.
5. Ahora `Principal.py` maneja adecuadamente la interacción con el apartado de tomadores.