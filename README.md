# Correduria-seguros
Proyecto escrito en lenguaje python para gestionar un supuesto para una correduría de seguros de pólizas para vehículos.
Tiene diferentes funcionalidades que permiten al usuario manejarse por un CLI sencillo y operar con distintos tipos de datos.
Incluye una función de carga y guardado de datos.


## Actualizaciones

## 26/01/2025
1. Se ha formateado el archivo para que `Polizas.py`sea lógicamente correcto con el requerimiento de tener al menos un archivo registrado 
en `tomadores.py`. 
2. Se ha impuesto la condición de que el `id_tomador` en `Polizas.py` deba estar entre la base de datos de `tomadores` y además que no se repita. 
3. Se ha añadido una funcionalidad agregada que recoge una lista de `id_tomador` no permitidos para la creación de nuevas pólizas.
4. Se ha empezado a añadir la funcionalidad `ModificarPoliza()`. Actualmente recoge los `nro_poliza` y se permite trabajar con ellos. Queda
pendiente la implementación de la validación de cada uno de los datos.
5. Se ha empezado a añadir la funcionalidad `ModificarTomador()`y `EliminarTomador()` a falta de probarlas ya que no detecta `CrearPoliza`. Los `import Tomadores y recibo` asi que no se puede probar hay que revisarlo.

## 27/01/2025
1. Se ha corregido parcialmente la funcionalidad `ModificarTomador()` y se han agregado funcionalidades nuevas a `CrearTomador()` de tal manera que ahora identifica una lista de tomadores ya creados con el fin de evitar duplicidad de identificaciones y documentos de identididad. 
2. Ahora `ModificarTomador()` puede listar los campos modificables correctamente debido a un error que provocaba un comportamiento indeseado en la impresión de los campos. 
3. Ahora `ModificarTomador()` empareja adecuadamente los documentos de identificacion del tomador `id_tomador`. Esta acción es necesaria para trabajar con los campos a modificar y para que la acción repercuta solamente a la identificación seleccionada por el usuario. 
4. Ahora `ModificarTomador()` es capaz de modificar denominaciones antiguas que pudiera tener un tomador.
5. Ahora `Principal.py` maneja adecuadamente la interacción con el apartado de tomadores.
6. Ahora `ModificarTomador()` es capaz de modificar datos relativos a fechas.
7. Ahora `ModificarTomador()` valida con certeza los datos relativos a números telefónicos y correos electrónicos.
8. Se ha ampliado la política de correos electrónicos en `Utilidades.py`.
9. Se ha creado la funcionalidad `ModificarTomador()` y tras breves comprobaciones ha quedado finalmente implementada en el sistema.
10. Implementada la funcionalidad parcial de `EliminarTomador()` para los casos donde no existan pólizas registradas. Es capaz de eliminar tomadores.
11. Implementada la funcionalidad completa de `EliminarTomador()`para los casos donde existan pólizas registradas. El algoritmo de borrado debe ser capaz de eliminar la póliza asociada a un tomador que esté de BAJA (póliza no vigente actualmente).
12. Corregido un bug que hacía que `CrearRecibo()` no cumpliese con los requisitos lógicos del diseño de la aplicación.
13. `CrearRecibo()` ahora maneja una <i>banlist</i> con los identificadores que ya fueron usados para cumplir con las reglas de integridad referencial.
14. `CrearRecibo()` en su algoritmo implementa y fuerza el comprobamiento de que la póliza a la que se quiere asociar exista. 
15. Solucionado un problema de serialización e integridad con la banlist referida a los recibos.
## 28/01/2025
1. Corregido un error que agregaba datos de tipo None en `Recibos.py`. 
2. Implementada la función de modificado de recibos. Se llama `ModificarRecibo()`.
3. Se ha asegurado la condición de que `ModificarRecibo()` pueda modificar los `'id_recibo'`. 
4. Se ha implementado correctamente la función de borrado de `EliminarRecibo()`. Cumple las condiciones lógicas necesarias para el correcto manejo de los datos internos.
5. Se ha mejorado la creación de siniestros de `CrearSiniestro()`.
6. Se ha implementado la opción de borrado de `EliminarSiniestro()`. 
7. `Siniestros.py` está al día en materia de comprobaciones lógicas e interacciones con el usuario y la ecología del programa.

## 09/02/2025
### Acciones a considerar:
1. Cuando una de las pólizas, tomadores, o recibos se eliminan del sistema, hay que actualizar los banlist (o eliminar la medida de las banlist por la implementación del recorrido antes de validar).