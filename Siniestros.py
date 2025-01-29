#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín


##Teniendo en cuenta que deben de existir las pólizas para trabajar con los siniestros, primeramente el usuario se verá forzado a al menos introducir
#una póliza en el sistema.
from Utilidades import ComprobarMatricula
def CrearSiniestro(id_siniestro: str, polizas:list) -> list:
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
    eleccion=int(input(">>>"))
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
def ModificarSiniestro(siniestros:list) -> list:
    #barrer toda la lista de siniestros, comprobar que el id introducido sea igual que el del usuario y modificar según lo barrido:
    ID=[]
    CAMPOS=[]
    if not siniestros:
        print("Error. Debe existir al menos un siniestro para poder proceder a su modificación.")
        return siniestros
    print("Estos son los identificadores asociados a los siniestros que existen: ")                    
    for elto in siniestros:
        for subelto in elto:
            print(f"id_siniestro: {subelto['id_siniestro']}")
            ID.append(subelto['id_siniestro'])
    print()
    modificar=input("Escriba uno de los identificadores listados >>> ")
    if modificar in ID:
        #Modificamos los datos según el que hemos introducido como usuarios
        for elto in siniestros:
            for subelto in elto:
                if subelto['id_siniestro']==modificar:#Nos metemos dentro del seleccionado
                 pass


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
        




        





