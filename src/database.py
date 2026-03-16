import sqlite3
from contextlib import contextmanager

DB_PATH = "database/ventas.db"


@contextmanager
def _conectar():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn.cursor()
        conn.commit()
    finally:
        conn.close()


def crear_base():
    with _conectar() as cursor:
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


def guardar_resumen(ventas_totales, producto_top):
    with _conectar() as cursor:
        cursor.execute(
            "INSERT INTO resumen (ventas_totales, producto_top) VALUES (?, ?)",
            (ventas_totales, producto_top),
        )


def guardar_ventas_ciudad(ventas_ciudad):
    with _conectar() as cursor:
        for ciudad, total in ventas_ciudad.items():
            cursor.execute(
                "INSERT INTO ventas_ciudad (ciudad, total) VALUES (?, ?)",
                (ciudad, total),
            )
