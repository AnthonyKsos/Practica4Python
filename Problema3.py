import requests
from zipfile import ZipFile
import os

def descargar_imagen(url, nombre_archivo):
    # Descarga una imagen y la guarda con el nombre de archivo especificado
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print("Imagen descargada")
    else:
        print("Error al descargar la imagen")

def comprimir_imagen(nombre_archivo_imagen, nombre_archivo_zip):
    # Comprime el archivo de imagen en un archivo zip
    with ZipFile(nombre_archivo_zip, 'w') as archivo_zip:
        archivo_zip.write(nombre_archivo_imagen, os.path.basename(nombre_archivo_imagen))
    print(f"Archivo '{nombre_archivo_imagen}' comprimido en '{nombre_archivo_zip}' exitosamente")

def descomprimir_imagen(nombre_archivo_zip, nombre_directorio_destino):
    # Extrae el contenido del archivo zip en un directorio específico
    os.makedirs(nombre_directorio_destino, exist_ok=True)
    with ZipFile(nombre_archivo_zip, 'r') as archivo_zip:
        archivo_zip.extractall(nombre_directorio_destino)
    print(f"Contenido de '{nombre_archivo_zip}' extraído en el directorio '{nombre_directorio_destino}'")

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_archivo_imagen = "imagen.jpg"
    nombre_archivo_zip = "imagen_comprimida.zip"
    nombre_directorio_destino = "imagen_descomprimidas"

    descargar_imagen(url_imagen, nombre_archivo_imagen)
    comprimir_imagen(nombre_archivo_imagen, nombre_archivo_zip)
    descomprimir_imagen(nombre_archivo_zip, nombre_directorio_destino)

if __name__ == "__main__":
    main()