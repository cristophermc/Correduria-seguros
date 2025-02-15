#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín

#espacio para modulación // librerías
import pickle
import os
from Polizas import EliminarPoliza
from Polizas import ModificarPoliza
from Polizas import CrearPoliza
from Tomadores import CrearTomador
from Tomadores import EliminarTomador
from Tomadores import ModificarTomador
from Estadisticas import estadisticasPolizas
from Estadisticas import estadisticasLiquidaciones
from Recibos import CrearRecibo
from Recibos import ModificarRecibo
from Recibos import EliminarRecibo
from Utilidades import SerialPoliza
from Utilidades import SerialRecibo
from Utilidades import SerialSiniestro
from Utilidades import RecogerBanlistPolizas
from Utilidades import RecogerBanlistTomador
from Utilidades import RecogerBanlistRecibo
from Utilidades import NumSiniestro
from Siniestros import CrearSiniestro
from Siniestros import ModificarSiniestro
from Siniestros import EliminarSiniestro
from Utilidades import NumLiquidaciones
from Liquidaciones import CrearLiquidacion
from Liquidaciones import CerrarLiquidacion
from Liquidaciones import ModificarLiquidacion
#espacio para definición de funciones internas del programa / rutinas necesarias para consolidar los datos

def DetectarDatosCarga()->list:
     '''funcion implementada en el programa principal para la deteccion de datos de carga. El usuario elige si 
     quiere cargar o no los datos detectados desde el directorio de /datos cogiendo el archivo guardado.gcs
     (.gcs quiere decir GUARDADO CORREDURIA SEGUROS) - devuelve listas'''
     if os.path.exists('../datos/guardado.gcs'):
          print("Detectado un punto de guardado con datos.")
          while True:
            cargar=input("¿Desea cargar los datos disponibles en el sistema de ficheros? s/n >>> ").lower()
            if cargar == 's':
                guardado=open('guardado.gcs', 'rb')
                carga = pickle.load(guardado)
                return carga
            elif cargar == 'n':
                print("Anulando la operación de carga de datos.\nProcediendo al normal funcionamiento del programa.")
                return None
            else:
                print("Responda afirmativamente entre s o n.")
     else:
          print("Archivos de guardado no encontrados en el sistema de archivos.\nProcediendo al normal funcionamiento del programa.")
          return None
def GuardarDatos(polizasRegistro, recibos, tomador, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos, numeradorSiniestro, siniestros, numeradorLiquidaciones, liquidaciones):  
    '''funcion que permite guardar y serializar los datos'''
    #definimos la ruta base del directorio
    ruta_datos = '../datos'
    ruta_archivo = os.path.join(ruta_datos, 'guardado.gcs')  #Ruta completa del archivo

    if os.path.exists(ruta_datos):  #Verificamos si existe el directorio
        print("Proceso de guardado de datos seleccionado.")
        print(f"Haciendo copia de seguridad de todos los datos en el sistema de ficheros en el directorio {ruta_datos}.")

        #lista de datos de guardado
        lista = [polizasRegistro, recibos, tomador, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos, numeradorSiniestro, siniestros, numeradorLiquidaciones, liquidaciones]

        #guardamos los datos en el archivo usando `with` para garantizar seguridad
        try:
            with open(ruta_archivo, 'wb') as guardado:
                pickle.dump(lista, guardado)

            #confirmar de alguna manera que el archivo se guardó correctamente
            if os.path.exists(ruta_archivo):
                print(f"El archivo se ha generado correctamente en: {os.path.abspath(ruta_archivo)}")
                print("Volviendo al menú principal.")
            else:
                print("Ha habido un error en el guardado de datos. Volviendo al menú principal.")
        except Exception as e: #levantamos la excepción en caso de error
            print(f"Error durante el guardado de datos: {e}")
            return None
    else:
        print("Directorio de trabajo inexistente. Asegúrese de tener una carpeta de nombre 'datos' en el directorio padre.")
        return None
if __name__=='__main__':
    os.chdir('./datos') #Cambiamos de directorio para controlar las entradas y salidas de datos / DIRECTORIO DE GUARDADO DE DATOS
    datos_cargados=DetectarDatosCarga() #Procedemos a la carga opcional de datos / ACCION DE PERSISTENCIA
    if datos_cargados:
        '''desempaquetamos los datos completamente y los cargamos en nuestro programa principal'''
        polizasRegistro, tomador, recibos, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos, numeradorSiniestro, siniestros, numeradorLiquidaciones, liquidaciones = datos_cargados
    else:
        '''si los datos no se cargan, creamos las estructuras de datos pertinentes'''
        polizasRegistro=[] #listado de pólizas que actualmente existen / o si no existen, directorio de guardado
        tomador=[]
        recibos=[]
        siniestros=[]
        liquidaciones=[]
        numeradorPoliza=0
        numeradorRecibo=0
        numeradorSiniestro=0
        numeradorLiquidaciones=0
        banlistPolizas=[]
        banlistTomadores=[]
        banlistRecibos=[]
        
    while True: #bucle principal del programa - incluye todas las subrutinas necesarias para el funcionamiento de la aplicación a modelo teórico
        print("----------------------------------------")
        print("\033[31mCorreduría 'Mi Coche Asegurado'\033[0m")
        print(".----------------.")
        print("|\033[35m Menú Principal\033[0m |")
        print("'----------------'")
        print(" ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
        print(f"┇ \033[94m1. ★  Pólizas\033[0m           ┇\n┇ \033[92m2. ⬤  Tomadores\033[0m         ┇\n┇ \033[93m3. €  Recibos\033[0m           ┇\n┇ \033[91m4. ⚠  Siniestros\033[0m        ┇\n┇ \033[95m5. ✉  Liquidaciones\033[0m     ┇\n┇ \033[96m6. 🛈  Estadísticas\033[0m      ┇\n┇ \033[38;5;214m7. ❂  Guardado de datos\033[0m ┇\n┇ \033[38;5;130m9. ⏏  Salir\033[0m             ┇")
        print(" ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
        eleccion=input("Haga su elección escribiendo el número figurado en cada una de las opciones listadas anteriormente >>> ")
        match eleccion:
            case '1':
                while True:
                    print("Menú de pólizas")
                    print()
                    print(f"Pólizas creadas actualmente > {polizasRegistro}")
                    print(banlistPolizas)
                    print("1. Crear póliza\n2. Modificar póliza\n3. Eliminar póliza\n4. Retorno a menú principal")
                    elePolizas=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match elePolizas:
                        case '1':
                            if not tomador:
                                print("Error. Deben haber tomadores registrados previamente en la base de datos.\n Volviendo al menú.")
                                break
                            else:
                                numeradorPoliza=SerialPoliza(numeradorPoliza)
                                nuevaPoliza=CrearPoliza(numeradorPoliza, tomador, banlistPolizas)
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
                                    polizasRegistro, banlistPolizas, tomadores=ModificarPoliza(polizasRegistro, banlistPolizas, tomador)
                                else:
                                    print("Se ha encontrado un error. No existen pólizas registradas.")

                        case '3':
                            if polizasRegistro:
                                polizasRegistro, banlistPolizas, tomador, banlistTomadores, recibos, banlistRecibos, siniestros=EliminarPoliza(polizasRegistro, banlistPolizas, tomador, banlistTomadores, recibos, banlistRecibos, siniestros)
                                
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
                    print(banlistTomadores)
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
                                tomador,polizasRegistro, banlistTomadores, banlistPolizas=EliminarTomador(tomador, polizasRegistro, banlistTomadores, banlistPolizas) 
                                break
                            if polizasRegistro:
                                #Se pasa el tomador, y se devuelve una lista con el elemento eliminado.
                                #También se debe eliminar el registro de una póliza.
                                tomador, polizasRegistro, banlistTomadores, banlistPolizas=EliminarTomador(tomador, polizasRegistro, banlistTomadores, banlistPolizas)
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
                                numeradorRecibo = SerialRecibo(numeradorRecibo) 
                                nuevoRecibo = CrearRecibo(numeradorRecibo, banlistRecibos, polizasRegistro)
                                if nuevoRecibo is None:
                                    print("Volviendo al menú principal.")
                                    break
                                else:
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
                                recibos, polizasRegistro=ModificarRecibo(recibos, polizasRegistro)
                                break
                        case '3':
                            if not recibos:
                                print("No hay recibos registrados para eliminar.")
                            if not polizasRegistro:
                                print("No hay registros de pólizas para asociar.")
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
                    print(siniestros)
                    print("1. Crear siniestro\n2. Modificar siniestro\n3. Eliminar siniestro\n4. Retorno a menú principal")
                    eleLiquidacion=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match eleLiquidacion:
                        case '1':
                            print("Asistente de creación de siniestros.")
                            if not polizasRegistro:
                                print("No se detectaron pólizas en el registro. Debe existir al menos una póliza registrada para poder\nfacilitar un siniestro sobre la misma.\n\nVolviendo al menú principal.")
                                break
                            else:
                                print("Continuando con el proceso de creación de siniestros...")
                                serial=''
                                numeradorSiniestro=SerialSiniestro(numeradorSiniestro)
                                serial=NumSiniestro(numeradorSiniestro)
                                nuevoSiniestro=CrearSiniestro(serial, polizasRegistro)
                                siniestros.append(nuevoSiniestro)
                        case '2':
                            siniestros=ModificarSiniestro(siniestros)
                            break
                        case '3':
                            siniestros=EliminarSiniestro(siniestros)
                            break
                        case '4':
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("Error. Seleccione una de las opciones numéricas.")

            case '5':
                while True:
                    print("------------------")                    
                    print("Menú de liquidaciones")
                    print()
                    print(liquidaciones)
                    print("1. Generar liquidación\n2. Modificar liquidación\n3. Cerrar liquidación\n4. Retorno a menú principal")
                    eleLiquidacion=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match eleLiquidacion:
                        case '1':
                            print("Asistente de generación de liquidaciones.")
                            if siniestros and recibos: #la validación se hace por fuera (no es necesario hacerla dentro de la función)
                                numeradorLiquidaciones=NumLiquidaciones(numeradorLiquidaciones)
                                nuevaLiquidacion=CrearLiquidacion(recibos, siniestros, numeradorLiquidaciones)
                                liquidaciones.append(nuevaLiquidacion)
                            #casos donde no hay ni una cosa, ni la otra, o las dos a la vez
                            if not siniestros and not recibos:
                                print("No hay registros de siniestros ni recibos. Volviendo al menú principal.")
                                break
                            if siniestros and not recibos:
                                print("Hay registros de siniestros pero no hay registros de recibos.\nCree un recibo para poder formalizar una liquidación.")
                                break
                            if not siniestros and recibos:
                                print("No hay siniestros registrados.\nFormalice primero un siniestro.")
                                break
                        case '2':
                            if siniestros and recibos and liquidaciones:
                                liquidaciones=ModificarLiquidacion(liquidaciones, siniestros, recibos)
                                break
                            if not siniestros:
                                print("No hay siniestros registrados para poder modificar en orden.")
                                break
                            if not recibos:
                                print("No hay recibos al día para poder modificar.")
                                break
                            if not liquidaciones:
                                print("No hay liquidaciones registradas en la base de datos.")
                                break
                        case '3':
                            if not siniestros and not recibos and not liquidaciones:
                                print("Error. Deben existir primeramente datos de siniestros, recibos y liquidaciones.")
                            else:
                                recibos, siniestros, liquidaciones = CerrarLiquidacion(recibos, siniestros, liquidaciones)
                            break
                        case '4':
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("Error. Seleccione una de las opciones numéricas.")
                    
            case '6':
                while True:
                    print("Menú de estadísticas\n\n1. Ver estadísticas de pólizas.\n2. Ver estadísticas de liquidaciones.\n3. Retorno al menú principal.")
                    eleccEstadisticas=input("Haga su elección escribiendo el número que corresponde a cada una de las opciones >>> ")
                    match eleccEstadisticas:
                        case '1':
                            if polizasRegistro: #si hay polizas
                                estadisticasPolizas(polizasRegistro)
                            else:
                                print("No hay pólizas registradas.\n Deberá primero formalizar una.\nVolviendo al menú principal.")
                                break
                        case '2':
                            if liquidaciones:
                                estadisticasLiquidaciones(liquidaciones)
                            else:
                                print("No hay liquidaciones creadas todavía.\nVolviendo al menú principal.")
                                break
                        case '3':
                            print("Volviendo al menú principal.")
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
                        GuardarDatos(polizasRegistro, tomador, recibos, numeradorPoliza, numeradorRecibo, banlistPolizas, banlistTomadores, banlistRecibos, numeradorSiniestro, siniestros, numeradorLiquidaciones, liquidaciones)
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