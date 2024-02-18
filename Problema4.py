import requests

def obtener_precio_bitcoin_y_guardar():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si hay un error en la solicitud
        datos = respuesta.json()
        
        precio_bitcoin = datos["bpi"]["USD"]["rate_float"]  # Obtener el precio actual de Bitcoin en USD
        fecha_actualizacion = datos["time"]["updated"]  # Obtener la fecha de actualización del precio
        
        datos_a_escribir = f"Fecha de actualización: {fecha_actualizacion}\nPrecio de Bitcoin (USD): {precio_bitcoin}"
        
        # Escribir los datos en un archivo de texto
        with open("precio_bitcoin.txt", "w") as archivo:
            archivo.write(datos_a_escribir)
        
        print("Datos del precio de Bitcoin almacenados exitosamente")
    
    except requests.RequestException as error:
        print(f"Error al obtener el precio de Bitcoin: {error}")

if __name__ == "__main__":
    obtener_precio_bitcoin_y_guardar()