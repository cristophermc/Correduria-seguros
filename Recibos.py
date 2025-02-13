#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín

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
    eleccion=input("Seleccione un número de póliza >>> ")
 

    # Verificar si la elección está en las pólizas existentes
    if eleccion not in ID:
        print("No se ha seleccionado ninguna identificación asociada a una póliza. Volviendo al menú principal.")
        return None

    # Continuar con la creación del recibo
    print("Cargando otros datos...")
    print("\nEstablecer ahora la fecha de inicio del recibo (DD/MM/AAAA).")

    # Validación de fecha de inicio
    if eleccion in ID:
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
        print("Seleccionando ahora el importe a pagar por el cobrador de la póliza a la compañía.")
        while True:
            try:
                importe_pagar=float(input("Escriba el monto a pagar por el cobrador de la póliza >>> "))
            except:
                print("Error. Escriba solamente entradas numéricas decimales en el importe a pagar.")
                continue
            else:
                print("Importe seleccionado.")
                break
        print()
        print("Estableciendo ahora el estado de liquidación.")
        while True:
            print("El recibo puede estar en dos estados: (P)endiente o (L)iquidado.")
            estado_liquidacion=input("Seleccione el estado de liquidación >>> ").upper()
            if estado_liquidacion=='P':
                estado_liquidacion='Pendiente'
                print("Estado de liquidación establecido con éxito.")
                break
            elif estado_liquidacion=='L':
                estado_liquidacion='Liquidado'
                print("Estado de liquidación establecido con éxito.")
                break
            else:
                print("Error. Escoja adecuadamente entre los estados figurados.")
        print()
        print("Estableciendo ahora la fecha de liquidación.")
        while True:
            fecha_liquidacion=input("DD/MM/AAAA >>> ")
            if len(fecha_liquidacion)==10 and fecha_liquidacion[2]=='/' and fecha_liquidacion[5]=='/' and fecha_liquidacion[:2].isdigit() and fecha_liquidacion[3:5].isdigit() and fecha_liquidacion[6:].isdigit():
                fechaLq=fecha_liquidacion.split('/')
                listaAux=[]
                for elto in fechaLq:
                    elto=int(elto)
                    listaAux.append(elto)
                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                    print("Fecha de liquidación válida. Registrando...")
                    break
                else:
                    print("Error. La fecha de liquidación introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                    continue
            
        print(f"Creando recibo asociado a la póliza con identificador {eleccion}")
        dNroRecibo = {
            'id_recibo': str(id_recibo), #reconversión a string
            'nro_poliza': eleccion,
            'fecha_inicio': fecha_inicio,
            'duracion': duracion,
            'importe_cobrar': importe_cobrar,
            'fecha_cobro': fecha_cobro,
            'estado_recibo': estado_recibo,
            'importe_pagar': importe_pagar,
            'estado_liquidacion':estado_liquidacion,
            'fecha_liquidacion':fecha_liquidacion,
            }
        lista.append(dNroRecibo)

        # Actualizar banlist con la póliza utilizada
        # banlist.append(eleccion)

        print(f"Recibo creado con identificador {id_recibo}")
        return lista
def ModificarRecibo(lista_recibos: list, polizas:list) -> list:
    CAMPOS=[]
    nroPol=[]
    duraciones = ('A', 'S', 'T', 'M')
    estadosrecibos = ['P', 'PB', 'C', 'CB', 'B']
    estadosliquidacion=['Liquidado', 'Pendiente']

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
            
        print()
        print("Seleccione un recibo que quiera MODIFICAR: ")
        seleccionarID=input(">>> ")
        if seleccionarID in ID: #Nos aseguramos de que el ID esté entre los datos cotejados.
            print(f"Se ha seleccionado el recibo con identificador {seleccionarID}")
            while True:
                print()
                print()
                print("\nSeleccione el campo que desea MODIFICAR:")
                print()
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
                            print("Posibles cambios: ")
                            for elto in polizas:
                                for subelto in elto:
                                    if subelto['nro_poliza']!=seleccionarID and subelto['nro_poliza'] not in nroPol:
                                        nroPol.append(subelto['nro_poliza'])
                            for nro in nroPol: 
                                print(f"- {nro}", end=' ')
                            nuevaPoliza=input("Escriba el nuevo número de póliza >>> ")
                            if nuevaPoliza in nroPol: #Nos aseguramos de que el nuevo número de póliza esté entre los datos cotejados.
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['nro_poliza']=nuevaPoliza
                                print("Recibo modificado.")
                                return lista_recibos, polizas
                            else:
                                print("Error. El número de póliza introducido no se encuentra en la lista.")
                        case 'fecha_inicio':
                            print("Antigua fecha de inicio")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['fecha_inicio'])
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
                                    return lista_recibos, polizas
                            else:
                                print("Error. La fecha de inicio introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                return lista_recibos, polizas

                        case 'duracion':
                            print("Antiguos datos de duración: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(f"Duración: {subelto['duracion']}")
        
                            cambioDuracion=input(f"Seleccione una nueva duración entre {duraciones} >>> ")
                            if cambioDuracion in duraciones:
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['duracion']=cambioDuracion
                                            print("Datos de duración modificados.")
                                            return lista_recibos, polizas
                            else:
                                print("El cambio sugerido no se encuentra entre las opciones disponibles.")
                                return lista_recibos, polizas
                        case 'importe_cobrar':
                            print("Antiguos datos del importe: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(f"Importe a cobrar: {subelto['importe_cobrar']}")

                            cambioImporte=float(input("Introduzca un nuevo importe a cobrar >>> "))
                            if cambioImporte >= 0:
                                print("Importe válido. Registrando...")
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['importe_cobrar']=cambioImporte
                                            print("Importe cambiado.")
                                            return lista_recibos, polizas
                            else:
                                print("Error. El importe debe ser superior a 0.")
                                return lista_recibos, polizas
                        case 'fecha_cobro':
                            print("Antigua fecha de inicio")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['fecha_cobro'])
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
                                    return lista_recibos, polizas
                            else:
                                print("Error. La fecha de cobro introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                return lista_recibos, polizas
                        case 'estado_recibo':
                            print("Antiguo estado del recibo: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['estado_recibo'])
                            cambioEstado=input(f"Introduzca un nuevo estado entre los siguientes {estadosrecibos}: ")
                            if cambioEstado in estadosrecibos:
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['estado_recibo']=cambioEstado
                                            print("Estado cambiado.\nRecibo modificado.")
                                            return lista_recibos, polizas
                            else:
                                print("El cambio sugerido no se encuentra entre las opciones disponibles.")
                                return lista_recibos, polizas
                        case 'importe_pagar':
                            print("Antiguo importe a pagar:")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['importe_pagar'])
                            cambioImportePagar=float(input("Introduzca un nuevo importe a pagar >>> "))
                            if cambioImportePagar >= 0:
                                print("Importe válido. Registrando...")
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['importe_pagar']=cambioImportePagar
                                            print("Importe a pagar cambiado.")
                                            return lista_recibos, polizas
                            else:
                                print("Error. El importe debe ser superior a 0.")
                                return lista_recibos, polizas
                        case 'estado_liquidacion':
                            print("Antiguo estado de liquidación: ")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['estado_liquidacion'])
                            cambioEstadoLiquidacion=input(f"Introduzca un nuevo estado entre los siguientes {estadosliquidacion}: ")
                            if cambioEstadoLiquidacion in estadosliquidacion:
                                for elto in lista_recibos:
                                    for subelto in elto:
                                        if subelto['id_recibo']==seleccionarID:
                                            subelto['estado_liquidacion']=cambioEstadoLiquidacion
                                            print("Estado cambiado.\nRecibo modificado.")
                                            return lista_recibos, polizas
                       
                            else:
                                print("El cambio sugerido no se encuentra entre las opciones disponibles.")
                                return lista_recibos, polizas
                        case 'fecha_liquidacion':
                            print("Antigua fecha de liquidacion:")
                            for elto in lista_recibos:
                                for subelto in elto:
                                    if subelto['id_recibo']==seleccionarID:
                                        print(subelto['fecha_liquidacion'])
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
                                                subelto['fecha_liquidacion']=cambioFecha
                                    print("Fecha de liquidacion cambiada. \nRecibo modificado.")
                                    return lista_recibos, polizas
                            else:
                                print("Error. La fecha de cobro introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                return lista_recibos, polizas
                elif seleccionarCampo == ' ':
                    print("No es posible introducir un campo vacío. Por favor escriba datos.")
                    continue
                else:
                    print("Error. El campo escrito no se encuentra entre las opciones disponibles")
                    continue
def EliminarRecibo(listaRecibos: list) -> list:
    print("Bienvenido/a al asistente para eliminar recibos.")
    if not listaRecibos: #Comprobación de que la lista está vacía
        print("No hay recibos registrados actualmente. Volviendo al menú principal.")
        return listaRecibos
    print("A continuación se muestran los recibos disponibles:")
    for elto in listaRecibos:
        for subelto in elto:
            print(f"id_recibo: {subelto['id_recibo']}")
            pass
    seleccionarID=input("Introduzca el ID del recibo que desea eliminar >>> ") #MODIFICADO CON ANTIGUO INT
    for elto in listaRecibos:
        for recibo in elto:
            if recibo['id_recibo']==seleccionarID:
                if recibo['estado_recibo'] != 'P' and subelto['estado_recibo'] != 'C':
                    listaRecibos.remove(elto)
                    print(f"El recibo con ID {seleccionarID} ha sido eliminado.")
                    return listaRecibos
                else:
                    print("No se puede eliminar un recibo que esté VIGOR.\nUn recibo VIGOR está en estado (P)endiente o (C)obrado.")
                    return listaRecibos