#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
# Función para crear una liquidación
'''Tendrá opciones para generar, modicar y cerrar una liquidación.
Cosas a tener en cuenta:
• No se permiten liquidaciones con igual identicación, recordar que es un campo
con números correlativos.
• La liquidación se genera de la siguiente forma:
- Se barre la lista de recibos y se cogen todos los recibos que se han cobrado
por la agencia y que no se han liquidado a la compañía de seguros. Se
totaliza la cantidad de dinero que se debería pagar a la compañía por este
concepto.
- Luego se barre la lista de siniestros para conseguir todos aquellos que ha
pagado la agencia pero que no se han descontado (liquidado) todavía a la
compañía de seguros. Se totaliza la cantidad de dinero que se debería pagar
a la compañía por este concepto.
- Por último, se barre la lista de recibos y se cogen todos los recibos que son
baja y que no se han descontado a la compañía de seguros. Se totaliza la
cantidad de dinero que ya no debemos enviar a la compañía.
- Se rellenan el resto de campos con los cálculos explicados al comienzo, a
excepción del campo estado.
- Cerrar una liqui    dación lo que hace es cambiar de estado a una liquidación
abierta existente.'''
#Estructura de datos
'''Liquidaciones: es la estructura que contiene los datos de las liquidaciones
realizadas a la aseguradora. Se trata de una lista en la que cada elemento será un
diccionario con los campos siguientes:
nro_liquidacion: campo que identica al siniestro. Tiene el siguiente formato
aaaa-nro_correlativo
fecha_liquidación: la fecha en la que se realiza la liquidación.
estado_liquidacion: Un campo con dos valores:
• Abierta: es el estado en el que se crea la liquidación.
• Cerrada: cuando se ha da por buenos los datos de la liquidación.
(1) importe_recibos_cobrados: suma de los importes a pagar de los recibos
cobrados por la correduría que se deben abonar a la compañía de seguros.
***lista_recibos_liquidar: una lista con tuplas con la siguiente información:
(nro_poliza, nro_recibo).
(2) importe_recibos_baja: suma de los importes a dar de baja de la deuda de los
recibos no cobrados por la correduría de las pólizas que se van a dar de baja.
lista_recibos_baja: una lista con tuplas con la siguiente información: (nro_poliza,
nro_recibo).
(3) importe_siniestros_pagados: suma de los importes abonados por la
correduría de los siniestros pagados a descontar en la liquidación.
lista_siniestros_pagados: una lista con tuplas con la siguiente información:
(nro_poliza, nro_siniestro).
importe_liquidacion: Una tupla con la siguiente información ( (1) - (3), (2) ). El
primer campo es la resta de lo marcado como (1) menos el importe de lo marcado
como (3), el segundo campo es el valor marcado como (2).'''

#Es el año actual el que se pone en la fecha



def CrearLiquidacion(recibos:list, siniestros:list, serial:int)->list:
    recibos
    siniestros
    serial
    while True:
        fecha_liquidacion=input("Detalle la fecha de liquidación en el siguiente formato (DD/MM/AAAA) en el año 2025>>> ")
        if len(fecha_liquidacion)==10 and fecha_liquidacion[2]=='/' and fecha_liquidacion[5]=='/' and fecha_liquidacion[:2].isdigit() and fecha_liquidacion[3:5].isdigit() and fecha_liquidacion[6:].isdigit():
            fechaLiq=fecha_liquidacion.split('/')
            listaAux=[]
            for elto in fechaLiq:
                elto=int(elto)
                listaAux.append(elto)
            if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]==2025:
                print("Fecha de liquidación válida. Registrando...")
                break
        else:
            print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
            continue
    #generación seriada:
    nro_liquidacion=fecha_liquidacion[6:]+'-'+str(serial) #se coge del programa principal el seriado incrementado y se añade al año de la liquidación
    estado_liquidacion='Abierta'
    #1º
    importe_recibos_cobrados=0 #inicialización a 0 y vamos a barrer en breves
    for elto in recibos: #entiendo que para barrer en busca de cobrados hay que moverse por recibos - iteramos y buscamos coincidencias | si las hay, mandamos a incrementar
        for subelto in elto:
            if (subelto['estado_recibo']=='C' or subelto['estado_recibo'=='CB']) and subelto['estado_liquidacion']=='Pendiente':
                importe_recibos_cobrados+=subelto['importe_cobrar']
    lista_recibos_liquidar=[] #inicializamos una lista vacía
    #se obtiene filtrando aquellos recibos que han sido cobrados por la correduría, 
    # pero que aún no han sido liquidados a la aseguradora.
    for elto in recibos: 
        for subelto in elto:
            if (subelto['estado_recibo']=='C' or subelto['estado_recibo'=='CB']) and subelto['estado_liquidacion']=='Pendiente':
                elementos_liquidar=(subelto['nro_poliza'], subelto['id_recibo'])
                lista_recibos_liquidar.append(elementos_liquidar)
    #2º
    importe_recibos_baja=0
    for elto in recibos:
        for subelto in elto:
            if subelto['estado_recibo']=='B' and subelto['estado_liquidacion']=='Pendiente':
                importe_recibos_baja+=subelto['importe_pagar']
    lista_recibos_baja=[]
    for elto in recibos:
        for subelto in elto:
            if subelto['estado_recibo']=='B' and subelto['estado_liquidacion']=='Pendiente':
                elementos_liquidar_baja=(subelto['nro_poliza'], subelto['id_recibo'])
                lista_recibos_baja.append(elementos_liquidar_baja)
    #3º 
    importe_siniestros_pagados=0 #Ahora nos movemos por siniestros y bajo las condiciones de PA y P en estado_siniestro y estado_liquidacion, extraemos el importe_pagar e incrementamos
    for elto in siniestros:
        for subelto in elto:
            if subelto['estado_siniestro']=='PA' and subelto['estado_liquidacion']=='P':
                importe_siniestros_pagados+=subelto['importe_pagar']
    lista_siniestros_pagados=[]
    for elto in siniestros:
        for subelto in elto:
            if subelto['estado_siniestro']=='PA' and subelto['estado_liquidacion']=='P':
                elementos_siniestros_liquidar=(subelto['nro_poliza'], subelto['id_siniestro'])
                lista_siniestros_pagados.append(elementos_siniestros_liquidar)
    #CALCULO DE LIQUIDACION ( (1) - (3), (2) )
    importe_liquidacion=((importe_recibos_cobrados-importe_siniestros_pagados), importe_recibos_baja) 
    dLiquidacion={'nro_liquidacion': nro_liquidacion,
                  'fecha_liquidacion': fecha_liquidacion,
                  'estado_liquidacion': estado_liquidacion,
                  'importe_recibos_cobrados': importe_recibos_cobrados,
                  'lista_recibos_liquidar': lista_recibos_liquidar,
                  'importe_recibos_baja': importe_recibos_baja,
                  'lista_recibos_baja': lista_recibos_baja,
                  'importe_siniestros_pagados': importe_siniestros_pagados,
                  'lista_siniestros_pagados': lista_siniestros_pagados,
                  'importe_liquidacion': importe_liquidacion}
    print(f"Se ha creado una liquidación con número identificador {nro_liquidacion}.")
    liquidacion=[]
    liquidacion.append(dLiquidacion)
    return liquidacion

##El siguiente paso ahora es cerrar la liquidación, lo que significa mandar un mensaje al usuario para que confirme y, además, 
#se debe hacer antes del return

def CerrarLiquidacion(recibos:list, siniestros:list, liquidaciones:list)->list:
    while True:
        for elto in liquidacion:
            for subelto in elto:
                for clave, valor in subelto.items():
                    print(f"- {clave}: {valor}")
        confirmar=input("¿Son estos datos correctos? Se va a proceder al cierre de la liquidación. Escriba s/n >>> ").lower()
        if confirmar == 's':
            print("Cerrando la liquidación.\nCambiando los estados de los recibos y los siniestros implicados...")
            for elto in recibos:
                for subelto in elto:
                    if (subelto['estado_recibo']=='C' or subelto['estado_recibo'=='CB'] or subelto['estado_recibo']=='B') and subelto['estado_liquidacion']=='Pendiente':
                        subelto['estado_liquidacion']='Liquidado'
            for elto in siniestros:
                for subelto in elto:
                    if subelto['estado_siniestro']=='PA' and subelto['estado_liquidacion']=='P':
                        subelto['estado_liquidacion']=='L'
            
            liquidacion=[]
            print("Todos los estados modificados.\nLiquidación cerrada correctamente.")