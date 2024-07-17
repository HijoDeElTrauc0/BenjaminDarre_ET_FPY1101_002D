# empleados: juan perez;María García;Carlos López;Ana Martínez;Pedro Rodríguez;Laura Hernández;MiguelSánchez;Isabel Gómez;Francisco Díaz;Elena Fernández.
# sueldos: aleatorio entre $300.000 y $2.500.000 
# funciones de la aplicacion :Asignar sueldos aleatorios;Clasificar sueldos;Ver estadísticas;Reporte de sueldos;Salir del programa

import random
import csv

Empleados = ["Juan Perez","Maria Garcia","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández",
             "Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"] 
    
def Sueldos():
    Sueldos = {}
    for Empleado in Empleados:
        Sueldo = random.randint(300000,2500000)
        Sueldos[Empleado] = Sueldo
    return Sueldos

def clasificar_sueldos() -> None:
    sueldos_bajo_800000 = []
    sueldos_entre_800000_y_2000000 = []
    sueldos_sobre_2000000 = []

    for empleado, sueldo in Sueldos.items():
        if sueldo < 800000:
            sueldos_bajo_800000.append((empleado, sueldo))
        elif 800000 <= sueldo < 2000000:
            sueldos_entre_800000_y_2000000.append((empleado, sueldo))
        else:
            sueldos_sobre_2000000.append((empleado, sueldo))

    menu_clasificar_sueldos = '''
    1. sueldos menores a $800.000
    2. sueldos entre $800.000 y $2.000.000
    3. sueldos superiores a $2.000.000
    4. salir
    '''

    while True:
        print(menu_clasificar_sueldos)
        opcion = int(input("ingrese una opcion: "))
        while opcion < 1 or opcion > 4:
            opcion = int(input("ingrese una opcion del 1 al 4: "))
        if opcion == 1:
            print("sueldos menores de $800.000: ")
            for empleado, sueldo in sueldos_bajo_800000:
                print(f"{empleado}: {sueldo}")
            continue
        if opcion == 2:
            print("\nSueldos Entre $800.000 y $2.000.000: ")
            for empleado, sueldo in sueldos_entre_800000_y_2000000:
                print(f"{empleado}: {sueldo}")
            continue
        if opcion == 3:
            print("\nSueldos Mayores a $2.000.000: ")
            for empleado, sueldo in sueldos_sobre_2000000:
                print(f"{empleado}: {sueldo}")
            continue
        if opcion == 4:
            break


def max_sueldos(diccionario_sueldos):
    Mayor_sueldo = max(diccionario_sueldos, key=diccionario_sueldos.get)
    return Mayor_sueldo, diccionario_sueldos[Mayor_sueldo]

def min_sueldos(diccionario_sueldos):
    Menor_sueldo = min(diccionario_sueldos, key=diccionario_sueldos.get)
    return Menor_sueldo, diccionario_sueldos[Menor_sueldo]

def promedio_sueldos(diccionario_sueldos):
    Total_sueldos = sum(diccionario_sueldos.values())  
    Cantidad_empleados = len(diccionario_sueldos)  
    Promedio = Total_sueldos / Cantidad_empleados  
    return Promedio


def media_sueldos(diccionario_sueldos):
    sueldos = list(diccionario_sueldos.values())
    if not sueldos:
        raise ValueError("El diccionario de sueldos está vacío")
    producto = 1
    for sueldo in sueldos:
        producto *= sueldo
    media_geometrica = round(producto ** (1 / len(sueldos)))
    return media_geometrica

def estadisticas_de_sueldos():
    menu = '''
    1. Sueldo Máximo
    2. Sueldo Mínimo
    3. Sueldo Promedio
    4. Media Geométrica
    5. Salir
    '''

    while True:
        print(menu)
        op2=int(input('Ingrese opcion: '))
        while(op2<1 or op2>5):
            op2=int(input('Ingrese opcion del 1 al 5: '))
        if(op2==1):
            sueldos_empleados = Sueldos()
            empleado_max, sueldo_max = max_sueldos(sueldos_empleados)
            print(f"El empleado con el mayor sueldo es {empleado_max} con un sueldo de {sueldo_max}")

        if(op2==2):
            sueldos_empleados = Sueldos()
            empleado_min, sueldo_min = min_sueldos(sueldos_empleados)
            print(f"El empleado con el menor sueldo es {empleado_min} con un sueldo de {sueldo_min}")
        if(op2==3):
            sueldos_empleados = Sueldos()
            sueldo_promedio = promedio_sueldos(sueldos_empleados)
            print(f"El sueldo promedio es {sueldo_promedio:.2f}")
        if(op2==4):
            sueldos_empleados = Sueldos()
            try:
                media_geo = media_sueldos(sueldos_empleados)
                print(f"La media geométrica de los sueldos es: {media_geo}")
            except ValueError as e:
                print(f"Error: {e}")
            continue
        if(op2==5):
            break

def reportes_de_sueldos(sueldos_empleados):
    empleados_ordenados = sorted(sueldos_empleados.items(), key=lambda x: x[0], reverse=True)
    print("Nombre empleado sueldo base descuento AFP sueldo liquido")
    for empleado , sueldo in empleados_ordenados:
        sueldo_base = sueldo
        descuento_salud = sueldo_base *0.07
        descuento_AFP = sueldo_base *0.12
        Sueldo_liquido = sueldo_base - descuento_salud - descuento_AFP
        
        print(f"{empleado:<15} {round(sueldo_base):<10} {round(descuento_salud):<10} {round(descuento_AFP):<10} {round(Sueldo_liquido):<10}")
        
        
def salir():
    print("finalizando programa...\n Desarrollado por Benjamin Darre\nRut: 21.989.389-2")
    
def exportar_csv(sueldos_empleados):
    confirmacion = input("Desea exportar el archivo? (s/n): ")
    if confirmacion.lower() == "s":
        empleados_ordenados = sorted(sueldos_empleados.items(), key=lambda x: x[0], reverse=True)
        
        with open("sueldos.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre empleado","sueldo base","descuento salud","descuento AFP","sueldo liquido"])
            for empleado, sueldo in empleados_ordenados:
                sueldo_base = sueldo
                descuento_salud = sueldo_base *0.07
                descuento_AFP = sueldo_base *0.12
                Sueldo_liquido = sueldo_base - descuento_salud - descuento_AFP
                
                writer.writerow([empleado, round(sueldo_base), round(descuento_salud), round(descuento_AFP), round(Sueldo_liquido)])
        print("Se ha exportado el archivo 'sueldos.csv'")
    
        
        