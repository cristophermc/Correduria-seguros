#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín


id_recibo=0
def CrearRecibo(nrosPolizas:list, id_recibo:int) -> list:
    lista=[]
    print("Bienvenido/a al asistente de creación de recibos.\nPrimero seleccione un ID de póliza sobre la cual formalizar el recibo.")
    print("Se muestran a continuación una serie de números identificadores. Escoja el número sobre el cual crear un recibo asociado.")
    print(nrosPolizas)
    eleccion=int(input(">>>"))
    # global nro_poliza
    if eleccion in nrosPolizas:
        for identificador in nrosPolizas:
            if identificador==eleccion:
                nro_poliza=identificador
        print(f"Encontrado y emparejado. Identificador de la póliza: {nro_poliza}")
        print("Cargando otros datos...")
        print()
        print()
        print("Establecer ahora la fecha de inicio del recibo (DD/MM/AAAA).")
        while True:
            fecha_inicio=input(">>> ")
            if len(fecha_inicio)==10 and fecha_inicio[2]=='/' and fecha_inicio[5]=='/' and fecha_inicio[:2].isdigit() and fecha_inicio[3:5].isdigit() and fecha_inicio[6:].isdigit():
                fechaIn=fecha_inicio.split('/')
                listaAux=[]
                for elto in fechaIn:
                    elto=int(elto)
                    listaAux.append(elto)
                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                    print("Fecha de inicio válida. Registrando...")
                    break
                else:
                    print("Error. La fecha de inicio introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                    continue
        print()
        print()
        print("Cargando rutinas de estado de duración de un recibo...")
        duraciones=('A','S','T','M')
        while True:
            print("Las pólizas se cobran de manera:\n(A)nual\n(S)emestral\n(T)rimestral\n(M)ensual")
            print()
            duracion=input("Seleccione de entre las opciones anteriores >>> ").upper()
            if duracion in duraciones:
                print("Periodo de liquidación de póliza seleccionado con éxito.")
                break
            else:
                print("Error. Seleccione correctamente entre las opciones listadas anteriormente (Indicadas en el paréntesis).")
        print()
        print()
        while True:
            try:
                importe_cobrar=float(input("Escriba el monto a cobrar en cada vencimiento del periodo de liquidación >>> "))
            except:
                print("Error. Escriba solamente entradas numéricas decimales en el importe a cobrar.")
                continue
            else:
                print("Importe seleccionado.")
                break
        print()
        print('Estableciendo ahora la fecha de cobro')
        while True:
            fecha_cobro=input("DD/MM/AAAA >>> ")
            if len(fecha_cobro)==10 and fecha_cobro[2]=='/' and fecha_cobro[5]=='/' and fecha_cobro[:2].isdigit() and fecha_cobro[3:5].isdigit() and fecha_cobro[6:].isdigit():
                fechaCo=fecha_cobro.split('/')
                listaAux=[]
                for elto in fechaCo:
                    elto=int(elto)
                    listaAux.append(elto)
                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2025:
                    print("Fecha de cobro válida. Registrando...")
                    break
                else:
                    print("Error. La fecha de cobro introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                    continue
        print()
        print("Seleccionando ahora el estado en el cual se encuentra el recibo.")
        while True:
            estadosrecibos=['P', 'PB', 'C', 'CB', 'B']
            print("Escoje entre:\nPendiente: el recibo no ha sido pagado por el tomador\nPendiente_banco: el recibo tiene cobro bancario y no se ha informado de su  cobro.\nCobrado: el recibo ha sido cobrado en la agencia.\nCobrado_banco: el recibo ya ha sido cobrado mediante la domiciliación bancaria.\nBaja: el recibo se ha dado de baja.")
            print(f'{estadosrecibos} > En dicho orden')
            estado_recibo=input(">>> ")
            if estado_recibo in estado_recibo:
                print("Estado correctamente introducido.")
                break
            elif estado_recibo not in estado_recibo:
                print("Error. Seleccione entre las opciones listadas.")
                continue
            else:
                print("Error. Seleccione correctamente entre las opciones listadas.")
        print()
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
        print()
        print(f"Creando recibo asociado a la póliza con identificador {nro_poliza}")
        dNroRecibo={'id_recibo': id_recibo,
                'nro_poliza':nro_poliza,
                'fecha_inicio':fecha_inicio,
                'duracion':duracion,
                'importe_cobrar':importe_cobrar,
                'fecha_cobro': fecha_cobro,
                'estado_recibo':estado_recibo,
                'importe_pagar':importe_pagar,
                'estado_liquidacion': estado_liquidacion,
                'fecha_liquidacion': fecha_liquidacion}
        lista.append(dNroRecibo)
        print(f"Recibo creado con identificador {id_recibo}")
        return lista
    else:
        print("No se ha seleccionado ninguna identificación asociada a una póliza. Volviendo al menú principal.")
        return None

def ModificarRecibo(lista_recibos: list) -> list:

    #Se tienen que desempaquetar las claves primeramente para que podamos sacar dos colecciones:
    #Colección A: campos=[] - lista con los campos de cada uno de los recibos - En el contexto de nuestra aplicación lo usamos como verificador cuando el usuario trata de acceder a los datos
    #Colección B: lista_recibos=[] - lista con los datos completos recibos de la llamada de la función.
    if not lista_recibos:#1. Lo primero que hacemos es comprobar que la lista NO esté vacía. Si está VACIA la mandamos de vuelta y salimos al menú. 
        print("No hay recibos disponibles para modificar.")
        return lista_recibos
    if lista_recibos: #Si la lista efectivamente tiene datos dentro (el contexto es QUE NO ESTÉ VACÍA):
        print("Lista de recibos disponibles:")
        for elto in lista_recibos:
            for recibo in elto:
                print(f"ID Recibo: {recibo['id_recibo']} | Póliza: {recibo['nro_poliza']}")

        id_modificar = int(input("Introduzca el ID del recibo que desea modificar >>> "))
        if id_modificar==1:
            print("Esto es una prueba de acceso.")
            return lista_recibos
        else:
            print("No es 1, que es la clave de ruptura.")

        
        # for recibo in lista_recibos:
        #     if recibo['id_recibo'] == id_modificar:
        #         print(f"Recibo seleccionado: {recibo}")
        #         print("Seleccione qué desea modificar:\n1. Fecha de inicio\n2. Duración\n3. Importe a cobrar\n4. Fecha de cobro\n5. Estado del recibo\n6. Importe a pagar\n7. Estado de liquidación\n8. Fecha de liquidación")
        #         eleccion = int(input(">>> "))
                
        #         if eleccion == 1:
        #             print("Introduzca la nueva fecha de inicio (DD/MM/AAAA):")
        #             while True:
        #                 fecha_inicio = input(">>> ")
        #                 if len(fecha_inicio) == 10 and fecha_inicio[2] == '/' and fecha_inicio[5] == '/' and fecha_inicio[:2].isdigit() and fecha_inicio[3:5].isdigit() and fecha_inicio[6:].isdigit():
        #                     fechaIn = fecha_inicio.split('/')
        #                     listaAux = [int(el) for el in fechaIn]
        #                     if listaAux[0] >= 1 and listaAux[0] <= 31 and listaAux[1] >= 1 and listaAux[1] <= 12 and listaAux[2] >= 1900 and listaAux[2] <= 2025:
        #                         print("Fecha de inicio válida. Registrando...")
        #                         recibo['fecha_inicio'] = fecha_inicio
        #                         break
        #                     else:
        #                         print("Fecha no válida. Inténtelo de nuevo.")
        #                 else:
        #                     print("Formato incorrecto. Inténtelo de nuevo.")

        #         elif eleccion == 2:
        #             print("Seleccione una nueva duración: (A)nual, (S)emestral, (T)rimestral, (M)ensual.")
        #             duraciones = ('A', 'S', 'T', 'M')
        #             while True:
        #                 nueva_duracion = input(">>> ").upper()
        #                 if nueva_duracion in duraciones:
        #                     recibo['duracion'] = nueva_duracion
        #                     print("Duración actualizada con éxito.")
        #                     break
        #                 else:
        #                     print("Selección incorrecta. Inténtelo nuevamente.")

        #         elif eleccion == 3:
        #             print("Introduzca el nuevo importe a cobrar:")
        #             while True:
        #                 try:
        #                     nuevo_importe = float(input(">>> "))
        #                     recibo['importe_cobrar'] = nuevo_importe
        #                     print("Importe actualizado.")
        #                     break
        #                 except:
        #                     print("Entrada inválida. Inténtelo de nuevo.")

        #         elif eleccion == 4:
        #             print("Introduzca la nueva fecha de cobro (DD/MM/AAAA):")
        #             while True:
        #                 fecha_cobro = input(">>> ")
        #                 if len(fecha_cobro) == 10 and fecha_cobro[2] == '/' and fecha_cobro[5] == '/' and fecha_cobro[:2].isdigit() and fecha_cobro[3:5].isdigit() and fecha_cobro[6:].isdigit():
        #                     fechaCo = fecha_cobro.split('/')
        #                     listaAux = [int(el) for el in fechaCo]
        #                     if listaAux[0] >= 1 and listaAux[0] <= 31 and listaAux[1] >= 1 and listaAux[1] <= 12 and listaAux[2] >= 1900 and listaAux[2] <= 2025:
        #                         recibo['fecha_cobro'] = fecha_cobro
        #                         print("Fecha de cobro actualizada.")
        #                         break
        #                     else:
        #                         print("Fecha no válida. Inténtelo nuevamente.")
        #                 else:
        #                     print("Formato incorrecto. Inténtelo nuevamente.")

        #         elif eleccion == 5:
        #             print("Seleccione el nuevo estado del recibo:")
        #             estados_recibos = ['P', 'PB', 'C', 'CB', 'B']
        #             print("Pendiente: P\nPendiente_banco: PB\nCobrado: C\nCobrado_banco: CB\nBaja: B")
        #             while True:
        #                 nuevo_estado = input(">>> ")
        #                 if nuevo_estado in estados_recibos:
        #                     recibo['estado_recibo'] = nuevo_estado
        #                     print("Estado actualizado.")
        #                     break
        #                 else:
        #                     print("Entrada inválida. Inténtelo nuevamente.")

        #         elif eleccion == 6:
        #             print("Introduzca el nuevo importe a pagar:")
        #             while True:
        #                 try:
        #                     nuevo_importe_pagar = float(input(">>> "))
        #                     recibo['importe_pagar'] = nuevo_importe_pagar
        #                     print("Importe actualizado.")
        #                     break
        #                 except:
        #                     print("Entrada inválida. Inténtelo de nuevo.")

        #         elif eleccion == 7:
        #             print("Seleccione el nuevo estado de liquidación: (P)endiente o (L)iquidado.")
        #             while True:
        #                 nuevo_estado_liquidacion = input(">>> ").upper()
        #                 if nuevo_estado_liquidacion in ['P', 'L']:
        #                     recibo['estado_liquidacion'] = 'Pendiente' if nuevo_estado_liquidacion == 'P' else 'Liquidado'
        #                     print("Estado de liquidación actualizado.")
        #                     break
        #                 else:
        #                     print("Selección incorrecta. Inténtelo nuevamente.")

        #         elif eleccion == 8:
        #             print("Introduzca la nueva fecha de liquidación (DD/MM/AAAA):")
        #             while True:
        #                 fecha_liquidacion = input(">>> ")
        #                 if len(fecha_liquidacion) == 10 and fecha_liquidacion[2] == '/' and fecha_liquidacion[5] == '/' and fecha_liquidacion[:2].isdigit() and fecha_liquidacion[3:5].isdigit() and fecha_liquidacion[6:].isdigit():
        #                     fechaLq = fecha_liquidacion.split('/')
        #                     listaAux = [int(el) for el in fechaLq]
        #                     if listaAux[0] >= 1 and listaAux[0] <= 31 and listaAux[1] >= 1 and listaAux[1] <= 12 and listaAux[2] >= 1900 and listaAux[2] <= 2025:
        #                         recibo['fecha_liquidacion'] = fecha_liquidacion
        #                         print("Fecha de liquidación actualizada.")
        #                         break
        #                     else:
        #                         print("Fecha no válida. Inténtelo nuevamente.")
        #                 else:
        #                     print("Formato incorrecto. Inténtelo nuevamente.")

        #         else:
        #             print("Opción no válida.")
        #         return
        
        # print("No se encontró un recibo con ese ID.")

def EliminarRecibo(listaRecibos: list) -> list:
    print("Bienvenido/a al asistente para eliminar recibos.")
#[[{id_recibo}]] for for 
    if not listaRecibos: #Comprobación de que la lista está vacía
        print("No hay recibos registrados actualmente. Volviendo al menú principal.")
        return listaRecibos

    print("A continuación se muestran los recibos disponibles:")
    #for elemento in listaRecibos
    #for recibo in elemento

    for elemento in listaRecibos:
        for recibo in elemento:
            print(f"ID Recibo: {recibo['id_recibo']}, Número de Póliza: {recibo['nro_poliza']}, Estado: {recibo['estado_recibo']}")

    while True:
        try:
            id_recibo = int(input("Escriba el identificador del recibo que desea eliminar >>> "))
        except ValueError:
            print("Error. Introduzca un valor numérico válido.")
            continue

        # Buscar el recibo con el ID proporcionado
        recibo_encontrado = None
        for recibo in listaRecibos:
            if recibo['id_recibo'] == id_recibo:
                recibo_encontrado = recibo
                break

        if recibo_encontrado:
            print("Recibo encontrado:")
            print(f"ID Recibo: {recibo_encontrado['id_recibo']}, Número de Póliza: {recibo_encontrado['nro_poliza']}, Estado: {recibo_encontrado['estado_recibo']}")

            # Confirmar eliminación
            while True:
                confirmacion = input("¿Está seguro de que desea eliminar este recibo? (S/N) >>> ").upper()
                if confirmacion == 'S':
                    listaRecibos.remove(recibo_encontrado)
                    print("Recibo eliminado correctamente.")
                    return listaRecibos
                elif confirmacion == 'N':
                    print("Operación cancelada. Volviendo al menú principal.")
                    return listaRecibos
                else:
                    print("Error. Responda con 'S' o 'N'.")
        else:
            print("No se encontró ningún recibo con el identificador proporcionado. Intente nuevamente.")