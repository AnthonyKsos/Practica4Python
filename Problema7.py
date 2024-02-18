import requests
import sqlite3
from datetime import date, timedelta

def obtenerCambioDolar(fecha_consulta):
    endpoint = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha_consulta}"
    respuesta = requests.get(endpoint)
    datos = respuesta.json()
    compra_dolar = datos['compra']
    venta_dolar = datos['venta']
    return compra_dolar, venta_dolar

def inicializarBaseDatos(conexion):
    cursor_db = conexion.cursor()
    cursor_db.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        FECHA TEXT PRIMARY KEY,
                        COMPRA_DOLAR REAL,
                        VENTA_DOLAR REAL
                    )''')

def almacenarDatos(conexion, dia, compra, venta):
    cursor_db = conexion.cursor()
    cursor_db.execute("INSERT INTO sunat_info (FECHA, COMPRA_DOLAR, VENTA_DOLAR) VALUES (?, ?, ?)", (dia, compra, venta))

def recuperarInformacion():
    with sqlite3.connect('base.db') as conexion:
        cursor_db = conexion.cursor()
        cursor_db.execute("SELECT * FROM sunat_info")
        registros = cursor_db.fetchall()
    return registros

def mostrarRegistros(lista_registros):
    for registro in lista_registros:
        print(registro)

def main():
    # Conexión a la base de datos
    with sqlite3.connect('base.db') as conexion:
        inicializarBaseDatos(conexion)

        fecha_inicio = date(2023, 1, 1)
        fecha_fin = date(2023, 12, 31)

        periodo = timedelta(days=1)
        dia_actual = fecha_inicio

        while dia_actual <= fecha_fin:
            compra, venta = obtenerCambioDolar(dia_actual.strftime('%Y-%m-%d'))
            almacenarDatos(conexion, dia_actual.strftime('%Y-%m-%d'), compra, venta)
            dia_actual += periodo

    print("Información almacenada en 'base.db'")

    lista_registros = recuperarInformacion()
    mostrarRegistros(lista_registros)

if __name__ == "__main__":
    main()