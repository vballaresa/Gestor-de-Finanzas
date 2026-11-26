import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

ingresos = []
gastos = []

def guardar_datos():
        tipo_dato = tipo.get()
        nombre = name.get().strip()
        monto = mount.get().strip().replace(",", ".")

        if not nombre or not monto:
            tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        try:
            monto = float(monto)
        except ValueError:
            tk.messagebox.showerror("Error", "El monto debe ser un número válido.")     
            return
        if monto < 0:
            tk.messagebox.showerror("Error", "El monto no puede ser negativo.")
            return
        if tipo_dato == "Ingresos":
            ingresos.append((nombre, monto))
            lista.insert(tk.END, f"Ingreso: {nombre} - Monto: {monto}")
        else:
            gastos.append((nombre, monto))
            lista.insert(tk.END, f"Gasto: {nombre} - Monto: {monto}")

            ingresos_total = sum(monto_ingreso for _, monto_ingreso in ingresos)
            gastos_total =sum(monto_gasto for _, monto_gasto in gastos)
            ahorros = ingresos_total - gastos_total
            inicio.config(text=f"Total de ingresos: {ingresos_total:.2f} | Total de gastos: {gastos_total:.2f} | Ahorros: {ahorros:.2f}")
        name.delete(0, tk.END)
        mount.delete(0, tk.END)

def generar_grafico():
    ingresos_total = sum(monto_ingreso for _, monto_ingreso in ingresos)
    gastos_total =sum(monto_gasto for _, monto_gasto in gastos)
    ahorros = ingresos_total - gastos_total

    if ingresos_total <= 0:
        tk.messagebox.showinfo("Información", "No se puede crear un gráfico de pastel ya que el total de ingresos es cero o negativo.")
        return
    elif ahorros < 0:
        tk.messagebox.showwarning("Advertencia", f"Cuidado, los gastos superan a los ingresos por {abs(ahorros):.2f} entras en deficit.")
        etiquetas = [nombre for nombre, _ in gastos]
        valores = [monto for _, monto in gastos]
    else:
        etiquetas = ['Ingresos', 'Gastos', 'Ahorros']
        valores = [ingresos_total, gastos_total, ahorros]

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Ingresos y Gastos')
    plt.axis('equal')
    plt.show()

ventana = tk.Tk()
ventana.title("Gestor de Finanzas Personales v0.3")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, text="Bienvenido al gestor de finanzas personales v0.3")
etiqueta.pack(pady=5)

inicio = tk.Label(ventana, text="Ingrese el tipo bien sea Ingreso o Gasto")
inicio.pack(pady=5)
tipo = ttk.Combobox(ventana, values=["Ingresos", "Gastos"], state="readonly", width=20)
tipo.current(0)
tipo.pack(pady=(2, 8))

tk.Label(ventana, text="Ingrese el nombre del ingreso o gasto").pack(pady=5)
name = tk.Entry(ventana, width=30)
name.pack(pady=(2, 8))

tk.Label(ventana, text="Ingrese el monto del ingreso o gasto").pack(pady=5)
mount = tk.Entry(ventana, width=30)
mount.pack(pady=(2, 8))

guardar_button = ttk.Button(ventana, text="Agregar", command=guardar_datos)
guardar_button.pack(pady=10)

lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

grafico_button = ttk.Button(ventana, text="Generar gráfico", command=generar_grafico)
grafico_button.pack(pady=10)






ventana.mainloop()