#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
def CrearLiquidacion(recibos:list, siniestros:list, serial:int)->list:
    '''Funcion que permite crear una liquidacion mediante la barrida de los datos de siniestros y recibos
    respetando las normas impuestas por el ejc'''
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
def ModificarLiquidacion(liquidacion:list)->list:
    ''' 
    Funcion que permite cambiar la fecha de la liquidacion
    '''
    print("Estas son todas las liquidaciones registradas hasta ahora: ")
    PROHIBIDOS=[]
    LIQUIDACIONES=[]
    print("Estas son todas las modificaciones registradas")
    for elto in liquidacion:
        for subelto in elto:
            print(f"- {subelto['nro_liquidacion']}")
    for elto in liquidacion: #LAS QUE ESTÁN PROHIBIDAS SE USAN AL VALIDAR
        for subelto in elto:
            if subelto['estado_liquidacion']=='Liquidado':
                PROHIBIDOS.append(subelto['nro_liquidacion'])
            else:
                LIQUIDACIONES.append(subelto['nro_liquidacion'])
    print("Liquidaciones NO MODIFICABLES en el registro (cerradas)")
    for elto in PROHIBIDOS:
        print(elto)
    print("Liquidaciones disponibles a modificar: ")
    for elto in LIQUIDACIONES:
        print(elto)
    seleccionLiquidacion=input("Seleccione entre las liquidaciones disponibles / Solo es posible modificar la fecha>>> ")
    if seleccionLiquidacion in LIQUIDACIONES:
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
                    for elto in liquidacion:
                        for subelto in elto:
                            if subelto['nro_liquidacion']==seleccionLiquidacion:
                                subelto['fecha_liquidacion']=fecha_liquidacion
                                return liquidacion
            else:
                print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                continue
    elif seleccionLiquidacion in PROHIBIDOS:
        print("Error. Esta póliza está cerrada y no es modificable. Volviendo al menú principal.")
        return liquidacion
    else:
        print("No se ha encontrado el id de la liquidación. Volviendo al menú principal.")
        return liquidacion  
##El siguiente paso ahora es cerrar la liquidación, lo que significa mandar un mensaje al usuario para que confirme y, además, 
#se debe hacer antes del return
def CerrarLiquidacion(recibos:list, siniestros:list, liquidaciones:list)->list:
    '''Funcion que permite crear un cierre de liquidacion teniendo en cuenta las 
    normas del ejercicio y basandonos en estados lógicos. Cuando se cierra, tambien se actualiza
    el estado_liq en recibos y siniestros'''
    liqEncontrada=False
    while True:
        for elto in liquidaciones:
            for subelto in elto:
                for clave, valor in subelto.items():
                    print(f"- {clave}: {valor}")
        confirmar=input("¿Son estos datos correctos? Se va a proceder al cierre de la liquidación. Escriba s/n >>> ").lower()
        if confirmar == 's':
            print("Cerrando la liquidación.\nCambiando los estados de los recibos y los siniestros implicados...")
            numLiq=input("Seleccione un nº de liquidación al que quiera acceder: ")
            for elto in liquidaciones:
                for subelto in elto:
                    if subelto['nro_liquidacion']==numLiq:
                        liqEncontrada=True
                        subelto['estado_liquidacion']='Liquidado' #cambio de estado a liquidado, pero ahora toca barrer para modificar en el resto de listas
                        fecha_liquidacion = subelto['fecha_liquidacion']  #COGER fecha de liquidacion

            if liqEncontrada:
                for elto in liquidaciones: #extraigo los datos de mi liquidación que quiero cerrar
                    for subelto in elto:
                        if subelto['nro_liquidacion']==numLiq:
                            recibosLiquidar=subelto['lista_recibos_liquidar']
                            listaRecibosBaja=subelto['lista_recibos_baja']
                            siniestrosPagados=subelto['lista_siniestros_pagados']
                
                print(recibosLiquidar)
                print(listaRecibosBaja)
                print(siniestrosPagados)
                for elemento in recibosLiquidar:
                    for elto in recibos:
                        for subelto in elto:
                            if subelto['id_recibo']==elemento[1]: #este funcionamiento teorico es correcto y comprobado por el IDLE de Python
                                subelto['estado_liquidacion']='Liquidado'
                                subelto['fecha_liquidacion']=fecha_liquidacion#AÑADIDO

                for elemento in listaRecibosBaja:
                    for elto in recibos:
                        for subelto in elto:
                            if subelto['id_recibo']==elemento[1]:
                                subelto['estado_liquidacion']='Liquidado'
                                subelto['fecha_liquidacion']=fecha_liquidacion#AÑADIDO
                for elemento in siniestrosPagados:
                    for elto in siniestros:
                        for subelto in elto:
                            if subelto['id_siniestro']==elemento[1]:
                                subelto['estado_liquidacion']='L'
                                subelto['fecha_liquidacion']=fecha_liquidacion #AÑADIDO #se establece entonces el estado de Liquidado donde antes estaba en pendiente
                return recibos, siniestros, liquidaciones
            else:
                print("Error. No se ha encontrado el id de la liquidación a cerrar.")
                return recibos, siniestros, liquidaciones
        elif confirmar == 'n':
            print("Volviendo al menu principal.")
            return recibos, siniestros, liquidaciones
        else:
            print("Seleccione correctamente entre s/n")

