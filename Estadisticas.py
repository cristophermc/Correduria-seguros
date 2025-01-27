#Cristopher Méndez Cervantes | Ángel Cristo Castro Martín

''' Dado un número de póliza se debe mostrar toda la información que de ella se 
dispone.
• Dado un número de liquidación se debe mostrar toda la información de la 
liquidación.
'''

def MostrarEstadisticaPolizas(Polizas:list, localizador:int):
    for lista in Polizas:
        for sublista in lista:
            if sublista['nro_poliza']==localizador:
                print("¡Poliza localizada! mostrando datos:")
                for clave, valor in sublista.items():
                    print(f"{clave}:\t{valor}")
                return sublista
    print(f"No se encontró en el sistema ninguna póliza con ID localizador {localizador}")
    return None #PISTA para el de Tomadores