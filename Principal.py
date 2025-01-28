#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín

#espacio para modulación // librerías
import pickle
import os
import Polizas
import Tomadores
import Recibos
from Polizas import EliminarPoliza
from Polizas import ModificarPoliza
from Polizas import CrearPoliza
from Tomadores import CrearTomador
from Tomadores import EliminarTomador
from Tomadores import ModificarTomador
from Estadisticas import MostrarEstadisticaPolizas
from Recibos import CrearRecibo
from Recibos import ModificarRecibo
from Recibos import EliminarRecibo
from Utilidades import SerialPoliza
from Utilidades import SerialRecibo
from Utilidades import SerialSiniestro
from Siniestros import CrearSiniestro
from Utilidades import RecogerBanlistPolizas
from Utilidades import RecogerBanlistTomador
from Utilidades import RecogerBanlistRecibo
#espacio para definición de funciones internas del programa / rutinas necesarias para consolidar los datos

def DetectarDatosCarga():
     if os.path.exists('../datos/guardado.gcs'):
          print("Detectado un punto de guardado con datos.")
          while True:
            cargar=input("¿Desea cargar los datos disponibles en el sistema de ficheros? s/n >>> ").lower()
            if cargar == 's':
                guardado=open('guardado.gcs', 'rb')
                carga = pickle.load(guardado)
                return carga
            elif cargar == 'n':
                print("Anulando la operación de cargado de datos.\nProcediendo al normal funcionamiento del programa.")
                return None
            else:
                print("Responda afirmativamente entre s o n.")
     else:
          print("Archivos de guardado no encontrados en el sistema de archivos.\nProcediendo al normal funcionamiento del programa.")
          return None
def GuardarDatos(polizasRegistro, recibos, tomador, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos):  # MÁS PARÁMETROS EN UN FUTURO
    # Definimos la ruta base del directorio
    ruta_datos = '../datos'
    ruta_archivo = os.path.join(ruta_datos, 'guardado.gcs')  # Ruta completa del archivo

    if os.path.exists(ruta_datos):  # Verificamos si existe el directorio
        print("Proceso de guardado de datos seleccionado.")
        print(f"Haciendo copia de seguridad de todos los datos en el sistema de ficheros en el directorio {ruta_datos}.")

        # Crear la lista de datos a guardar
        lista = [polizasRegistro, recibos, tomador, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos]

        # Guardar los datos en el archivo usando `with` para garantizar seguridad
        try:
            with open(ruta_archivo, 'wb') as guardado:
                pickle.dump(lista, guardado)

            # Confirmar de alguna manera que el archivo se guardó correctamente
            if os.path.exists(ruta_archivo):
                print(f"El archivo se ha generado correctamente en: {os.path.abspath(ruta_archivo)}")
                print("Volviendo al menú principal.")
            else:
                print("Ha habido un error en el guardado de datos. Volviendo al menú principal.")
        except Exception as e:
            print(f"Error durante el guardado de datos: {e}")
            return None
    else:
        print("Directorio de trabajo inexistente. Asegúrese de tener una carpeta de nombre 'datos' en el directorio padre.")
        return None
if __name__=='__main__':
    os.chdir('./datos') #Cambiamos de directorio para controlar las entradas y salidas de datos / DIRECTORIO DE GUARDADO DE DATOS
    datos_cargados=DetectarDatosCarga() #Procedemos a la carga opcional de datos 
    if datos_cargados:
        polizasRegistro, tomador, recibos, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos = datos_cargados


    else:
        polizasRegistro=[] #listado de pólizas que actualmente existen / o si no existen, directorio de guardado
        tomador=[]
        recibos=[]
        siniestros=[]
        numeradorPoliza=0
        numeradorRecibo=0
        numeradorSiniestro=0
        banlistPolizas=[]
        banlistTomadores=[]
        banlistRecibos=[]
    while True:
        print("----------------------------------------")
        print("Correduría Mi Coche Asegurado")
        print()
        print("Menú Principal")
        print("...")
        print("...")
        print(f"1. Pólizas\n2. Tomadores\n3. Recibos\n4. Siniestros\n5. Liquidaciones\n6. Estadísticas\n7. Guardado de datos\n9. Salir")
        print()
        eleccion=input("Haga su elección escribiendo el número figurado en cada una de las opciones listadas anteriormente >>> ")
        match eleccion:
            case '1':
                while True:
                    print("Menú de pólizas")
                    print()
                    print(f"Pólizas creadas actualmente > {polizasRegistro}")
                    print("1. Crear póliza\n2. Modificar póliza\n3. Eliminar póliza\n4. Retorno a menú principal")
                    elePolizas=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match elePolizas:
                        case '1':
                                #Eliminar las lineas de abajo cuando implementemos la operación de tomador, la cual pasa parámetros a CrearPoliza /// Sugerida lista para registrar datos
                            if not tomador:
                                print("Error. Deben haber tomadores registrados previamente en la base de datos.\n Volviendo al menú.")
                                break
                            else:
                                numeradorPoliza=SerialPoliza(numeradorPoliza)
                                nuevaPoliza=Polizas.CrearPoliza(numeradorPoliza, tomador, banlistPolizas)
                                polizasRegistro.append(nuevaPoliza)
                                banlistPolizas=RecogerBanlistPolizas(polizasRegistro)
                                break
                        case '2':
                            if not tomador:
                                print("Error. Deben haber tomadores registrados previamente en la base de datos.")
                                print("¿Desea agregar un nuevo tomador ahora? s/n >>> ")
                                if input().lower() == 's':
                                    nuevoTomador = CrearTomador()
                                    tomador.append(nuevoTomador)
                                else:
                                    print("Operación cancelada. Volviendo al menú.")
                                break

                            if tomador:
                                print("Se procede a modificar una póliza")
                                if polizasRegistro:
                                    polizasRegistro=ModificarPoliza(polizasRegistro)
                                else:
                                    print("Se ha encontrado un error. No existen pólizas registradas.")

                        case '3':
                            if polizasRegistro:
                                for lista in polizasRegistro:
                                    for sublista in lista:
                                        if sublista['nro_poliza'] not in nrosPolizas:  # Verificar si ya existe
                                            nrosPolizas.append(sublista['nro_poliza'])
                                if nrosPolizas:
                                    print(f"Seleccione entre los distintos identificadores de pólizas para eliminarla\n{nrosPolizas}.")
                                    elimPol=int(input(">>> "))
                                    if elimPol in nrosPolizas:
                                        polizasRegistro=EliminarPoliza(elimPol, polizasRegistro)
                                        print("Poliza borrada. Actualizando datos...")
                                        print(polizasRegistro)
                                        print()
                                        print()
                                        print("Volviendo al menú principal...")
                                        break
                                if not nrosPolizas:
                                    print("Por ahora no hay pólizas para eliminar.")
                                    break
                            elif not polizasRegistro:
                                #por ahora no hay nada, por tanto mandamos a crear
                                print("No hay pólizas con las que trabajar. Volviendo al menú principal.")
                                break
                            
                        case '4':
                            print("Volviendo al menú principal.")
                            break
                        case _:
                            print("Error. Seleccione correctamente entre las opciones disponibles.")
                            continuar = input("¿Desea intentar nuevamente? (s/n): ").lower()
                            if continuar != 's':
                                break
     
            case '2':
                while True:
                    print("Menú de tomadores")
                    print()
                    print(f"Tomadores registrados actualmente > {tomador}")
                    print("1. Crear tomador\n2. Modificar tomador\n3. Eliminar tomador\n4. Retorno a menú principal")
                    eleTomadores=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match eleTomadores:
                        case '1':
                            if not tomador:
                                nuevoTomador=CrearTomador(banlistTomadores)
                                tomador.append(nuevoTomador)
                                banlistTomadores=RecogerBanlistTomador(tomador)
                                break
                            if tomador:
                                nuevoTomador=CrearTomador(banlistTomadores)
                                tomador.append(nuevoTomador)
                                banlistTomadores=RecogerBanlistTomador(tomador)
                                break
                        case '2':
                            tomador=ModificarTomador(tomador)
                            break
                        case '3':
                            if not polizasRegistro:
                                tomador,polizasRegistro=EliminarTomador(tomador, polizasRegistro) 
                                break
                            if polizasRegistro:
                                #Se pasa el tomador, y se devuelve una lista con el elemento eliminado.
                                #También se debe eliminar el registro de una póliza.
                                tomador, polizasRegistro=EliminarTomador(tomador, polizasRegistro)
                                break                               
                        case '4':
                            print("Volviendo al menú principal.")
                            break
                        case _:
                            print("Error. Seleccione correctamente entre las opciones disponibles.")

            case '3':
                while True:
                    print("------------------")
                    print("Menú de recibos")
                    print()
                    print("1. Crear recibo\n2. Modificar recibo\n3. Eliminar recibo\n4. Retorno a menú principal")
                    print(f"Recibos creados actualmente >>> {recibos}")
                    eleRecibo = input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    
                    match eleRecibo:
                        case '1':
                            if not polizasRegistro:
                                print("Error. Aún no hay pólizas registradas. Primeramente deberá existir una póliza en el registro para poder crear un recibo asociado. Volviendo al menú principal.")
                                break
                            elif polizasRegistro:
                                numeradorRecibo = SerialRecibo(numeradorRecibo) #No es del todo seriado
                                nuevoRecibo = CrearRecibo(numeradorRecibo, banlistRecibos, polizasRegistro)
                                recibos.append(nuevoRecibo)
                                banlistRecibos=RecogerBanlistRecibo(recibos)
                                break
                        case '2':
                            if not polizasRegistro:
                                print("No hay pólizas registradas sobre las cuales se tengan recibos asociados.")
                                break
                            if not recibos:
                                print("No hay recibos registrados para modificar.")
                            else:
                                recibos=ModificarRecibo(recibos, polizasRegistro)
                                break
                        case '3':
                            if not recibos:
                                print("No hay recibos registrados para eliminar.")
                            else:
                                recibos = EliminarRecibo(recibos)
                            break
                        case '4':
                            break
                        case _:
                            print("Error. Seleccione correctamente entre las opciones disponibles.")

            case '4':
                while True:
                    print("------------------")                    
                    print("Menú de siniestros")
                    print()
                    print("1. Crear siniestro\n2. Modificar siniestro\n3. Eliminar siniestro\n4. Retorno a menú principal")
                    print(f"Siniestros actuales > {siniestros}")
                    eleSiniestro=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match eleSiniestro:
                        case '1':
                            print("Asistente de creación de siniestros.")
                            if not polizasRegistro:
                                print("No se detectaron pólizas en el registro. Debe existir al menos una póliza registrada para poder\nfacilitar un siniestro sobre la misma.\n\nVolviendo al menú principal.")
                                break
                            else:
                                print("Continuando con el proceso de creación de siniestros...")
                                for lista in polizasRegistro:
                                        for sublista in lista:
                                            if sublista['nro_poliza'] not in nrosPolizas:  # Verificar si ya existe
                                                nrosPolizas.append(sublista['nro_poliza'])  # Solo añadir si no existe
                                numeradorSiniestro=SerialSiniestro(numeradorSiniestro)
                                nuevoSiniestro=CrearSiniestro(numeradorPoliza, nrosPolizas)
                                siniestros.append(nuevoSiniestro)
                        case '2':
                            print("En construcción. Saliendo al menú principal.")
                            break
                        case '3':
                            print("En construcción. Saliendo al menú principal.")
                            break
                        case '4':
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("Error. Seleccione una de las opciones numéricas.")

            case '5':
                pass
            case '6':
                while True:
                    print("Menú de estadísticas\n\n1. Ver estadísticas de pólizas.\n2. Ver estadísticas de liquidaciones.\n3. Retorno al menú principal.")
                    eleccEstadisticas=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match eleccEstadisticas:
                        case '1':
                            for lista in polizasRegistro:
                                for sublista in lista:
                                    nrosPolizas.append(sublista['nro_poliza'])
                            print(f"Nº de pólizas registrados > {nrosPolizas}")
                            try:
                                buscadorIdPoliza=int(input("Escriba uno de los números figurantes en la tabla de arriba para mostrar datos sobre pólizas registradas: "))
                            except:
                                print("El formato válido de inserción es una entrada de números.")
                            else:
                                MostrarEstadisticaPolizas(polizasRegistro, buscadorIdPoliza)
                            continue
                        case '2':
                            pass
                        case '3':
                            break
                        case _:
                            print("Error. Seleccione correctamente entre las opciones disponibles.")
            case '7':
                print("Procedimiento de guardado rutinario.")
                print()
                while True:
                    print("Antes de guardar tenga en cuenta que sobreescribirá todos los registros anteriores existentes.")
                    continuarGuarda=input("¿Desea continuar de todos modos? s/n >>> ").lower()
                    if continuarGuarda=='s':
                        GuardarDatos(polizasRegistro, tomador, recibos, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos)
                        break
                    elif continuarGuarda=='n':
                        print("Operación de guardado anulada. Volviendo al menú principal.")
                        break
                    else:
                        print("Error. Escriba adecuadamente la entrada entre s o n.")
            case '9':
                exit()
            case _:
                print("Error. Seleccione correctamente entre las opciones disponibles.")