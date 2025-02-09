#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
from Utilidades import ValidarDocumento
from Utilidades import ComprobarMatricula
from Utilidades import ComprobarIBAN
import Utilidades
def CrearPoliza(nro_poliza:int, tomadores:list, banlist:list) -> list:
    lista=[]
    listaCoberturas=[]
    tipoVehiculo=('Ciclomotor','Moto', 'Turismo','Furgoneta','Camión')
    coberturasDisponibles=('RC', 'RL', 'INC', 'RB', 'TR')
    cobertura=()
    documentosDisponibles=[]

    print("Bienvenido al asistente creador de pólizas.\nRellene adecuadamente los siguientes datos:")
    for elto in tomadores:
        for subelto in elto:
            documentosDisponibles.append(subelto['id_tomador'])
    while True:
        print("Mostrando documentos registrados en el sistema:")
        print(documentosDisponibles)
            
            # Solicitar el ID del tomador
        id_tomador = input("Escriba el NIF | NIE | CIF >>> ")

            # Validar el ID del tomador
        if id_tomador in banlist: #Se checkea primero si está en la lista de id ya registrados.
            print("Error. El id ya se encuentra registrado en la base de datos. Pruebe con otro.")
            continue

        elif id_tomador in documentosDisponibles and id_tomador not in banlist:
            if ValidarDocumento(id_tomador):
                print("Documento validado correctamente.")
                break
            else:
                    print("Error. El tipo de documento no es válido según las normas de validación estándares en España.\nEscriba nuevamente un valor para NIF | NIE | CIF\n\n")

        elif id_tomador not in documentosDisponibles:
            print(f"El ID {id_tomador} no figura en la base de datos como registrado. Seleccione un ID válido de los previamente registrados.")
        
        else:
            print(f"Error inesperado. Intente nuevamente. Detalles:\nID ingresado: {id_tomador}\nIDs disponibles: {documentosDisponibles}\nBanlist actual: {banlist}")
    while True:
        matricula=input("Escriba la matrícula del vehículo que requiere registro >>> ").upper()
        if ComprobarMatricula(matricula):
            break
        else:
            print("Error. La matrícula introducida tiene un formato inválido.")
            continue
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
            print("Error. Seleccione adecuadamente entre la tupla figurante.")
    datos_vehiculo=(tipo, marca, modelo, funcionamiento)
    print(f"En la empresa tenemos para contratar las siguientes coberturas - {coberturasDisponibles} \n Transcripción\nRC - Responsabilidad Civil \nRL - Rotura de lunas\nINC - Incendio\nRB - Robos\nTR - Seguro a todo riesgo")
    print("Ud. puede contratar más de una cobertura.")
    trContratado=False
    cobContratadas=[]
    estandar=False
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
    if estandar:
        cobertura='RC'
    idConductor=[]
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

    id_cobertura=tuple(idConductor)
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

    dNroPoliza={'nro_poliza': nro_poliza,
                'id_tomador':id_tomador,
                'matricula':matricula,
                'datos_vehiculo':datos_vehiculo,
                'cobertura':cobertura,
                'id_cobertura': id_cobertura,
                'estado_poliza':estado_poliza,
                'fecha_emision':fecha_emision,
                'forma_pago': forma_pago}
    lista.append(dNroPoliza)
    print(f"Creando póliza con ID: {nro_poliza}")
    print(f"Póliza creada exitosamente.")
    print("Volviendo al menú principal.")
    return lista
def ModificarPoliza(poliza:list) -> list:
    #1. Se tiene que seleccionar la póliza, la llamamos por el ID.
    ID=[]
    CAMPOS=[]
    for lista in poliza:               
        for diccionario in lista:     
            for clave in diccionario.keys():  
             if clave !='nro_poliza' and clave not in CAMPOS:      
                CAMPOS.append(clave)
    for elto in poliza:
        for subelto in elto:
            ID.append(subelto['nro_poliza'])
    if not ID:
        print("Error. No se han encontrado datos para modificar.")
        return poliza
    else:
        for dato in ID:
            print(dato, end=' ')
        print()
        
        print("Seleccione entre los siguientes números de póliza: ")
        seleccionID=int(input('>>> '))
        if seleccionID in ID:
            print("Para modificar la póliza se deberá primero seleccionar el campo que se quiere modificar.")
            print("Estos son los campos:")
            for info in CAMPOS:
                print(info)
            print()
            return poliza
        else:
            print("El ID seleccionado no es válido. Asegúrese de que el número de póliza esté en la lista.")
            return poliza
def EliminarPoliza(polizas:list, banlistPolizas:list, tomadores:list, banlistTomadores:list, recibos:list, banlistRecibos:list) -> list:
        print("Números de póliza disponibles") 
        print("-----------------------------")
        ids=[]
        for elto in polizas:
            for subelto in elto:
                print(f"* {subelto['nro_poliza']}")
                ids.append(subelto['nro_poliza'])
        # Recorremos la lista para buscar la póliza
        try:
            eleccion=int(input("Escriba el número de póliza a eliminar >>> "))
        except:
            print("Error. El tipo de dato introducido no es numérico.")
        else:
            if eleccion in ids:
                for lista_polis in polizas:
                    for diccionario in lista_polis:
                        if eleccion == diccionario['nro_poliza']:
                            if diccionario['estado_poliza'] == 'Baja':
                                id_tomador = diccionario['id_tomador']  #obtengo el id_tomador antes de eliminar para poder borrar en el resto
                                polizas.remove(lista_polis)
                                print(f"Póliza con ID: {eleccion} eliminada exitosamente.")
                            else:
                                print("Error. Sólo se pueden eliminar pólizas que NO ESTÉN VIGENTES (Baja).")
                                return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos #tupla de desempaquetamiento en principal

                for elto in banlistPolizas:
                    if id_tomador in elto:
                        banlistPolizas.remove(id_tomador)
                        break
                if tomadores and banlistTomadores:
                    for elto in tomadores:
                        for subelto in elto:
                            if subelto['id_tomador']==id_tomador:
                                tomadores.remove(elto)
                                break
                    for elto in banlistTomadores:
                        if elto==id_tomador:
                            banlistTomadores.remove(elto)
                            break
                if recibos and banlistRecibos:
                    for elto in recibos:
                        for subelto in elto:
                            if subelto['nro_poliza']==eleccion:
                                recibos.remove(elto)
                                break
                    for elto in banlistRecibos:
                        if elto==eleccion:
                            banlistRecibos.remove(elto)                
                return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos #tupla de desempaquetamiento en principal
            else:
                print("Error. No se encuentra el id asociado.")
                return polizas, banlistPolizas, tomadores, banlistTomadores, recibos, banlistRecibos #tupla de desempaquetamiento en principal
                            
            
                    

            