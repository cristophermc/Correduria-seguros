#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
from Utilidades import ValidarDocumento
from Utilidades import ComprobarMatricula
from Utilidades import ComprobarIBAN
def CrearPoliza(nro_poliza:int, tomadores:list, banlist:list) -> list:
    '''Función que permite formalizar una póliza mediante diferentes bucles con sus respectivas validaciones.
    Se contemplan las matrículas de la DGT normales y las de ciclomotores traídas desde el archivo modular de 
    utilidades. Además, se implementa el algoritmo de validación de documentación NIF/NIE/CIF y el algoritmo del IBAN'''
    lista=[]
    listaCoberturas=[]
    tipoVehiculo=('ciclomotor','moto', 'turismo','furgoneta','camion')
    coberturasDisponibles=('RC', 'RL', 'INC', 'RB', 'TR')
    cobertura=()
    documentosDisponibles=[]

    print("Bienvenido al asistente creador de pólizas.\nRellene adecuadamente los siguientes datos:")
    print()
    for elto in tomadores:
        for subelto in elto:
            documentosDisponibles.append(subelto['id_tomador'])
    while True:
        print("Mostrando documentos registrados en el sistema")
        print(documentosDisponibles)
            
            #se solicita el id del tomador
        id_tomador = input("Escriba el NIF | NIE | CIF >>> ")

            #Validamos el id a ver si ya está en la banlist
        if id_tomador in banlist: #Se checkea primero si está en la lista de id ya registrados
            print("Error. El id ya se encuentra registrado en la base de datos. Pruebe con otro.")
            continue
            #en este paraguas cogemos y rompemos el bucle infinito
        elif id_tomador in documentosDisponibles and id_tomador not in banlist:
            if ValidarDocumento(id_tomador):
                print("Documento validado correctamente.")
                break
            else:
                print("Error. El tipo de documento no es válido según las normas de validación estándares en España.\nEscriba nuevamente un valor para NIF | NIE | CIF\n\n")

        elif id_tomador not in documentosDisponibles:
            print(f"El ID {id_tomador} no figura en la base de datos como tomador registrado. Seleccione un ID válido de los previamente registrados.")
        
        else:
            print(f"Error inesperado. Intente nuevamente. Detalles:\nID ingresado: {id_tomador}\nIDs disponibles: {documentosDisponibles}\nBanlist actual: {banlist}")
    while True: #---------datos del vehiculo
        matricula=input("Escriba la matrícula del vehículo que requiere registro | Ejemplos -> (0418UTE / C0844TE)>>> ").upper()
        if ComprobarMatricula(matricula):
            break
        else:
            continue
    while True:
        tipo=input(f"Seleccione ahora un tipo de vehículo que quiera registrar - datos disponibles > {tipoVehiculo} >>> ").lower()
        if tipo in tipoVehiculo:
            print(f"Vehículo de tipo {tipo} seleccionado.")
            break
        else:
            print("Error. Seleccione correctamente entre la lista de tipos de vehículos disponibles para registrar.")
    while True:
        marca=input("Escriba la marca que representa al vehículo >>> ")
        if marca !='':
            print("Marca seleccionada correctamente.")
            break
        else:
            print("Error. No se admiten valores nulos o vacíos en el registro de marcas de un vehículo.")
    while True:
        modelo=input("Escriba el modelo que acompaña a la marca del vehículo >>> ")
        if modelo !='':
            print("Modelo seleccionado correctamente.")
            break
        else:
            print("Error. No se admiten valores nulos o vacíos.")
    while True:
        tipoFuncionamiento=('combustion', 'electrico', 'mixto')
        funcionamiento=input(f"Selecciona un valor correspondiente al funcionamiento del vehículo figurado en la siguiente secuencia - {tipoFuncionamiento} >>> ").lower()
        if funcionamiento in tipoFuncionamiento:
            print("Dato proporcionado con éxito.")
            break
        else:
            print("Error. Seleccione adecuadamente entre la tupla figurante.")
    datos_vehiculo=(tipo, marca, modelo, funcionamiento)
    print(f"En la empresa tenemos para contratar las siguientes coberturas - {coberturasDisponibles} \nTranscripción\nRC - Responsabilidad Civil \nRL - Rotura de lunas\nINC - Incendio\nRB - Robos\nTR - Seguro a todo riesgo")
    print("Ud. puede contratar más de una cobertura.")
    trContratado=False
    cobContratadas=[]
    estandar=False
    while True: #coberturas disponibles 
        eleccionCobertura=input(f"Escriba su elección entre {coberturasDisponibles} o el caracter @ para parar: ")
        if eleccionCobertura != '@' and eleccionCobertura in coberturasDisponibles and eleccionCobertura not in listaCoberturas:
            if eleccionCobertura == 'TR' and not trContratado:
                franquicia = input(f"Escriba la franquicia colaboradora asociada a la cobertura >>> ").upper()
                valor_franquicia = ('TR', franquicia)
                listaCoberturas.append(valor_franquicia)
                cobContratadas.append(eleccionCobertura)
                trContratado = True
            elif eleccionCobertura == 'TR' and trContratado:
                print("Error. La cobertura 'TR' ya ha sido contratada.")
            elif eleccionCobertura in coberturasDisponibles and eleccionCobertura != 'TR':
                listaCoberturas.append(eleccionCobertura)
                cobContratadas.append(eleccionCobertura)
                print(f"Cobertura añadida: {eleccionCobertura}")
        elif eleccionCobertura == '@':
            if not listaCoberturas:
                print("Por defecto, ud. tiene contratada la cobertura RC.")
                estandar=True
                break
            else:
                break
        else:
            print(f"Error. Escriba una cobertura de entre las disponibles en el sistema y que no haya sido contratada. \n-> C. CONTRATADAS >>> {cobContratadas}")
    if not estandar:
        cobertura=tuple(listaCoberturas)
    if estandar:
        cobertura='RC'
    idConductor=[]
    print("A continuación se detallan los datos pertenecientes a los conductores del vehículo registrado.")
    while True: #documentacion de la persona conductora
        while True:
            nifnie=input("Escriba el DNI/NIE de la persona física conductora del vehículo >>> ")
            if ValidarDocumento(nifnie):
                print("DNI/NIE validado correctamente.")
                idConductor.append(nifnie)
                break
            else:
                print("Error. El tipo de documento no es válido según las normas de validación estándares en España.\nEscriba nuevamente un valor para DNI/NIE.\n\n")
        while True: #fecha de nacimiento del conductor del veh
            fecha_nacimiento=input("Detalle la fecha de nacimiento del conductor en el siguiente formato (DD/MM/AAAA) >>> ")
            if len(fecha_nacimiento)==10 and fecha_nacimiento[2]=='/' and fecha_nacimiento[5]=='/' and fecha_nacimiento[:2].isdigit() and fecha_nacimiento[3:5].isdigit() and fecha_nacimiento[6:].isdigit():
                fechaNac=fecha_nacimiento.split('/')
                listaAux=[]
                for elto in fechaNac:
                    elto=int(elto)
                    listaAux.append(elto)
                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2006:
                    print("Fecha de nacimiento válida. Registrando...")
                    idConductor.append(fecha_nacimiento)
                    break
            else:
                print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                continue
        while True: #tipos de carné que existen, lo almacenamos en tupla
            tiposCarne=('AM','A1','A2','A','B1','B','C1','D1','D','BE','C1E','CE','D1E','DE')
            tipo_carnet=input(f"Seleccione un carné de entre el siguiente catálogo - {tiposCarne} >>> ")
            if tipo_carnet in tiposCarne:
                print("Tipo de carné de conducir seleccionado correctamente.")
                idConductor.append(tipo_carnet)
                break
            else:
                print("Error. Seleccione correctamente un tipo de carné de conducir.")
        while True: #emisión del carné - fecha
            fecha_carnet=input("Establezca una fecha de emisión del carné con el formato DD/MM/AAAA >>> ")
            if len(fecha_carnet)==10 and fecha_carnet[2]=='/' and fecha_carnet[5]=='/' and fecha_carnet[:2].isdigit() and fecha_carnet[3:5].isdigit() and fecha_carnet[6:].isdigit():
                fechaCarnet=fecha_carnet.split('/')
                listaAux=[]
                for elto in fechaCarnet:
                    elto=int(elto)
                    listaAux.append(elto)
                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025: #DETECCIÓN DE ERRORES / ERROR
                    print("Fecha de emisión del carné de conducir válida. Registrando...")
                    idConductor.append(fecha_carnet)
                    break
                else:
                    print("Error. La fecha de emisión del carné de conducir introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                    continue
            else:
                print("Error. La fecha de emisión del carné de conducir introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                continue
        break

    id_conductor=tuple(idConductor)
    estado_poliza=''
    print("Cargando datos de actualización de estado de póliza...\nLa póliza puede solamente estar en uno de los siguientes estados:\nCobrada\nPteCobro\nBaja")
    while True:
        epeleccion=input("Escoja entre (C)obrada (P)teCobro o (B)aja >>>").upper()
        if epeleccion == 'C':
            estado_poliza+='Cobrada'
            break
        elif epeleccion=='P':
            estado_poliza+='PteCobro'
            break
        elif epeleccion=='B':
            estado_poliza+='Baja'
            break
        else:
            print("Error. Escoja entre 1 de los 3 posibles estados.")
    print(f"Estado de la póliza: {estado_poliza}")
    while True:
        fecha_emision=input("Detalle la fecha de emisión de la póliza actual en el siguiente formato (DD/MM/AAAA) >>> ")
        if len(fecha_emision)==10 and fecha_emision[2]=='/' and fecha_emision[5]=='/' and fecha_emision[:2].isdigit() and fecha_emision[3:5].isdigit() and fecha_emision[6:].isdigit():
            fechaEm=fecha_emision.split('/')
            listaAux=[]
            for elto in fechaEm:
                elto=int(elto)
                listaAux.append(elto)
            if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                print("Fecha emisión válida. Registrando...")
                break
            else:
                print("Error. La fecha de emisión introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                continue
        else:
                print("Error. La fecha de emisión introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                continue
    print("Hay dos maneras de hacer efectivo el pago de la póliza.\n1. (E)fectivo.\n2. (B)anco.")
    while True:
        pagoEleccion=input("Elija su forma de pago escribiendo las letras entre paréntesis >>> ").upper()
        if pagoEleccion == 'E':
            print("Forma de pago elegida: Efectivo")
            print("Datos bancarios aceptados correctamente.")
            forma_pago="Efectivo"
            break
        elif pagoEleccion == 'B':
            print("Forma de pago elegida: Banco")
            while True:
                print("Se debe validar el IBAN del propietario de la póliza.")
                iban=input("Escriba el IBAN del propietario de la póliza >>> ").upper
                iban=iban.replace(' ', '')
                if len(iban)==24 and iban[0:2].isalpha() and iban[2:].isdigit():
                    print("Validando el IBAN, espere...")
                    if ComprobarIBAN(iban):
                        VALIDADO=True
                        print("IBAN válido.\n Estableciendo ahora otras politicas...")
                        banco=input("Escriba ahora el banco al cual pertenece la cuenta domiciliada >>> ")
                        forma_pago=(banco, iban)
                        break
                    else:
                        print("Hubo un error...")
                else:
                    print("Error. Escriba el IBAN en el formato ESNN NNNN NNNN NNNN NNNN NNNN.")
            if VALIDADO:
                print("Datos aceptados correctamente.")
                break
    #creamos aqui el dict para traerlo al return
    dNroPoliza={'nro_poliza':str(nro_poliza), #string del nro_poliza 
                'id_tomador':id_tomador,
                'matricula':matricula,
                'datos_vehiculo':datos_vehiculo,
                'cobertura':cobertura,
                'id_conductor': id_conductor,
                'estado_poliza':estado_poliza,
                'fecha_emision':fecha_emision,
                'forma_pago': forma_pago}
    lista.append(dNroPoliza)
    print(f"Creando póliza con ID: {str(nro_poliza)}")
    print(f"Póliza creada exitosamente.")
    print("Volviendo al menú principal.")
    return lista
def ModificarPoliza(poliza:list, banlistPolizas:list, tomadores:list) -> list:
    '''ID -> lista que contiene los identificadores de las pólizas - se usa para validar
       CAMPOS -> lista que contiene los campos de las pólizas - se usa para acceder a los datos de manera sencilla
       función que permite modificar pólizas respetando las restricciones impuestas por el enunciado.'''
    ID=[]
    CAMPOS=[]
    for lista in poliza:               
        for diccionario in lista:     
            for clave in diccionario.keys(): #considerar  
             if clave !='nro_poliza' and clave not in CAMPOS: #despreciamos el identificador de la póliza al tener la condición de no poder modificar el nº de póliza
                CAMPOS.append(clave)
    for elto in poliza:
        for subelto in elto:
            ID.append(subelto['nro_poliza'])
    if not ID:
        print("Error. No se han encontrado datos para modificar.")
        return poliza, banlistPolizas, tomadores
    else:
        for dato in ID:
            print(dato, end=' ')
        print()
        
        print("Seleccione entre los siguientes números de póliza: ")
        seleccionID=input('>>> ') #ELECCION DEL USUARIO Y AQUI ACCEDEMOS
        if seleccionID in ID:
            while True:
                print("Para modificar la póliza se deberá primero seleccionar el campo que se quiere modificar.")
                print("Estos son los campos:")
                for info in CAMPOS:
                    print(info)
                print()
                seleccionCampo=input("Escriba el campo correspondiente >>> ")
                break
            #llegados a este paraguas, seleccionamos los campos a modificar y nos retorna siempre que terminemos al menu.
            match seleccionCampo:
                case 'id_tomador':
                    while True:
                        TOMADORESID=[]
                        for elto in tomadores:
                            for subelto in elto:
                                if subelto['id_tomador'] not in TOMADORESID:
                                    TOMADORESID.append(subelto['id_tomador'])
                        print("Esta es la lista de identificadores que existen de los tomadores:")
                        for elto in TOMADORESID:
                            print(f"-{elto}")
                        print("De los cuales estos ya se han usado y no pueden repetirse:")
                        for elto in banlistPolizas:
                            print(f"-{elto}")    
                        id_tomador = input("Escriba el NIF | NIE | CIF >>> ")
                        if id_tomador not in banlistPolizas and id_tomador in TOMADORESID: #filtro: que no esté en la lista de no permitidos y que esté en la lista de TOMADORESID
                            if ValidarDocumento(id_tomador):
                                print("Documento validado correctamente.")
                                print("Modificando...")
                                for elto in poliza:
                                    for subelto in elto:
                                        if subelto['nro_poliza']==seleccionID:
                                            antiguo=subelto['id_tomador']
                                            subelto['id_tomador']=id_tomador
                                            banlistPolizas.append(id_tomador)
                                            banlistPolizas.remove(antiguo)
                                            return poliza, banlistPolizas, tomadores
                            else:
                                print("Error. El tipo de documento no es válido según las normas de validación estándares en España.\nEscriba nuevamente un valor para NIF | NIE | CIF\n\n")
                        else:
                            print("Esa identificación no se encuentra entre las bases de datos registradoras o ya se ha usado con anterioridad.")
                case 'matricula': #
                    print("Antigua matrícula")
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza'] == seleccionID:
                                print(subelto['matricula'])
                    while True:
                        matricula=input("Escriba la matrícula del vehículo que requiere registro >>> ").upper()
                        if ComprobarMatricula(matricula):
                            print("La matrícula es válida.")
                            for elto in poliza:
                                for subelto in elto:
                                    if subelto['nro_poliza'] == seleccionID:
                                        subelto['matricula']=matricula
                                        print("Matricula modificada exitosamente.")
                                        return poliza, banlistPolizas, tomadores
                                        
                        else:
                            print("Error. La matrícula introducida tiene un formato inválido.")
                            continue   
                case 'datos_vehiculo':
                        tipoVehiculo=('Ciclomotor','Moto', 'Turismo','Furgoneta','Camión')
                        print("Se muestran los antiguos datos del vehículo registrado")
                        for elto in poliza:
                            for subelto in elto:
                                if subelto['nro_poliza']==seleccionID:
                                    print(subelto['datos_vehiculo'])
                        while True:
                            tipo=input(f"Seleccione ahora un tipo de vehículo que quiera registrar - datos disponibles > {tipoVehiculo} >>> ")
                            if tipo in tipoVehiculo:
                                print(f"Vehículo de tipo {tipo} seleccionado.")
                                break
                            else:
                                print("Error. Seleccione correctamente entre la lista de tipos de vehículos disponibles para registrar.")
                        while True:
                            marca=input("Escriba la marca que representa al vehículo >>> ")
                            if marca !='':
                                print("Marca seleccionada correctamente.")
                                break
                            else:
                                print("Error. No se admiten valores nulos o vacíos en el registro de marcas de un vehículo.")
                        while True:
                            modelo=input("Escriba el modelo que acompaña a la marca del vehículo >>> ")
                            if modelo !='':
                                print("Modelo seleccionado correctamente.")
                                break
                            else:
                                print("Error. No se admiten valores nulos o vacíos.")
                        while True:
                            tipoFuncionamiento=('Combustión', 'Eléctrico', 'Mixto')
                            funcionamiento=input(f"Selecciona un valor correspondiente al funcionamiento del vehículo figurado en la siguiente tupla - {tipoFuncionamiento} >>> ")
                            if funcionamiento in tipoFuncionamiento:
                                print("Dato proporcionado con éxito.")
                                break
                            else:
                                print("Error. Seleccione adecuadamente entre los datos cotejados.")
                        datos_vehiculo=(tipo, marca, modelo, funcionamiento)                

                        for elto in poliza:
                            for subelto in elto:
                                if subelto['nro_poliza']==seleccionID:
                                    subelto['datos_vehiculo'] = datos_vehiculo
                                    print("Datos cambiados correctamente.")
                                    return poliza, banlistPolizas, tomadores

                case 'cobertura': 
                    listaCoberturas=[]
                    coberturasDisponibles=('RC', 'RL', 'INC', 'RB', 'TR')
                    print(f"En la empresa tenemos para contratar las siguientes coberturas - {coberturasDisponibles} \n Transcripción\nRC - Responsabilidad Civil \nRL - Rotura de lunas\nINC - Incendio\nRB - Robos\nTR - Seguro a todo riesgo")
                    print("Ud. puede contratar más de una cobertura.")
                    trContratado=False
                    cobContratadas=[]
                    estandar=False
                    print("Mostrando antigua cobertura: ")
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                print(subelto['cobertura'])
                                print()
                                print()
                    while True:
                        eleccionCobertura=input(f"Escriba su elección entre {coberturasDisponibles} o el caracter @ para parar: ")
                        if eleccionCobertura != '@' and eleccionCobertura in coberturasDisponibles and eleccionCobertura not in listaCoberturas:
                            if eleccionCobertura == 'TR' and not trContratado:
                                franquicia = input(f"Escriba la franquicia colaboradora asociada a la cobertura >>> ")
                                valor_franquicia = ('TR', franquicia)
                                listaCoberturas.append(valor_franquicia)
                                cobContratadas.append(eleccionCobertura)
                                trContratado = True
                            elif eleccionCobertura == 'TR' and trContratado:
                                print("Error. La cobertura 'TR' ya ha sido contratada.")
                            elif eleccionCobertura in coberturasDisponibles and eleccionCobertura != 'TR':
                                listaCoberturas.append(eleccionCobertura)
                                cobContratadas.append(eleccionCobertura)
                                print(f"Cobertura añadida: {eleccionCobertura}")
                        elif eleccionCobertura == '@':
                            if not listaCoberturas:
                                print("Por defecto, ud. tiene contratada la cobertura RC.")
                                estandar=True
                                break
                            else:
                                break
                        else:
                            print(f"Error. Escriba una cobertura de entre las disponibles en el sistema y que no haya sido contratada. \n-> C. CONTRATADAS >>> {cobContratadas}")
                    if not estandar:
                        cobertura=tuple(listaCoberturas)
                        for elto in poliza:
                            for subelto in elto:
                                if subelto['nro_poliza']==seleccionID:
                                    subelto['cobertura']=cobertura
                                    print("Nueva cobertura actualizada.")
                                    return poliza, banlistPolizas, tomadores
                    if estandar:
                        cobertura='RC'
                        for elto in poliza:
                            for subelto in elto:
                                if subelto['nro_poliza']==seleccionID:
                                    subelto['cobertura']=cobertura 
                                    print("La cobertura estándar se ha actualizado por defecto.")     
                                    return poliza, banlistPolizas, tomadores
          
                case 'id_conductor': 
                    print("Antiguos registros de la identificación del conductor: ")
                    idConductor=[]
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                print(subelto['id_conductor'])
                            
                    print("A continuación se detallan los datos pertenecientes a los conductores del vehículo registrado.")
                    while True:
                        while True:
                            nifnie=input("Escriba el DNI/NIE de la persona física conductora del vehículo >>> ")
                            if ValidarDocumento(nifnie):
                                print("DNI/NIE validado correctamente.")
                                idConductor.append(nifnie)
                                break
                            else:
                                print("Error. El tipo de documento no es válido según las normas de validación estándares en España.\nEscriba nuevamente un valor para DNI/NIE.\n\n")
                        while True:
                            fecha_nacimiento=input("Detalle la fecha de nacimiento del conductor en el siguiente formato (DD/MM/AAAA) >>> ")
                            if len(fecha_nacimiento)==10 and fecha_nacimiento[2]=='/' and fecha_nacimiento[5]=='/' and fecha_nacimiento[:2].isdigit() and fecha_nacimiento[3:5].isdigit() and fecha_nacimiento[6:].isdigit():
                                fechaNac=fecha_nacimiento.split('/')
                                listaAux=[]
                                for elto in fechaNac:
                                    elto=int(elto)
                                    listaAux.append(elto)
                                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2006:
                                    print("Fecha de nacimiento válida. Registrando...")
                                    idConductor.append(fecha_nacimiento)
                                    break
                            else:
                                print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                continue
                        while True:
                            tiposCarne=('AM','A1','A2','A','B1','B','C1','D1','D','BE','C1E','CE','D1E','DE')
                            tipo_carnet=input(f"Seleccione un carné de entre el siguiente catálogo - {tiposCarne} >>> ")
                            if tipo_carnet in tiposCarne:
                                print("Tipo de carné de conducir seleccionado correctamente.")
                                idConductor.append(tipo_carnet)
                                break
                            else:
                                print("Error. Seleccione correctamente un tipo de carné de conducir.")
                        while True:
                            fecha_carnet=input("Establezca una fecha de emisión del carné con el formato DD/MM/AAAA >>> ")
                            if len(fecha_carnet)==10 and fecha_carnet[2]=='/' and fecha_carnet[5]=='/' and fecha_carnet[:2].isdigit() and fecha_carnet[3:5].isdigit() and fecha_carnet[6:].isdigit():
                                fechaCarnet=fecha_carnet.split('/')
                                listaAux=[]
                                for elto in fechaCarnet:
                                    elto=int(elto)
                                    listaAux.append(elto)
                                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025: #DETECCIÓN DE ERRORES / ERROR
                                    print("Fecha de emisión del carné de conducir válida. Registrando...")
                                    idConductor.append(fecha_carnet)
                                    break
                                else:
                                    print("Error. La fecha de emisión del carné de conducir introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                    continue
                        break

                    id_conductor=tuple(idConductor)
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                subelto['id_conductor']=id_conductor
                                print("Datos correctamente actualizados.")
                                return poliza, banlistPolizas, tomadores                
                case 'estado_poliza':
                    print("Se observa el antiguo estado de la póliza:")
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                print(subelto['estado_poliza'])
                    estado_poliza=''
                    print("Cargando datos de actualización de estado de póliza...\nLa póliza puede solamente estar en uno de los siguientes estados:\nCobrada\nPteCobro\nBaja")
                    while True:
                        epeleccion=input("Escoja entre (C)obrada (P)teCobro o (B)aja >>>").upper()
                        if epeleccion == 'C':
                            estado_poliza+='Cobrada'
                            break
                        elif epeleccion=='P':
                            estado_poliza+='PteCobro'
                            break
                        elif epeleccion=='B':
                            estado_poliza+='Baja'
                            break
                        else:
                            print("Error. Escoja entre 1 de los 3 posibles estados.")
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                subelto['estado_poliza']=estado_poliza
                                print("Estado de la póliza actualizada y modificada con éxito.")
                                return poliza, banlistPolizas, tomadores

                case 'fecha_emision': 
                    print("Antigua fecha de emisión del carné: ")
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                print(subelto['fecha_emision'])
                    while True:
                        fecha_emision=input("Detalle la fecha de emisión de la póliza actual en el siguiente formato (DD/MM/AAAA) >>> ")
                        if len(fecha_emision)==10 and fecha_emision[2]=='/' and fecha_emision[5]=='/' and fecha_emision[:2].isdigit() and fecha_emision[3:5].isdigit() and fecha_emision[6:].isdigit():
                            fechaEm=fecha_emision.split('/')
                            listaAux=[]
                            for elto in fechaEm:
                                elto=int(elto)
                                listaAux.append(elto)
                            if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                print("Fecha emisión válida. Registrando...")
                                break
                            else:
                                print("Error. La fecha de emisión introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                continue
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                subelto['fecha_emision']=fecha_emision
                                print("Fecha de emisión actualizada con éxito.")
                                return poliza, banlistPolizas, tomadores
                    
                case 'forma_pago': 
                    print("Antiguos datos formalizados:")
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                print(subelto['forma_pago'])
                    print("Hay dos maneras de hacer efectivo el pago de la póliza.\n1. (E)fectivo.\n2. (B)anco.")
                    while True:
                        pagoEleccion=input("Elija su forma de pago escribiendo las letras entre paréntesis >>> ").upper()
                        if pagoEleccion == 'E':
                            print("Forma de pago elegida: Efectivo")
                            print("Datos bancarios aceptados correctamente.")
                            forma_pago="Efectivo"
                            break
                        elif pagoEleccion == 'B':
                            print("Forma de pago elegida: Banco")
                            while True:
                                print("Se debe validar el IBAN del propietario de la póliza.")
                                iban=input("Escriba el IBAN del propietario de la póliza >>> ")
                                iban=iban.replace(' ', '')
                                if len(iban)==24 and iban[0:2].isalpha() and iban[2:].isdigit():
                                    print("Validando el IBAN, espere...")
                                    if ComprobarIBAN(iban):
                                        VALIDADO=True
                                        print("IBAN válido.\n Estableciendo ahora otras politicas...")
                                        banco=input("Escriba ahora el banco al cual pertenece la cuenta domiciliada >>> ")
                                        forma_pago=(banco, iban)
                                        break
                                    else:
                                        print("Hubo un error...")
                                else:
                                    print("Error. Escriba el IBAN en el formato ESNN NNNN NNNN NNNN NNNN NNNN.")
                            if VALIDADO:
                                print("Datos aceptados correctamente.")
                                break
                    for elto in poliza:
                        for subelto in elto:
                            if subelto['nro_poliza']==seleccionID:
                                subelto['forma_pago']=forma_pago
                                print("Datos financieros aceptados y modificados con éxito.")
                                return poliza, banlistPolizas, tomadores
                case _:
                    print("Error. Selecciona entre los campos disponibles.")   
        else:
            print("El ID seleccionado no es válido. Asegúrese de que el número de póliza esté en la lista.")
            return poliza
def EliminarPoliza(polizas:list, banlistPolizas:list, tomadores:list, banlistTomadores:list, recibos:list, banlistRecibos:list, siniestros:list) -> list:
    '''Función que elimina pólizas ajustandonos a las restricciones que nos impone la práctica 
    y a las políticas de borrado (similares a CASCADE en SQL)'''
    print("Números de póliza disponibles") 
    print("-----------------------------")
    ids = []
    id_tomador = None  #Inicializamos la variable para evitar posibles errores en la ejecucion

    for elto in polizas:
        for subelto in elto:
            print(f"* {subelto['nro_poliza']}")
            ids.append(subelto['nro_poliza'])

    #Recorremos la lista para buscar la póliza
    eleccion = input("Escriba el número de póliza a eliminar >>> ")
    
    if eleccion in ids:
        for lista_polis in polizas:
            for diccionario in lista_polis:
                if eleccion == diccionario['nro_poliza']:
                    if diccionario['estado_poliza'] == 'Baja':
                        id_tomador = diccionario['id_tomador']  #Se asigna el id_tomador antes de eliminar
                        polizas.remove(lista_polis)
                        print(f"Póliza con ID: {eleccion} eliminada exitosamente.")
                    else:
                        print("Error. Sólo se pueden eliminar pólizas que NO ESTÉN VIGENTES (Baja).")
                        return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos , siniestros

        #Si id_tomador es None, significa que no se encontró la póliza con el estado "Baja"
        if id_tomador is None:
            print("Error. No se encontró la póliza con estado 'Baja'.")
            return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos, siniestros

        #eliminamos de banlistPolizas
        for elto in banlistPolizas:
            if id_tomador in elto:
                banlistPolizas.remove(id_tomador)
                break

        #eliminamos de recibos y banlistRecibos
        if recibos and banlistRecibos:
            for elto in recibos:
                for subelto in elto:
                    if subelto['nro_poliza'] == eleccion:
                        recibos.remove(elto)
                        break
            for elto in banlistRecibos:
                if elto == eleccion:
                    banlistRecibos.remove(elto) 
        if siniestros: #y por ultimo actualizamos los siniestros para borrar coincidencias
            for elto in siniestros:
                for subelto in elto:
                    if subelto['nro_poliza']==eleccion:
                        siniestros.remove(elto)
                        break               

        return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos, siniestros  
    else:
        print("Error. No se encuentra el ID asociado.")
        return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos, siniestros
##////////////////////////////////////////////////////////////////////////////////////////////////////7
'''HA PASADO EL TEST DE PRUEBAS ADECUADAMENTE CON UNA GRAN COLECCIÓN DE DATOS'''                            
            
                    

            