#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
from Utilidades import ValidarDocumento
from Utilidades import ComprobarCorreoElectronico

#Separador -- - - - - - -- - - - 

'''Tendrá opciones para crear, modificar y eliminar a un tomador 
Cosas a tener en cuenta: 
•No se permiten tomadores con igual identificación. 
•En la opción modificar no se permite cambiar el identificador del tomador. 
•No se podrá eliminar un tomador que tenga alguna póliza vigente. 
•Si se puede borrar un tomador, se deben borrar todos los datos asociados a las 
pólizas que el tenía contratadas. 
'''
def CrearTomador(banlist:list) -> list:
    encontrado=False

    listaTomador=[]
    print("Bienvenido/a al creador de tomadores. En esta sencilla interfaz encontrarás un proceso sencillo para crear nuevos tomadores para las pólizas.\nEmpezemos...")
    print("¿Eres una (P)ersona física o una (E)mpresa?")
    while True:
        eleccionID=input("Escribe 'P' para persona física o 'E' para empresa >>> ").upper()
        if eleccionID=='P':
            print("A continuación procederemos a validar un DNI | NIE introducido por teclado.")
            id_tomador=input("Introduzca un DNI | NIE válido según la legislación española >>> ").upper()
            if ValidarDocumento(id_tomador):
                #VALIDACIÓN AHORA DE SI EL DNI | NIE | CIF YA ESTÁ EN LA BASE DE DATOS
                if id_tomador in banlist:
                    print("El documento ya se encuentra registrado en la base de datos.")
                    continue
                else:
                    print("Documento registrado satisfactoriamente.")
                    break
            else:
               print("Ha ocurrido un error con la validación del documento. DNI|NIE inválido.\nVuelva a introducir los datos pertinentes a un documento de identificación oficial para personas físicas.")
        elif eleccionID=='E':
            encontrado=False
            print("Se procede a validar un CIF | DNI para personalidades jurídicas por teclado.")
            id_tomador=input("Introduzca un CIF válido según la legislación española >>> ").upper()
            if ValidarDocumento(id_tomador):
                #VALIDACIÓN AHORA DE SI EL DNI | NIE | CIF YA ESTÁ EN LA BASE DE DATOS
                for sublista in listaTomador:
                    for diccionario in sublista:
                        if diccionario['id_tomador'] == id_tomador:
                            encontrado=True
                if encontrado:
                    print("El documento ya se encuentra registrado en la base de datos. Deberá registrar un documento válido distinto al registrado.")
                    continue
                if not encontrado:
                    print("Documento registrado satisfactoriamente.")
                    break
            else:
                print("Documento inválido. Pruebe de nuevo con otro documento CIF que sea susceptible de ser válido ante la legislación española.")
                continue
        else:
            print("Error al introducir el tipo de documento a validar.\nPor favor escriba entre 'P' o 'E'.")        
    #denominacion
    while True:   
        if eleccionID == 'P':
            denominacion=input("Escriba el nombre de la persona a la que hace referencia el documento: ")
            break
        elif eleccionID == 'E':
            denominacion=input("Escriba la denominación social que tiene la personalidad jurídica referenciada: ")
            break
  
    #fecha_nacimiento        
    while True:
        if eleccionID=='P':
            fecha_nacimiento=input("Detalle la fecha de nacimiento del tomador en el siguiente formato (DD/MM/AAAA) >>> ")
            if len(fecha_nacimiento)==10 and fecha_nacimiento[2]=='/' and fecha_nacimiento[5]=='/' and fecha_nacimiento[:2].isdigit() and fecha_nacimiento[3:5].isdigit() and fecha_nacimiento[6:].isdigit():
                fechaNac=fecha_nacimiento.split('/')
                listaAux=[]
                for elto in fechaNac:
                    elto=int(elto)
                    listaAux.append(elto)
                if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2006:
                    print("Fecha de nacimiento válida. Registrando...")
                    break
            else:
                print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                continue
        else:
            fecha_nacimiento=''
            break
      #domicilio    
    while True:
        domicilio=input("Determine el domicilio del figurante del documento: ")
        if domicilio!='':
            print("Datos guardados.")
            break
        else:
            print("Error. Este campo no puede estar vacío.")
    while True:
        try:
            movil_contacto=int(input("Escriba el teléfono móvil del tomador en el formato |AYUDA| (678022345) >>> "))
        except:
            print("Error. El formato debe ser numérico y con números enteros mayores a 0.")
        else:
            if len(str(movil_contacto))!=9:
                print("Error. El número de dígitos debe ser 9.")
            elif movil_contacto<0:
                print("Error. Las cifras del número no pueden ser negativas.")
            else:
                print("Teléfono registrado.")
                break
    while True:
        email_contacto=input("Escriba una dirección de correo electrónico para el tomador >>> ")
        if email_contacto != '':
            if ComprobarCorreoElectronico(email_contacto):
                break
            else:
                continue
        else:
            print("Error. El email no puede estar vacío.")
    dTomador={'id_tomador':id_tomador,
              'denominacion': denominacion,
              'fecha_nacimiento': fecha_nacimiento,
              'domicilio': domicilio,
              'movil_contacto':movil_contacto,
              'email_contacto':email_contacto
    }
    print(f"Cargando datos asociados al tomador con documento: {id_tomador}")
    print(f"Validados los datos. Volviendo al menú principal.")

    listaTomador.append(dTomador)
    return listaTomador
def ModificarTomador(listaTomador):
    print("Bienvenido/a a la opción de modificar tomadores.")

    # Validar si hay datos
    if not listaTomador:
        print("No hay tomadores registrados para modificar.")
        return listaTomador

    # Crear lista de IDs y lista de campos únicos excluyendo 'id_tomador'
    ID = []
    CAMPOS = []

    for dato in listaTomador:
        for valor in dato:
            # Añadir ID
            ID.append(valor['id_tomador'])
            # Añadir claves, verificando que no haya duplicados ni 'id_tomador'
            for clave in valor.keys():
                if clave != 'id_tomador' and clave not in CAMPOS:
                    CAMPOS.append(clave)

    while True:
        print("Esta es la lista de ID de tomadores para modificar.")
        print("----------------------------------------------------")
        for ident in ID:
            print(f"|{ident}|", end=' ')
        print("\n----------------------------------------------------")

        id_tomador = input("Ingrese el ID (DNI|NIE|CIF) que desea modificar de manera literal: ").upper()

        # Comprobar si el ID está en la lista
        if id_tomador in ID:
            print(f"Tomador encontrado con ID: {id_tomador}")
            print(f"Esta es la lista de campos disponibles para modificar:")
            for campo in CAMPOS:
                print(f"- {campo}")

            # Elegir el campo a modificar
            elegir_campo = input("Escriba de manera literal el nombre de uno de estos campos para MODIFICARLO >>> ")
            if elegir_campo in CAMPOS:  # Verificar si el campo es válido
                for elto in listaTomador:
                    for subelto in elto:
                        if subelto['id_tomador'] == id_tomador:
                            if elegir_campo == 'denominacion':
                                print(f"Antiguo valor de {elegir_campo}: {subelto[elegir_campo]}")
                                nuevo_valor = input(f"Ingrese el nuevo valor para {elegir_campo}: ")
                                if nuevo_valor:
                                    subelto[elegir_campo] = nuevo_valor
                                    print(f"{elegir_campo} modificado satisfactoriamente.")
                                    print("Volviendo al menú principal.")
                                    return listaTomador
                                else:
                                    print("Error: El nuevo valor no puede estar vacío.")
                                    continue
                            elif elegir_campo == 'fecha_nacimiento':
                                print(f"Antiguo valor de {elegir_campo}: {subelto[elegir_campo]}")
                                nuevo_valor = input(f"Ingrese el nuevo valor para {elegir_campo}: ")
                                if len(nuevo_valor)==10 and nuevo_valor[2]=='/' and nuevo_valor[5]=='/' and nuevo_valor[:2].isdigit() and nuevo_valor[3:5].isdigit() and nuevo_valor[6:].isdigit():
                                    FechaCambiar=nuevo_valor.split('/')
                                    listaAux=[]
                                    for elto in FechaCambiar:
                                        elto=int(elto)
                                        listaAux.append(elto)
                                    if listaAux[0]>=1 and listaAux[0]<=31 and listaAux[1]>=1 and listaAux[1]<=12 and listaAux[2]>=1900 and listaAux[2]<=2006:
                                         print("Fecha de nacimiento válida. Registrando...")
                                         subelto[elegir_campo]=nuevo_valor
                                         print("Volviendo al menú principal")
                                         return listaTomador
                                    else:
                                        print("Error. La fecha de nacimiento introducida no es válida. Por favor, introduzca una fecha en el formato DD/MM/AAAA.")
                                        continue
                         
            else:
                print("Error: El campo elegido no es válido. Intente nuevamente.")
                continue
        else:
            print("Error: El ID ingresado no está registrado. Intente nuevamente.")
            return listaTomador
            # for tomador in listaTomador:
            #     for dato in tomador:
            #         if dato['id_tomador'] == id_tomador:
            #             encontrado = True
            #             print(f"Tomador encontrado: {tomador}")
            #             print("Puede modificar los siguientes campos: denominación, domicilio, móvil, email.")

            #         # Modificar denominación
            #         nueva_denominacion = input("Nueva denominación (dejar en blanco para no cambiar): ")
            #         if nueva_denominacion:
            #             tomador['denominacion'] = nueva_denominacion

            #         # Modificar domicilio
            #         nuevo_domicilio = input("Nuevo domicilio (dejar en blanco para no cambiar): ")
            #         if nuevo_domicilio:
            #             tomador['domicilio'] = nuevo_domicilio

            #         # Modificar móvil
            #         while True:
            #             nuevo_movil = input("Nuevo móvil (dejar en blanco para no cambiar): ")
            #             if not nuevo_movil:
            #                 break
            #             if nuevo_movil.isdigit() and len(nuevo_movil) == 9:
            #                 tomador['movil_contacto'] = int(nuevo_movil)
            #                 break
            #             else:
            #                 print("Error: El número debe ser de 9 dígitos.")

            #         # Modificar email
            #         while True:
            #             nuevo_email = input("Nuevo email (dejar en blanco para no cambiar): ")
            #             if not nuevo_email:
            #                 break
            #             if ComprobarCorreoElectronico(nuevo_email):
            #                 tomador['email_contacto'] = nuevo_email
            #                 break
            #             else:
            #                 print("Error: Email no válido.")

            #         print("Datos actualizados correctamente.")
            #         break

            # if not encontrado:
            #     print("El documento ingresado no corresponde a ningún tomador registrado.")

            # return listaTomador

def EliminarTomador(listaTomador, listaPolizas):
    print("Bienvenido/a a la opción de eliminar tomadores.")
    if not listaTomador:
        print("No hay tomadores registrados para eliminar.")
        return listaTomador, listaPolizas

    id_tomador = input("Ingrese el documento del tomador que desea eliminar: ").upper()
    encontrado = False

    for tomador in listaTomador:
        if tomador['id_tomador'] == id_tomador:
            encontrado = True

            # Verificar si tiene pólizas vigentes
            tiene_polizas = any(poliza['id_tomador'] == id_tomador for poliza in listaPolizas)

            if tiene_polizas:
                print("No se puede eliminar este tomador porque tiene pólizas vigentes.")
                return listaTomador, listaPolizas

            # Eliminar las pólizas asociadas (si las hubiera, pero no están vigentes)
            listaPolizas = [poliza for poliza in listaPolizas if poliza['id_tomador'] != id_tomador]

            # Eliminar el tomador
            listaTomador.remove(tomador)
            print("Tomador y datos asociados eliminados correctamente.")
            break

    if not encontrado:
        print("El documento ingresado no corresponde a ningún tomador registrado.")

    return listaTomador, listaPolizas
