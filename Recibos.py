#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín

'''• No se permiten recibos con igual identificación
• En la opción modificar no se permite cambiar el identificador del rec
• A la hora de crear el recibo, la póliza a la que se quiere asociar debe estar 
creada.
• No se podrá eliminar una recibo que esté vigor (pendiente o cobrado).
• Al borrar un recibo no hace falta borrar más nada asociado a la póliza'''
id_recibo=0
def CrearRecibo(id_recibo:int, banlist:list, polizas:list) -> list:
    lista = []
    ID = []
    
    print("Bienvenido/a al asistente de creación de recibos.\nPrimero seleccione un ID de póliza sobre la cual formalizar el recibo.")
    print("Se muestran a continuación una serie de números identificadores. Escoja el número sobre el cual crear un recibo asociado.")
    
    # Mostrar las pólizas disponibles y recoger sus IDs
    for elto in polizas:
        for subelto in elto:
            print(f"- {subelto['nro_poliza']}", end=' ')
            ID.append(subelto['nro_poliza'])  # Guardar IDs de pólizas

    print()
    try:
        eleccion = int(input("Seleccione un número de póliza >>> "))
    except:
        print("Error. Introduzca un número válido.")
        return None

    # Verificar si la elección está en las pólizas existentes
    if eleccion not in ID:
        print("No se ha seleccionado ninguna identificación asociada a una póliza. Volviendo al menú principal.")
        return None

    # Verificar si la póliza ya tiene un recibo (está en la banlist)
    # if eleccion in banlist:
    #     print("Error. No se pueden crear recibos con un mismo identificador de póliza. Esta póliza ya fue utilizada para crear un recibo.")
    #     return None

    # Continuar con la creación del recibo
    print("Cargando otros datos...")
    print("\nEstablecer ahora la fecha de inicio del recibo (DD/MM/AAAA).")

    # Validación de fecha de inicio
    while True:
        fecha_inicio = input(">>> ")
        if len(fecha_inicio)==10 and fecha_inicio[2]=='/' and fecha_inicio[5]=='/' and fecha_inicio[:2].isdigit() and fecha_inicio[3:5].isdigit() and fecha_inicio[6:].isdigit():
            fechaIn=fecha_inicio.split('/')
            listaAux=[]
            for elto in fechaIn:
                elto=int(elto)
                listaAux.append(elto)
            if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                print("Fecha de nacimiento válida. Registrando...")
                break
        else:
            print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
            continue

    # Duración del recibo
    print("\nCargando rutinas de estado de duración de un recibo...")
    duraciones = ('A', 'S', 'T', 'M')
    while True:
        print("Las pólizas se cobran de manera:\n(A)nual\n(S)emestral\n(T)rimestral\n(M)ensual")
        duracion = input("Seleccione de entre las opciones anteriores >>> ").upper()
        if duracion in duraciones:
            print("Periodo de liquidación de póliza seleccionado con éxito.")
            break
        else:
            print("Error. Seleccione correctamente entre las opciones listadas anteriormente (Indicadas en el paréntesis).")

    # Importe a cobrar
    while True:
        try:
            importe_cobrar = float(input("Escriba el monto a cobrar en cada vencimiento del periodo de liquidación >>> "))
            print("Importe seleccionado.")
            break
        except ValueError:
            print("Error. Escriba solamente entradas numéricas decimales en el importe a cobrar.")

    # Fecha de cobro
    while True:
        fecha_cobro = input("Establezca la fecha de cobro (DD/MM/AAAA) >>> ")
        if len(fecha_cobro) == 10 and fecha_cobro[2] == '/' and fecha_cobro[5] == '/' and \
           fecha_cobro[:2].isdigit() and fecha_cobro[3:5].isdigit() and fecha_cobro[6:].isdigit():
            dia, mes, anio = map(int, fecha_cobro.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2025:
                print("Fecha de cobro válida. Registrando...")
                break
            else:
                print("Error. La fecha de cobro introducida no es válida.")
        else:
            print("Error. Formato incorrecto. Use DD/MM/AAAA.")

    # Estado del recibo
    estadosrecibos = ['P', 'PB', 'C', 'CB', 'B']
    while True:
        print("Seleccione el estado del recibo:\n(P)endiente\n(PB)endiente_banco\n(C)obrado\n(CB)obrado_banco\n(B)aja")
        estado_recibo = input(">>> ").upper()
        if estado_recibo in estadosrecibos:
            print("Estado correctamente introducido.")
            break
        else:
            print("Error. Seleccione correctamente entre las opciones listadas.")

    # Crear el recibo
    print(f"Creando recibo asociado a la póliza con identificador {eleccion}")
    dNroRecibo = {
        'id_recibo': id_recibo,
        'nro_poliza': eleccion,
        'fecha_inicio': fecha_inicio,
        'duracion': duracion,
        'importe_cobrar': importe_cobrar,
        'fecha_cobro': fecha_cobro,
        'estado_recibo': estado_recibo
    }
    lista.append(dNroRecibo)

    # Actualizar banlist con la póliza utilizada
    banlist.append(eleccion)

    print(f"Recibo creado con identificador {id_recibo}")
    return lista


def ModificarRecibo(lista_recibos: list, polizas:list) -> list:
    CAMPOS=[]
    nroPol=[]
    duraciones = ('A', 'S', 'T', 'M')
    estadosrecibos = ['P', 'PB', 'C', 'CB', 'B']

    #Se tienen que desempaquetar las claves primeramente para que podamos sacar dos colecciones:
    #Colección A: campos=[] - lista con los campos de cada uno de los recibos - En el contexto de nuestra aplicación lo usamos como verificador cuando el usuario trata de acceder a los datos
    #Colección B: lista_recibos=[] - lista con los datos completos recibos de la llamada de la función.
    #1. Lo primero que hacemos es comprobar que la lista NO esté vacía. Si está VACIA la mandamos de vuelta y salimos al menú. 
    for elto in lista_recibos:
        for subelto in elto:
            for clave in subelto.keys():
                if clave!='id_recibo' and clave not in CAMPOS:
                    CAMPOS.append(clave)
    for elto in lista_recibos:
        for subelto in elto:
            nroPol.append(subelto['nro_poliza'])
    while True:
        ID=[]
        print("Lista de identificadores de recibos:")
        for elto in lista_recibos:
            for subelto in elto:
                ID.append(subelto['id_recibo'])
                print(f"- {subelto['id_recibo']}", end=' ')

        print("Seleccione un recibo que quiera MODIFICAR: ")
        seleccionarID=int(input(">>> "))
        if seleccionarID in ID: #Nos aseguramos de que el ID esté entre los datos cotejados.
            print(f"Se ha seleccionado el recibo con identificador {seleccionarID}")
            while True:
                print("\nSeleccione el campo que desea MODIFICAR:")
                for campo in CAMPOS:
                    print(f"- {campo}", end=' ')
                seleccionarCampo=input(">>> ").lower()
                if seleccionarCampo in CAMPOS:
                    match seleccionarCampo:
                        case 'nro_poliza':
                            print("Nº de póliza anterior")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['nro_poliza'])
                                    else:
                                        print("No hay números de póliza registrados para este recibo.")
                                        continue
                            print("Posibles cambios: ")
                            for nro in nroPol: 
                                print(f"- {nro}", end=' ')
                            nuevaPoliza=int(input("Escriba el nuevo número de póliza >>> "))
                            if nuevaPoliza in nroPol: #Nos aseguramos de que el nuevo número de póliza esté entre los datos cotejados.
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['nro_poliza']=nuevaPoliza
                            
                                print("Recibo modificado.")
                                return lista_recibos
                            else:
                                print("Error. El número de póliza introducido no se encuentra en la lista.")
                        case 'fecha_inicio':
                            print("Antigua fecha de inicio")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['fecha_inicio'])
                                    else:
                                        print("No hay fechas de inicio registradas para este recibo.")
                                        continue
                            cambioFecha=input("Introduzca una nueva fecha: ")
                            if len(cambioFecha)==10 and cambioFecha[2]=='/' and cambioFecha[5]=='/' and cambioFecha[:2].isdigit() and cambioFecha[3:5].isdigit() and cambioFecha[6:].isdigit():
                                fechaCam=cambioFecha.split('/')
                                listaAux=[]
                                for elto in fechaCam:
                                    elto=int(elto)
                                    listaAux.append(elto)
                                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                    print("Fecha de incio válida. Registrando...")
                                    for elto in lista_recibos:
                                        for subelto in elto:
                                            if subelto['id_recibo']==seleccionarID:
                                                subelto['fecha_inicio']=cambioFecha
                                    print("Fecha de inicio cambiada. \nRecibo modificado.")
                                    return lista_recibos
                            else:
                                print("Error. La fecha de inicio introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                continue

                        case 'duracion':
                            print("Antiguos datos de duración: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(f"Duración: {subelto['duracion']}")
                                    else:
                                        print("No hay duraciones registradas para este recibo.")
                                        continue
                            cambioDuracion=input(f"Seleccione una nueva duración entre {duraciones} >>> ")
                            if cambioDuracion in duraciones:
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['duracion']=cambioDuracion
                            else:
                                print("El cambio sugerido no se encuentra entre las opciones disponibles.")
                                continue
                        case 'importe_cobrar':
                            print("Antiguos datos del importe: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(f"Importe a cobrar: {subelto['importe_cobrar']}")
                                    else:
                                        print("No hay importes registrados para este recibo.")
                                        continue
                            cambioImporte=float(input("Introduzca un nuevo importe a cobrar >>> "))
                            if cambioImporte >= 0:
                                print("Importe válido. Registrando...")
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['importe_cobrar']=cambioImporte
                                            print("Importe cambiado.")
                                            return lista_recibos
                            else:
                                print("Error. El importe debe ser superior a 0.")
                                continue
                        case 'fecha_cobro':
                            print("Antigua fecha de inicio")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['fecha_cobro'])
                                    else:
                                        print("No hay fechas de cobro registradas para este recibo.")
                                        continue
                            cambioFecha=input("Introduzca una nueva fecha: ")
                            if len(cambioFecha)==10 and cambioFecha[2]=='/' and cambioFecha[5]=='/' and cambioFecha[:2].isdigit() and cambioFecha[3:5].isdigit() and cambioFecha[6:].isdigit():
                                fechaCam=cambioFecha.split('/')
                                listaAux=[]
                                for elto in fechaCam:
                                    elto=int(elto)
                                    listaAux.append(elto)
                                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                                    print("Fecha de incio válida. Registrando...")
                                    for elto in lista_recibos:
                                        for subelto in elto:
                                            if subelto['id_recibo']==seleccionarID:
                                                subelto['fecha_cobro']=cambioFecha
                                    print("Fecha de cobro cambiada. \nRecibo modificado.")
                                    return lista_recibos
                            else:
                                print("Error. La fecha de cobro introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                continue
                        case 'estado_recibo':
                            print("Antiguo estado del recibo: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['estado_recibo'])
                                    else:
                                        print("No hay estados registrados para este recibo.")
                                        continue
                            cambioEstado=input(f"Introduzca un nuevo estado entre los siguientes {estadosrecibos}: ")
                            if cambioEstado in estadosrecibos:
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['estado_recibo']=cambioEstado
                                            print("Estado cambiado.\nRecibo modificado.")
                                            return lista_recibos
                                        else:
                                             print("No se ha encontrado el recibo con ese ID.")
                                             continue
                            else:
                                print("El cambio sugerido no se encuentra entre las opciones disponibles.")
                                continue


                elif seleccionarCampo == ' ':
                    print("No es posible introducir un campo vacío. Por favor escriba datos.")
                else:
                    print("Error. El campo escrito no se encuentra entre las opciones disponibles.")
                    continue
                




def EliminarRecibo(listaRecibos: list) -> list:
    print("Bienvenido/a al asistente para eliminar recibos.")
    if not listaRecibos: #Comprobación de que la lista está vacía
        print("No hay recibos registrados actualmente. Volviendo al menú principal.")
        return listaRecibos
    print("A continuación se muestran los recibos disponibles:")
    for elto in listaRecibos:
        for subelto in elto:
            print(f"id:recibo: {subelto['id_recibo']}")
            pass
    #//Continuar con barrido de comprobación