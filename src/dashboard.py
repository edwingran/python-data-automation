import streamlit as st
import sqlite3
import pandas as pd

st.title("Dashboard de Ventas")

# Conectar a la base de datos
conn = sqlite3.connect("database/ventas.db")

# Leer resumen
resumen = pd.read_sql_query("SELECT * FROM resumen", conn)

st.subheader("Resumen General")
st.dataframe(resumen)

# Leer ventas por ciudad
ventas_ciudad = pd.read_sql_query("SELECT ciudad, total FROM ventas_ciudad", conn)

st.subheader("Ventas por Ciudad")
st.dataframe(ventas_ciudad)

# Gráfico
st.subheader("Gráfico de ventas por ciudad")
st.bar_chart(ventas_ciudad.set_index("ciudad"))

conn.close()
