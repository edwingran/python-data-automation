# Automation Report – Excel con Python

Proyecto de automatización para el procesamiento y generación de reportes a partir de archivos Excel utilizando **Python y Pandas**.

Este script permite analizar datos de ventas, calcular métricas clave y generar reportes automáticos en formato Excel, simulando un escenario real de automatización de procesos administrativos o de negocio.

---

## 📌 Objetivo del proyecto

Automatizar el análisis de un archivo de ventas en Excel para:

- Calcular el total de ventas
- Obtener las ventas agrupadas por ciudad
- Identificar el producto más vendido
- Generar reportes automáticos en archivos Excel

Este proyecto está orientado a prácticas de **automatización, análisis de datos y scripting en Python**.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Pandas
- OpenPyXL
- Excel (.xlsx)

---

## 📂 Estructura del proyecto
```
automation-report
│
├── data
│   └── supermarket_sales.xlsx
│
├── reportes
│   ├── ventas_por_ciudad.xlsx
│   └── resumen.xlsx
│
├── src
│   └── main.py
│
├── README.md
└── requirements.txt
```


---

## 📊 Funcionalidades

El script realiza las siguientes acciones:

1. Lee un archivo Excel con datos de ventas.
2. Muestra las primeras filas del dataset para verificación.
3. Calcula:
   - Ventas totales
   - Ventas agrupadas por ciudad
   - Producto más vendido (por cantidad)
4. Genera automáticamente:
   - Un archivo Excel con ventas por ciudad.
   - Un archivo Excel con un resumen general.

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio
- git clone https://github.com/tu-usuario/automation-report.git

### 2. Instalar dependencias
- pip install -r requirements.txt

### 3. Ejecutar el script
- python src/main.py  

Al finalizar, los reportes se generarán en la carpeta reportes/.

## 📁 Dataset

El archivo supermarket_sales.xlsx es un dataset público de ventas de supermercados, utilizado con fines educativos para prácticas de análisis y automatización.

## 📈 Posibles mejoras futuras

- Modularizar el código usando funciones

- Manejo de errores (try/except)

- Parámetros por línea de comandos

- Envío automático de reportes por correo

- Visualización de datos con gráficos

- Integración con bases de datos (SQL)

## 👤 Autor

Desarrollado por John Granada  
Ingeniero Físico | Automatización | Python | Análisis de Datos