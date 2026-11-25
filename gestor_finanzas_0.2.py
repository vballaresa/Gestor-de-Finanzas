import matplotlib.pyplot as plt
from tabulate import tabulate

print("Bienvenido al gestor de finanzas personales v0.2")

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
    print("")
    ingresos.append((name_ingreso, mount_ingreso))
    ingresos_total = sum(mount_ingreso for _, mount_ingreso in ingresos)
print("")


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
    print("")
    gastos.append((name_gasto, mount_gasto))
    gastos_total =sum(mount_gasto for _, mount_gasto in gastos)
print("")


print(f"El total de gastos es: {gastos_total}")
print("La tabla de gastos es la siguiente:")
cabeceras_gastos = ['Nombre del gasto', 'Monto del gasto']
print(tabulate(gastos, headers=cabeceras_gastos, tablefmt='psql'))
print("")

ahorros = ingresos_total - gastos_total
print(f"El total de ahorros es: {ahorros}")

#Crear un gráfico de pastel para visualizar los ingresos y gastos

if ingresos_total <= 0:
    print("No se puede crear un gráfico de pastel ya que el total de ingresos es cero o negativo.")
elif ahorros < 0:
    print(f"Cuidado, los gastos superan a los ingresos por {abs(ahorros):.2f} entras en deficit.")
    etiquetas = [nombre for nombre, _ in gastos]
    valores = [monto for _, monto in gastos]

    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels = etiquetas, autopct='1.1f%%', startangle=90)
    plt.title(f"Distribucion de gastos y Deficit vs Ingresos (Total de ingresos: {ingresos_total:.2f})")
    plt.axis('equal')   
    plt.tight_layout()
    plt.show()
else :
    etiquetas = [nombre for nombre, _ in gastos] + ["Ahorros"]
    valores = [monto for _, monto in gastos] + [ahorros]

    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels = etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title(f"Distribucion de ingresos mensuales (Total de ingresos: {ingresos_total:.2f})")
    plt.axis('equal')   
    plt.tight_layout()
    plt.show()


input("Presione Enter para salir...")