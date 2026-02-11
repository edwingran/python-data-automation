import sqlite3


def crear_base():
    conn = sqlite3.connect("database/ventas.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ventas_totales REAL,
        producto_top TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas_ciudad (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ciudad TEXT,
        total REAL
    )
    """)

    conn.commit()
    conn.close()


def guardar_resumen(ventas_totales, producto_top):
    conn = sqlite3.connect("database/ventas.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO resumen (ventas_totales, producto_top)
        VALUES (?, ?)
    """, (ventas_totales, producto_top))

    conn.commit()
    conn.close()


def guardar_ventas_ciudad(ventas_ciudad):
    conn = sqlite3.connect("database/ventas.db")
    cursor = conn.cursor()

    for ciudad, total in ventas_ciudad.items():
        cursor.execute("""
            INSERT INTO ventas_ciudad (ciudad, total)
            VALUES (?, ?)
        """, (ciudad, total))

    conn.commit()
    conn.close()
