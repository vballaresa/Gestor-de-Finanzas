import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

print("Bienvenido al gestor de finanzas personales v0.1")

can_ingresos = input("Ingrese la cantidad de donde le llegan ingresos mensuales: ")
can_gastos = input("Ingrese la cantidad de sus gastos mensuales: ")
print("")

ingresos = []
gastos = []
for i in range(int(can_ingresos)):
    #Pedir los datos para hacer la tabla de ingresos
    print(f"Ingreso {i+1}:")
    name_ingreso = input(f"Ingrese el nombre del ingreso {i+1}: ")
    mount_ingreso = float(input(f"Ingrese el monto del ingreso {i+1}: "))
    ingresos_total = sum(mount_ingreso for _, mount_ingreso in ingresos)
    print("")
    ingresos.append((name_ingreso, mount_ingreso))

print(f"El total de ingresos es: {ingresos_total}")
print("")
print("La tabla de ingresos es la siguiente: ")
cabeceras_ingresos = ['Nombre del ingreso', 'Monto del ingreso']
print(tabulate(ingresos, headers=cabeceras_ingresos, tablefmt='psql'))



print("")
for o in range(int(can_gastos)):
    #Pedir los datos para hacer la tabla de gastos
    print(f"Gasto {o+1}:")
    name_gasto = input(f"Ingrese el nombre del gasto {o+1}: ")
    mount_gasto = float(input(f"Ingrese el monto del gasto {o+1}: "))
    gastos_total =sum(mount_gasto for _, mount_gasto in gastos)
    print("")
    gastos.append((name_gasto, mount_gasto))

print(f"El total de gastos es: {gastos_total}")
print("La tabla de gastos es la siguiente:")
cabeceras_gastos = ['Nombre del gasto', 'Monto del gasto']
print(tabulate(gastos, headers=cabeceras_gastos, tablefmt='psql'))
print("")

input("Presione Enter para salir...")