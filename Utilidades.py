#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
import random
def ValidarDocumento(documento:str) -> bool:
    documento=documento.upper()
    letras_dni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
 
    if documento[-1].isalpha() and documento[0:8].isdigit() and len(documento)==9: #-> DNI
        print("Documento detectado: DNI o documentación para persona física.")
        print("Validando...")
        letra=int(documento[0:8])%23
        if documento[-1]==letras_dni[letra]:
            print(f"El DNI {documento} es válido.")
            return True
        else:
            print("Error. El DNI no es válido.")
    elif documento[-1].isalpha() and documento[0].isalpha() and documento[0] in 'XYZ' and len(documento)==9 and documento[1:8].isdigit():
        print("Documento detectado: NIE o DNI extranjero.")
        print("Validando...")
        if documento[0]=='X':
           documento=documento.replace('X', '0', 1)
           letraNieX=int(documento[0:8])%23
           if documento[-1]==letras_dni[letraNieX]:
               print(f"El NIE {documento} es válido.")
               return True
           else:
                print("Error. El NIE no es válido.")
        elif documento[0]=='Y':
            documento=documento.replace('Y', '1', 1)
            letraNieX=int(documento[0:8])%23
            if documento[-1]==letras_dni[letraNieX]:
               print(f"El NIE {documento} es válido.")
               return True
            else:
                print("Error. El NIE no es válido.")
        elif documento[0]=='Z':
            documento=documento.replace('Z', '2', 1)
            letraNieX=int(documento[0:8])%23
            if documento[-1]==letras_dni[letraNieX]:
               print(f"El NIE {documento} es válido.")
               return True
            else:
                print("Error. El NIE no es válido.")

    elif documento[-1].isalpha() and documento[0].isalpha() and documento[0] in 'JABCDEFGHI' and len(documento)==9 and documento[1:8].isdigit() and documento[-1] in 'JABCDEFGHI':
        print("Documento detectado: NIF jurídico (Antiguo CIF).")
        print("Validando...")
            #reconvertimos la secuencia de números en una lista de enteros, trabajaremos con la lista más adelante.
        numeros=documento[1:8]
        tablaComparacion=['J','A','B','C','D','E','F','G','H','I']
        lista_str=list(numeros)
        lista_aux=[]
        for elto in lista_str:
            lista_aux.append(int(elto))
            #fuera de este bucle, ya tenemos la lista auxiliar que maneja los datos numéricos.
            #El algoritmo del CIF nos dice que primero tenemos que calcular el valor de A, que es la suma directa de los elementos en su posición par:
        a=0
        for i in range(0,7,2):
            a+=lista_aux[i]
        b=0
        for i in range(1,7,2):
            varAuxiliar=2*lista_aux[i]
            if varAuxiliar>9:
                b += (varAuxiliar % 10) + (varAuxiliar // 10)
            else:
                b += varAuxiliar
                
            #El algoritmo implica sumar A y B y el resultado es C
        c=a+b
        d=10-(c%10)
        if d==10:
            d=0
        if documento[-1].isdigit() and int(documento[-1]) == d:
            print(f"El NIF para personas físicas {documento} es válido.")
            return True
            
        elif documento[-1].isalpha() and documento[-1] == tablaComparacion[d]:
            print(f"El NIF para personas físicas {documento} es válido.")
            return True
        else:
            print("NIF (CIF) jurídico inválido.")
            #Ahora se hace el módulo de 10 de c para restarle a 10, eso es D, quien marca el número de control del documento
def ComprobarMatricula(matricula:str) -> bool: # -> EN CONSTRUCCIÓN
    print("Comprobando matrícula introducida...")
    if len(matricula)==7 and matricula[0:4].isdigit() and matricula[4:].isalpha() and matricula[4:] not in "ÑQ": #->Caso de matrícula ordinaria
        print("Matrícula identificada como 'Normal | Taxis y 'VTC'.")
        return True
    elif len(matricula)==7 and matricula[0:1].isalpha() and matricula[2:5].isdigit() and matricula[5:].isalpha():
        print("Matrícula identificada como 'Ciclomotores'.")
        return True
    else:
        print("Error. Matrícula no circunscrita como válida.")
        return False
def ComprobarIBAN(iban:str)->bool: #Función que transposiciona el IBAN introducido para calcular si el número de control es válido o no lo es mediante operaciones matemáticas modulares
    #NControl - ESCC NNNN NNNN NNNN NNNN NNNN // ES91 2100 0418 4502 0005 1332 IBAN VÁLIDO
    copiaNum=iban[2:4]
    iban_transpuesto = iban[4:] + '142800' 
    iban_transpuesto=int(iban_transpuesto)
    algoritmo=98-(iban_transpuesto%97)
    if str(algoritmo)==copiaNum:
        return True
    else:
        return False
def SerialPoliza(numeradorPoliza):
    numeradorPoliza+=1
    return numeradorPoliza
def SerialRecibo(numeradorRecibo):
    numeradorRecibo+=1
    return numeradorRecibo
def SerialSiniestro(numeradorSiniestro):
    numeradorSiniestro+=1
    return numeradorSiniestro
def ComprobarCorreoElectronico(direccion:str) -> bool:
    direccion_antes_arroba = direccion.partition('@')
    direccion_despues_punto = direccion_antes_arroba[2].partition(".")
    antes_arroba = direccion_antes_arroba[0]  # Parte antes de '@'
    dominio = direccion_despues_punto[0]      # Parte entre '@' y '.'
    extension = direccion_despues_punto[2]   # Parte después del '.'

    # Validar cada parte
    if (len(antes_arroba) > 2 and len(antes_arroba) <= 28 and 
        antes_arroba[0].isalpha() and              # La primera letra debe ser alfabética
        dominio.isalpha() and                      # El dominio debe ser solo letras
        len(extension) >= 2 and len(extension) <= 4 and 
        extension.isalpha()):                      # La extensión debe ser solo letras
        print("Dirección válida.")
        return True
    else:
        print("Dirección inválida.")
        return False

def RecogerBanlistPolizas(Polizas:list) -> list:
    banlist=[]
    for elto in Polizas:
        for subelto in elto:
            banlist.append(subelto['id_tomador'])
    return banlist
def RecogerBanlistTomador(tomador:list)-> list:
    banlist=[]
    for elto in tomador:
        for subelto in elto:
            banlist.append(subelto['id_tomador'])
    return banlist
def RecogerBanlistRecibo(recibos: list) -> list:
    banlist = []
    for elto in recibos:
        if elto:  
            for subelto in elto:
                banlist.append(subelto['nro_poliza']) 
    return banlist
def NumSiniestro(numSiniestro:int) ->str: #Toma un nº de siniestro inicializado en 0 y cuando se pasa a la función de creación se modifica.
    #aaaa-nro_correlativo
    #ESTRUCTURA ANTES DEL -
    letras='abcdefghijklmnñopqrstuvwxyz'
    NumIDSiniestro=''
    for i in range(4):
        NumIDSiniestro+=random.choice(letras).upper()
    NumIDSiniestro+='-'
    NumIDSiniestro+=str(numSiniestro)
    return NumIDSiniestro
def NumLiquidaciones(numeradorLiquidaciones:int)->int:
    numeradorLiquidaciones+=1
    return numeradorLiquidaciones












                
