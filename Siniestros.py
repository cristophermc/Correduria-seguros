#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
from Utilidades import ComprobarMatricula
def CrearSiniestro(id_siniestro:str, polizas:list) -> list:
    lista=[]
    print("Primero seleccione un ID de póliza sobre la cual formalizar el siniestro.")
    print("Escoja el número de póliza sobre el cual crear un recibo asociado.")
    for elto in polizas:
        for subelto in elto:
            print(f"nro_pol: {subelto['nro_poliza']}", end=' ')
    IDpolizas=[]
    for elto in polizas:
        for subelto in elto:
            IDpolizas.append(subelto['nro_poliza'])
    print()
    eleccion=input(">>>")
    # global nro_poliza
    if eleccion in IDpolizas:
        for elto in polizas:
            for subelto in elto:
                if subelto['nro_poliza']==eleccion:
                    print(f"Encontrado y emparejado. Identificador de la póliza: {eleccion}")
                    print("Cargando otros datos...")
                    for elto in polizas:
                        for subelto in elto:
                            if subelto['nro_poliza']==eleccion:
                                if subelto['estado_poliza']=='Baja' and subelto['estado_poliza']=='PteCobro':
                                    print("Ha ocurrido un error. Se ha detectado que la póliza a la que se quiere asociar el siniestro\nestá de baja o pendiente de cobro. No se puede llevar a cabo esta operación. Volviendo al menú principal.")
                                    return lista
                                else:

                                    print()
                                        #descripcion: detalle de lo ocurrido en el siniestro
                                    print("Se incluye una descripción de lo ocurrido en el siniestro.\nPor favor, expláyese a placer y cuando termine pulse ENTER.")
                                    descripcion=input(">>> ")
                                    #matricula_contrario: la matrícula del vehículo contrario involucrado en el siniestro
                                    print()
                                    while True:
                                        print("Para seguir registrando el siniestro, se debe reconocer la matrícula del vehículo contrario.\nIntroduzca la matrícula del contrario.")
                                        matricula_contrario=input('>>> ')
                                        if ComprobarMatricula(matricula_contrario):
                                            print("Datos de matrícula del vehículo contrario introducidos y validados correctamente.")
                                            break
                                        else:
                                            print("Los datos de la matrícula son incorrectos. Por favor, introduzca nuevamente la matrícula y asegúrese de que cumpla el formato de\nvalidez presente en la DGT.")
                                    #compañia_contrario: puede ser la misma que la del siniestrado.
                                    print()
                                    print("Cargando datos...")
                                    while True:
                                        print("Introduzca la compañía aseguradora del vehículo contrario.")
                                        compañia_contrario=input('>>> ')
                                        if compañia_contrario!='':
                                            print("Datos concernientes a la compañía del veh. contrario introducidos correctamente.")
                                            break
                                        elif compañia_contrario	in '@!¡.-,_`%&/()#~€¬$' and '0123456789':
                                            print("Error. Los datos introducidos no pueden estar en la secuencia de caracteres '@!¡.-,_`%&/()#~€¬$' ni en la serie numérica decimal.")
                                        else:
                                            print("Error al introducir los datos. No se permiten espacios en blancos, símbolos especiales o números.")    
                                    print()
                                    print()
                                    print("Cargando datos...")
                                    #nro_poliza_contrario.
                                    while True:
                                        print("Introduzca ahora el número de póliza del vehículo contrario. ")
                                        try:
                                            nro_poliza_contrario=int(input('>>> '))
                                        except:
                                            print("Error. Los caracteres solo pueden ser numéricos.")
                                        else:
                                            if nro_poliza_contrario>0 and nro_poliza_contrario <=10000000:
                                                print("Datos correctamente introducidos en el sistema.")
                                                break
                                            else:
                                                print("Error. Los datos solo pueden estar sezgados en números >0 y <10000000.")
                                    print()
                                    print()
                                    print("Cargando datos de abono...")
                                    #importe_pagar: el importe total que ha salido la reparación del siniestro y que se abona al cliente.
                                    while True:
                                        print("Introduzca el importe total que saldrá la reparación del siniestro y que se abona al cliente: ")
                                        try:
                                            importe_pagar=int(input('>>> '))
                                        except:
                                            print("Error. Los caracteres solo pueden ser numéricos.")
                                        else:
                                            if importe_pagar>0 and importe_pagar <=10000000:
                                                print("Datos correctamente introducidos en el sistema.")
                                                break
                                            else:
                                                print("Error. Los datos solo pueden estar sezgados en números >0 y <10000000.")
                                    #estado_siniestro
                                    estados=('P', 'C', 'PP', 'PA')
                                    while True:
                                        print("Un siniestro puede estar en cuatro estados:\n• Pendiente de confirmar (P): El siniestro no ha sido confirmado por la compañía contraria.\n• Confirmado (C): El siniestro ha sido confirmado por la compañía contraria.\n• Pendiente de Pago (PP): El siniestro no ha sido abonado todavía.\n• Pagado (PA): El siniestro ha sido abonado correctamente.")
                                        print()
                                        print(f"Introduzca la letra que corresponde al estado del siniestro - |AYUDA| {estados}")
                                        estado_siniestro=input(">>> ")
                                        if estado_siniestro in estados:
                                            print("Datos introducidos correctamente en el sistema.")
                                            break
                                        else:
                                            print("Error. Introduzca correctamente los datos con el formato específico.")
                                    print()
                                    print()
                                    print("Cargando datos...")
                                    #fecha_abono
                                    while True:
                                        if estado_siniestro!='PA':
                                            print("El siniestro no puede tener una fecha de abono al no haber sido pagado todavía.")
                                            fecha_abono=''
                                            break
                                        elif estado_siniestro=='PA':
                                            fecha_abono=input("Detalle la fecha de abono del siniestro en el siguiente formato (DD/MM/AAAA) >>> ")
                                            if len(fecha_abono)==10 and fecha_abono[2]=='/' and fecha_abono[5]=='/' and fecha_abono[:2].isdigit() and fecha_abono[3:5].isdigit() and fecha_abono[6:].isdigit():
                                                fechaAb=fecha_abono.split('/')
                                                listaAux=[]
                                                for elto in fechaAb:
                                                    elto=int(elto)
                                                    listaAux.append(elto)
                                                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                                    print("Fecha de abono válida. Registrando...")
                                                    break
                                            else:
                                                print("Error. La fecha de abono no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                                continue    
                                    print()
                                    print()
                                    print("Cargando datos de liquidación...")
                                    #estado_liquidacion
                                    estadosLiquidacion=('P','L')
                                    while True:
                                        print("Un siniestro puede estar a su vez en dos estados más:\n• Pendiente (P): El siniestro no ha sido abonado a la compañía aseguradora.\n• Liquidado (L): El recibo ha sido abonado o dado de baja a la compañía.")
                                        print(f"Introduzca la letra que corresponde al estado de liquidación del siniestro - |AYUDA| {estadosLiquidacion}")
                                        estado_liquidacion=input(">>> ")
                                        if estado_liquidacion in estadosLiquidacion:
                                            print("Datos introducidos correctamente en el sistema.")
                                            break
                                        else:
                                            print("Error. Introduzca correctamente los datos con el formato específico.")
                                    print()
                                    print()
                                    while True:
                                        fecha_liquidacion=input("Detalle la fecha de liquidación en el siguiente formato (DD/MM/AAAA) >>> ")
                                        if len(fecha_liquidacion)==10 and fecha_liquidacion[2]=='/' and fecha_liquidacion[5]=='/' and fecha_liquidacion[:2].isdigit() and fecha_liquidacion[3:5].isdigit() and fecha_liquidacion[6:].isdigit():
                                            fechaLiq=fecha_liquidacion.split('/')
                                            listaAux=[]
                                            for elto in fechaLiq:
                                                elto=int(elto)
                                                listaAux.append(elto)
                                            if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                                print("Fecha de liquidación válida. Registrando...")
                                                break
                                            else:
                                                print("Error. La fecha de liquidación no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                                continue    
                                    dSiniestro={'id_siniestro': id_siniestro,
                                                'nro_poliza':eleccion,
                                                'descripcion': descripcion,
                                                'matricula_contrario':matricula_contrario,
                                                'compañia_contrario': compañia_contrario,
                                                'nro_poliza_contrario':nro_poliza_contrario,
                                                'importe_pagar':importe_pagar,
                                                'estado_siniestro':estado_siniestro,
                                                'fecha_abono':fecha_abono,
                                                'estado_liquidacion':estado_liquidacion,
                                                'fecha_liquidacion':fecha_liquidacion}
                                    print(f"Siniestro creado para el nº de póliza {eleccion} con identificador {id_siniestro}")
                                    lista.append(dSiniestro)
                                    return lista
    else:
        print("No se puede acceder a un identificador de póliza escrito.")
        return id_siniestro, polizas   
def ModificarSiniestro(siniestros:list) -> list:
    #barrer toda la lista de siniestros, comprobar que el id introducido sea igual que el del usuario y modificar según lo barrido:
    ID=[]
    CAMPOS=[]
    if not siniestros:
        print("Error. Debe existir al menos un siniestro para poder proceder a su modificación.")
        return siniestros
    for elto in siniestros: #nos creamos CAMPOS para identificar y cotejar los datos más rapidamente y de forma segura
        for subelto in elto:
            for clave in subelto.keys():
                if clave!='id_siniestro' and clave not in CAMPOS:
                    CAMPOS.append(clave)
    print("Estos son los identificadores asociados a los siniestros que existen: ")                    
    for elto in siniestros:
        for subelto in elto:
            print(f"id_siniestro: {subelto['id_siniestro']}")
            ID.append(subelto['id_siniestro'])
    print()
    modificar=input("Escriba uno de los identificadores listados >>> ")
    if modificar in ID:
        print(f"Se ha seleccionado el ID: {modificar}")
        while True:
            print("Campos disponibles a seleccionar:")
            for elto in CAMPOS:
                print(f"- {elto}", end=' ')
                print()
            campo=input("Seleccione uno de los campos a continuación: ")
            if campo in CAMPOS: #Si la elección se encuentra en uno de los campos: 
                match campo:
                    case 'nro_poliza': #PREGUNTAR A REINALDO SI ESTO SE PUEDE HACER Y COMO IMPLEMENTARLO
                        pass
                    case 'descripcion':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es la descripción anterior\n\n{subelto['descripcion']}")
                            nuevaDescripcion=input("Escriba una nueva descripcion >>> ")
                            if nuevaDescripcion != '':
                                for elto in siniestros:
                                    for subelto in elto:
                                        if subelto['id_siniestro']==modificar:
                                            subelto['descripcion']=nuevaDescripcion
                                            print("Descripción modificada.")
                                            return siniestros
                            else:
                                print("La descripción no puede estar vacía. Por favor, introduzca una descripción nuevamente.")
                    case 'matricula_contrario':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es la matrícula del vehículo contrario anterior\n\n{subelto['matricula_contrario']}")
                            nuevaMatriculaContrario=input("Introduzca una nueva matrícula del contrario >>> ")
                            if ComprobarMatricula(nuevaMatriculaContrario):
                                for elto in siniestros:
                                    for subelto in elto:
                                        if subelto['id_siniestro']==modificar:
                                            subelto['matricula_contrario']=nuevaMatriculaContrario
                                            print("Matrícula modificada.")
                                            return siniestros
                            else:
                                print("Esa matrícula no es válida. Introduzca otra.")
                                continue
                                        
                    case 'compañia_contrario':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es la compañía del vehículo contrario anterior\n\n{subelto['compañia_contrario']}")
                            nuevaCompañia=input("Introduzca una nueva compañia >>> ")
                            if nuevaCompañia != '':
                                for elto in siniestros:
                                    for subelto in elto:
                                        if subelto['id_siniestro']==modificar:
                                            subelto['compañia_contrario']=nuevaCompañia
                                            print("Compañia contraria modificada.")
                                            return siniestros
                            else:
                                print("La compañia no puede quedar vacía.")
                                continue
                    case 'nro_poliza_contrario':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es el numero de poliza contrario anterior\n\n{subelto['nro_poliza_contrario']}")
                                        nuevoNumeroPoliza=input("Introduzca un nuevo numero de poliza >>> ")
                                        for elto in siniestros:
                                            for subelto in elto:
                                                if subelto['id_siniestro']==modificar:
                                                    subelto['nro_poliza_contrario']=nuevoNumeroPoliza
                                                    print("Poliza contraria modificada.")
                                                    return siniestros                                
                    case 'importe_pagar':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es el importe a pagar anterior\n\n{subelto['nro_poliza_contrario']}")
                            try:
                                nuevoImportePagar= float(input("Introduzca un nuevo importe a pagar >>> "))
                            except:
                                print("Error. El importe a pagar debe ser un valor numérico.")
                            else:
                                if nuevoImportePagar>0 and nuevoImportePagar <10000000:
                                    for elto in siniestros:
                                        for subelto in elto:
                                            if subelto['id_siniestro']==modificar:
                                                subelto['importe_pagar']=nuevoImportePagar
                                                print("Importe a pagar modificado.")
                                                return siniestros
                                else:
                                    print("Error. El importe a pagar debe estar entre 0 y 10000000 sin incluir ambos.")                                
                    case 'estado_siniestro':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es el estado del siniestro anterior\n\n{subelto['estado_siniestro']}")
                            estados=('P', 'C', 'PP', 'PA')
                            nuevoEstadoSin=input(f"Introduzca un nuevo estado entre: {estados} >>> ").upper()
                            if nuevoEstadoSin != '':
                                if nuevoEstadoSin in estados:
                                    for elto in siniestros:
                                        for subelto in elto:
                                            if subelto['id_siniestro']==modificar:
                                                subelto['estado_siniestro']=nuevoEstadoSin
                                                print("Estado del siniestro modificado.")
                                                return siniestros
                                else:
                                    print("La selección debe estar entre las opciones cotejadas.")
                            else:
                                print("La información del estado no puede estar vacía.")
                                continue
                    case 'fecha_abono':
                      while True:
                        for elto in siniestros:
                            for subelto in elto:
                                if subelto['id_siniestro']==modificar:
                                    print(f"Esta es la antigua fecha de abono {subelto['fecha_abono']}")
                        nueva_fecha_abono=input("Detalle la nueva fecha de abono en el siguiente formato (DD/MM/AAAA) >>> ")
                        if len(nueva_fecha_abono)==10 and nueva_fecha_abono[2]=='/' and nueva_fecha_abono[5]=='/' and nueva_fecha_abono[:2].isdigit() and nueva_fecha_abono[3:5].isdigit() and nueva_fecha_abono[6:].isdigit():
                            fechaAb=nueva_fecha_abono.split('/')
                            listaAux=[]
                            for elto in fechaAb:
                                elto=int(elto)
                                listaAux.append(elto)
                                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                    print("Fecha de liquidación válida. Registrando...")
                                    for elto in siniestros:
                                        for subelto in elto:
                                            if elto['id_siniestro']==modificar:
                                                elto['fecha_abono']=nueva_fecha_abono
                                                print("Fecha de abono modificada.")
                                                return siniestros
            
                        else:
                            print("Error. La fecha de abono no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                            continue  
                    case 'estado_liquidacion':
                        for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es el estado de la liquidacion anterior\n\n{subelto['estado_liquidacion']}")
                        estadosLiquidacion=('P','L')
                        while True:
                            print("Un siniestro puede estar a su vez en dos estados más:\n• Pendiente (P): El siniestro no ha sido abonado a la compañía aseguradora.\n• Liquidado (L): El recibo ha sido abonado o dado de baja a la compañía.")
                            print(f"Introduzca la letra que corresponde al estado de liquidación del siniestro - |AYUDA| {estadosLiquidacion}")
                            nuevo_estado_liquidacion=input(">>> ")
                            if nuevo_estado_liquidacion in estadosLiquidacion:
                                print("Datos introducidos correctamente en el sistema.")
                                for elto in siniestros:
                                    for subelto in elto:
                                        if subelto['id_siniestro']==modificar:
                                            subelto['estado_liquidacion'] = nuevo_estado_liquidacion
                            
                            else:
                                print("Error. Introduzca correctamente los datos con el formato específico.")
                    case 'fecha_liquidacion':
                        while True:
                            for elto in siniestros:
                                for subelto in elto:
                                    if subelto['id_siniestro']==modificar:
                                        print(f"Esta es la antigua fecha de liquidacion {subelto['fecha_liquidacion']}")
                            nueva_fecha_liq=input("Detalle la nueva fecha de liquidacion en el siguiente formato (DD/MM/AAAA) >>> ")
                            if len(nueva_fecha_liq)==10 and nueva_fecha_liq[2]=='/' and nueva_fecha_liq[5]=='/' and nueva_fecha_liq[:2].isdigit() and nueva_fecha_liq[3:5].isdigit() and nueva_fecha_liq[6:].isdigit():
                                fechaLq=nueva_fecha_liq.split('/')
                                listaAux=[]
                                for elto in fechaLq:
                                    elto=int(elto)
                                    listaAux.append(elto)
                                    if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                        print("Fecha de liquidación válida. Registrando...")
                                        for elto in siniestros:
                                            for subelto in elto:
                                                if elto['id_siniestro']==modificar:
                                                    elto['fecha_liquidacion']=nueva_fecha_liq
                                                    print("Fecha de liquidación modificada.")
                                                    return siniestros
                                    else:
                                        print("Error en el formato.")
                            else:
                                print("Error en el formato.")

        #Modificamos los datos según el que hemos introducido como usuarios
        # for elto in siniestros:
        #     for subelto in elto:
        #         if subelto['id_siniestro'] == modificar:#Nos metemos dentro del seleccionado
        #             pass
def EliminarSiniestro(siniestros:list)->list:
    #Barrer la lista de siniestros que hay y comprobar:
    '''No se puede eliminar un siniestro vigente, 
    independientemente de su estado.
    
    Una vez que el siniestro pasa al estado 
    Pagado y es liquidado con la aseguradora, 
    deja de ser considerado vigente.
    '''
    ID=[]
    if not siniestros:
        print("Error. Debe existir al menos un siniestro para poder proceder a su eliminación.")
        return siniestros
    while True:
        print("Estos son los identificadores asociados a los siniestros que existen: ")                    
        for elto in siniestros:
            for subelto in elto:
                print(f"id_siniestro: {subelto['id_siniestro']}")
                ID.append(subelto['id_siniestro'])
        print()
        eliminar=input("Escriba uno de los identificadores listados >>> ")
        if eliminar in ID:
            #Checkeamos las condiciones para poder borrar (PA y L):
            for elto in siniestros:
                for subelto in elto:
                    if subelto['id_siniestro']==eliminar: #Accedemos al que hemos introducido como usuarios
                        if subelto['estado_siniestro']=='PA' and subelto['estado_liquidacion']=='L':
                            siniestros.remove(elto)
                            print("Siniestro eliminado con éxito.")
                            print("Volviendo al menú principal.")
                            return siniestros
                        else:
                            print("Error. Solo se puede eliminar un siniestro que no esté vigente y liquidado.")
                            return siniestros
            else:
                print("Error. El siniestro al que se trata acceder no se encuentra registrado.")
        




        





