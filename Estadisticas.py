#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín
def estadisticasPolizas(polizas:list)->str:
    '''funcion que recoje de polizas sus ID e interactivamente el usuario seleccionando un num identificatorio es capaz
    de imprimir informacion de las mismas en pantalla'''
    ID=[]
    for elto in polizas:
        for subelto in elto:
            print(f"- Nº póliza: {subelto['nro_poliza']}")
            ID.append(subelto['nro_poliza'])

    try:
        seleccion=input("Escriba literalmente el número de póliza al que quiere acceder >>> ")
    except:
        print("Error. Sólo se puede acceder mediante valores numéricos.")
    else:
        if seleccion in ID:
            for elto in polizas:
                for subelto in elto:
                    if subelto['nro_poliza']==seleccion:
                        for clave, valor in subelto.items():
                            print(f"\033[32m{clave} \033[0m : {valor}")
        else:
            print("Error. No se ha encontrado la póliza asociada.")

def estadisticasLiquidaciones(liquidaciones:list)->str:
    '''Exactamente lo mismo pero con liquidaciones'''
    for elto in liquidaciones:
        for subelto in elto:
            print(f"- Nº póliza: {subelto['nro_liquidacion']}")
    seleccion=input("Escriba literalmente el número de liquidación al que quiere acceder >>> ")
    print('-'*60)    
    for elto in liquidaciones:
        for subelto in elto:
            if subelto['nro_liquidacion']==seleccion:
                for clave, valor in subelto.items():
                    print(f"\033[32m{clave} \033[0m :{valor}")
                print('-'*60)
            else:
                print("No se ha encontrado una póliza asociada a esa selección.")
                return