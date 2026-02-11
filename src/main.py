import pandas as pd
from database import crear_base, guardar_resumen, guardar_ventas_ciudad
from charts import generar_grafico_ventas_ciudad



# Leer archivo Excel
df = pd.read_excel("data/supermarket_sales.xlsx")

# Mostrar primeras filas
print(df.head())

# Calcular ventas totales
ventas_totales = df["Total"].sum()

# Ventas por ciudad
ventas_ciudad = df.groupby("City")["Total"].sum()

# Producto más vendido
producto_top = df.groupby("Product line")["Quantity"].sum().idxmax()

# Crear resumen
resumen = pd.DataFrame({
    "Ventas Totales": [ventas_totales],
    "Producto más vendido": [producto_top]
})

# Guardar resultados
ventas_ciudad.to_excel("reportes/ventas_por_ciudad.xlsx")
resumen.to_excel("reportes/resumen.xlsx")

# Se crea la base de datos
crear_base()
guardar_resumen(ventas_totales, producto_top)
guardar_ventas_ciudad(ventas_ciudad)

# Genera gráficos
generar_grafico_ventas_ciudad()


print("Reporte generado correctamente")
