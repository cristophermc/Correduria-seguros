#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín

''' Dado un número de póliza se debe mostrar toda la información que de ella se 
dispone.
• Dado un número de liquidación se debe mostrar toda la información de la 
liquidación.
'''

def estadisticasPolizas(polizas:list):
    for elto in polizas:
        for subelto in elto:
            print(f"- Nº póliza: {subelto['nro_poliza']}")
    try:
        seleccion=int(input("Escriba literalmente el número de póliza al que quiere acceder >>> "))
    except:
        print("Error. Sólo se puede acceder mediante valores numéricos.")
    else:
        for elto in polizas:
            for subelto in elto:
                if subelto['nro_poliza']==seleccion:
                    for clave, valor in subelto.items():
                        print(f"{clave}: {valor}")
                else:
                    print("No se ha encontrado una póliza asociada a esa selección.")
                    return
def estadisticasLiquidaciones(liquidaciones:list):
    for elto in liquidaciones:
        for subelto in elto:
            print(f"- Nº póliza: {subelto['nro_liquidacion']}")
    seleccion=input("Escriba literalmente el número de liquidación al que quiere acceder >>> ")
    print('-'*60)    
    for elto in liquidaciones:
        for subelto in elto:
            if subelto['nro_liquidacion']==seleccion:
                for clave, valor in subelto.items():
                    print(f"\033[32m{clave}.\033[0m :{valor}")
                print('-'*60)
            else:
                print("No se ha encontrado una póliza asociada a esa selección.")
                return