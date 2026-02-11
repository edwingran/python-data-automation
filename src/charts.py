import sqlite3
import matplotlib.pyplot as plt


def generar_grafico_ventas_ciudad():
    conn = sqlite3.connect("database/ventas.db")
    cursor = conn.cursor()

    cursor.execute("SELECT ciudad, total FROM ventas_ciudad")
    datos = cursor.fetchall()

    conn.close()

    ciudades = [fila[0] for fila in datos]
    totales = [fila[1] for fila in datos]

    plt.figure()
    plt.bar(ciudades, totales)
    plt.title("Ventas por Ciudad")
    plt.xlabel("Ciudad")
    plt.ylabel("Total de ventas")

    plt.savefig("reportes/grafico_ventas_ciudad.png")
    plt.close()

    print("Gráfico generado correctamente")
