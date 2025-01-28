# Condiciones de Creación y Gestión del Programa de Correduría

Este documento resume en detalle las condiciones necesarias para la creación y gestión de los diferentes elementos del programa de gestión de seguros de automóviles según los requisitos especificados en el ejercicio.

## 1. Pólizas

### Estructura de las pólizas:
Una póliza está representada como un diccionario con los siguientes campos:
- **nro_poliza:** Identificador único de tipo string.
- **id_tomador:** Identificador del tomador (NIF, NIE o CIF) que debe ser validado.
- **matricula:** Matrícula del vehículo (puede repetirse para distintos tomadores).
- **datos_vehiculo:** Tupla con:
  - **Tipo:** Ciclomotor, Moto, Turismo, Furgoneta, Camión.
  - **Marca:** String con la marca del vehículo.
  - **Modelo:** String con el modelo del vehículo.
  - **Funcionamiento:** Combustión, Eléctrico o Mixto.
- **cobertura:** Cobertura contratada (RC por defecto o tupla con más riesgos: RL, INC, RB, TR).
- **id_conductor:** Tupla con:
  - **nif/nie:** Identificador del conductor.
  - **fecha_nacimiento:** Fecha de nacimiento del conductor.
  - **tipo_carnet:** Tipo de carnet.
  - **fecha_carnet:** Fecha de emisión del carnet.
- **estado_poliza:** Cobrada, PteCobro o Baja.
- **fecha_emisión:** Fecha de emisión de la póliza.
- **forma_pago:** Efectivo o una tupla (Banco, nro_cuenta).

### Condiciones para la creación de pólizas:
1. El identificador de la póliza (**nro_poliza**) debe ser único.
2. El tomador asociado (**id_tomador**) debe existir previamente.
3. Debe especificarse toda la información requerida en la estructura de la póliza.

### Restricciones para modificación:
- No se permite cambiar el **nro_poliza**.

### Restricciones para eliminación:
1. No se puede eliminar una póliza vigente (estado diferente de Baja).
2. Al eliminar una póliza, deben eliminarse también sus siniestros y recibos asociados.

## 2. Tomadores

### Estructura de los tomadores:
Un tomador está representado como un diccionario con los siguientes campos:
- **id_tomador:** Identificador (NIF, NIE o CIF) validado.
- **denominacion:** Nombre del tomador (persona o empresa).
- **fecha_nacimiento:** Fecha de nacimiento (solo para personas físicas).
- **domicilio:** Domicilio del tomador.
- **movil_contacto:** Número de teléfono de contacto.
- **email_contacto:** Correo electrónico de contacto.

### Condiciones para la creación de tomadores:
1. El identificador del tomador (**id_tomador**) debe ser único.
2. Debe especificarse toda la información requerida en la estructura del tomador.

### Restricciones para modificación:
- No se permite cambiar el **id_tomador**.

### Restricciones para eliminación:
1. No se puede eliminar un tomador que tenga alguna póliza vigente.
2. Al eliminar un tomador, deben eliminarse todas las pólizas asociadas a él.

## 3. Recibos

### Estructura de los recibos:
Un recibo está representado como un diccionario con los siguientes campos:
- **id_recibo:** Identificador único del recibo.
- **nro_poliza:** Número de póliza asociada.
- **fecha_inicio:** Fecha de inicio de vigencia.
- **duración:** Periodo de vigencia (A, S, T, M).
- **importe_cobrar:** Importe a cobrar.
- **fecha_cobro:** Fecha de cobro.
- **estado_recibo:** Pendiente, Pendiente_banco, Cobrado, Cobrado_banco, Baja.
- **importe_pagar:** Importe que la correduría debe pagar a la aseguradora.
- **estado_liquidacion:** Pendiente o Liquidado.
- **fecha_liquidacion:** Fecha de liquidación.

### Condiciones para la creación de recibos:
1. El identificador del recibo (**id_recibo**) debe ser único.
2. La póliza asociada (**nro_poliza**) debe existir previamente.
3. Debe especificarse toda la información requerida en la estructura del recibo.

### Restricciones para modificación:
- No se permite cambiar el **id_recibo**.

### Restricciones para eliminación:
1. No se puede eliminar un recibo en vigor (estado Pendiente o Cobrado).


## 4. Siniestros

### Estructura de los siniestros:
Un siniestro está representado como un diccionario con los siguientes campos:
- **nro_siniestro:** Identificador único (formato `aaaa-nro_correlativo`).
- **nro_poliza:** Número de póliza asociada.
- **descripcion:** Detalle del siniestro.
- **matricula_contrario:** Matrícula del vehículo contrario (opcional).
- **compañia_contrario:** Nombre de la aseguradora del vehículo contrario.
- **nro_poliza_contrario:** Número de la póliza del vehículo contrario.
- **importe_pagar:** Importe total de la reparación.
- **estado_siniestro:** Puede tener uno de los siguientes valores:
  - **PendienteConfirmar:** No ha sido confirmado por la aseguradora contraria.
  - **Confirmado:** Confirmado por la aseguradora contraria.
  - **PendientePago:** Confirmado, pero aún no abonado.
  - **Pagado:** Abonado al cliente.
- **fecha_abono:** Fecha de abono (si el estado es `Pagado`).
- **estado_liquidacion:** Puede tener uno de los siguientes valores:
  - **Pendiente:** No liquidado aún con la aseguradora.
  - **Liquidado:** Liquidado o dado de baja.
- **fecha_liquidacion:** Fecha de la liquidación.

### Condiciones para la creación de siniestros:
1. El identificador del siniestro (**nro_siniestro**) debe ser único.
2. La póliza asociada (**nro_poliza**) debe existir, estar vigente y cobrada.
3. Debe especificarse toda la información requerida en la estructura del siniestro.

### Restricciones para modificación:
- No se permite cambiar el **nro_siniestro**.

### Restricciones para eliminación:
1. No se puede eliminar un siniestro vigente, independientemente de su estado.

---

## 5. Liquidaciones

### Estructura de las liquidaciones:
Una liquidación está representada como un diccionario con los siguientes campos:
- **nro_liquidacion:** Identificador único (formato `aaaa-nro_correlativo`).
- **fecha_liquidación:** Fecha de la liquidación.
- **estado_liquidacion:** Puede ser:
  - **Abierta:** Estado inicial al crear la liquidación.
  - **Cerrada:** Cuando la liquidación ha sido finalizada.
- **importe_recibos_cobrados:** Suma de los importes de los recibos cobrados.
- **lista_recibos_liquidar:** Lista de tuplas (nro_poliza, id_recibo).
- **importe_recibos_baja:** Suma de los importes de recibos dados de baja.
- **lista_recibos_baja:** Lista de tuplas (nro_poliza, id_recibo).
- **importe_siniestros_pagados:** Suma de los importes de siniestros pagados.
- **lista_siniestros_liquidados:** Lista de tuplas (nro_poliza, nro_siniestro).
- **importe_liquidacion:** Tupla con los valores:
  - **(importe_recibos_cobrados - importe_siniestros_pagados, importe_recibos_baja).**

### Condiciones para la creación de liquidaciones:
1. El identificador de la liquidación (**nro_liquidacion**) debe ser único.
2. La liquidación se genera con los siguientes cálculos:
   - Recibos cobrados no liquidados.
   - Siniestros pagados no descontados.
   - Recibos dados de baja no descontados.
3. El estado inicial de la liquidación es **Abierta**.

### Restricciones para modificación:
- Solo se permite cambiar el estado a **Cerrada**.

---

## 6. Estadísticas

### Opciones disponibles:
1. Mostrar toda la información de una póliza dado su identificador (**nro_poliza**).
2. Mostrar toda la información de una liquidación dado su identificador (**nro_liquidacion**).

