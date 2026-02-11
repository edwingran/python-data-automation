# Automation Report – Excel con Python

Proyecto de automatización para el procesamiento, almacenamiento y visualización de datos a partir de archivos Excel utilizando **Python**.

Este proyecto simula un flujo real de trabajo de análisis de datos:

Excel → Procesamiento → Reportes → Base de datos → Gráficas → Dashboard

---

## 📌 Objetivo del proyecto

Automatizar el análisis de un archivo de ventas en Excel para:

- Calcular métricas clave
- Generar reportes automáticos
- Almacenar resultados en una base de datos SQLite
- Generar gráficas
- Visualizar la información en un dashboard interactivo

Este proyecto está orientado a prácticas de:

- Automatización de procesos
- Análisis de datos
- Persistencia en bases de datos
- Visualización de información

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Pandas
- OpenPyXL
- Excel (.xlsx)
- Matplotlib
- SQLite3
- Streamlit

---

## 📂 Estructura del proyecto
```
│   README.md
│   requirements.txt
│
├───data
│       supermarket_sales.xlsx
│
├───database
│       ventas.db
│
├───reportes
│       grafico_ventas_ciudad.png
│       resumen.xlsx
│       ventas_por_ciudad.xlsx
│
└───src
    │   charts.py
    │   dashboard.py
    │   database.py
    │   main.py
    │
    └───__pycache__
            charts.cpython-314.pyc
            database.cpython-314.pyc
```


---

## 📊 Funcionalidades

El proyecto realiza las siguientes acciones:

1. Lee un archivo Excel con datos de ventas.
2. Muestra las primeras filas del dataset para verificación.
3. Calcula:
   - Ventas totales
   - Ventas agrupadas por ciudad
   - Producto más vendido (por cantidad)
4. Genera automáticamente:
   - Un archivo Excel con ventas por ciudad.
   - Un archivo Excel con un resumen general.
5. Guarda resultados en una base de datos SQLite.
6. Genera gráficas automáticamente.
7. Muestra la información en un dashboard interactivo.

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio
- git clone https://github.com/tu-usuario/automation-report.git

### 2. Instalar dependencias
- pip install -r requirements.txt

### 3. Ejecutar el script
- python src/main.py  

   Esto genera:
   - Reportes en Excel.
   - Datos en la base de datos.
   - Gráficas en la carpeta reportes.

### 4. Ejecutar el dashboard
- streamlit run src/dashboard.py  

   Se abrirá automáticamente en el navegador.

Al finalizar, los reportes se generarán en la carpeta reportes/.

## 📁 Dataset

El archivo supermarket_sales.xlsx es un dataset público de ventas de supermercados, utilizado con fines educativos para prácticas de análisis y automatización.

## 📈 Posibles mejoras futuras

- Envío automático de reportes por correo.
- Dashboard web desplegado en la nube.
- API para consultar datos.
- Programación automática del script (cron o task scheduler)
- Filtros interactivos en el dashboard.

## 👤 Autor

Desarrollado por John Granada  
Ingeniero Físico | Automatización | Python | Análisis de Datos