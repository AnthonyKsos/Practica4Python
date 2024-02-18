def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith('.py'):
        print("El archivo no es un archivo Python (.py)")
        return

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            lineas_codigo = [linea for linea in lineas if not linea.strip().startswith('#') and linea.strip() != '']
            return len(lineas_codigo)
    except FileNotFoundError:
        print("La ruta del archivo es inválida o el archivo no existe")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    numero_lineas = contar_lineas_codigo(ruta_archivo)
    if numero_lineas is not None:
        print(f"Número de líneas de código: {numero_lineas}")

if __name__ == "__main__":
    main()