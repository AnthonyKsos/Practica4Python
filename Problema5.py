class TablaMultiplicar:
    def crear_tabla(self, n):
        if 1 <= n <= 10:
            with open(f"tabla_del_{n}.txt", "w") as archivo:
                for i in range(1, 11):
                    archivo.write(f"{n} * {i} = {n*i}\n")
            print(f"Tabla de multiplicar del {n} guardada correctamente")
        else:
            print("El número debe estar entre 1 y 10.")

    def mostrar_tabla(self, n):
        try:
            with open(f"tabla_del_{n}.txt", "r") as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print(f"No existe el archivo tabla_del_{n}.txt")

    def mostrar_linea_tabla(self, n, m):
        try:
            with open(f"tabla_del_{n}.txt", "r") as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= 10:
                    print(lineas[m-1])
                else:
                    print("El número de línea debe estar entre 1 y 10")
        except FileNotFoundError:
            print(f"No existe el archivo tabla_del_{n}.txt")

def main():
    tabla = TablaMultiplicar()
    while True:
        print("\nMenu")
        print("1. Crear archivo con tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entre 1 y 10: "))
            tabla.crear_tabla(n)
        elif opcion == "2":
            n = int(input("Ingrese un número entre 1 y 10 para mostrar su tabla de multiplicar: "))
            tabla.mostrar_tabla(n)
        elif opcion == "3":
            n = int(input("Ingrese el número de la tabla de multiplicar: "))
            m = int(input("Ingrese el número de línea a mostrar: "))
            tabla.mostrar_linea_tabla(n, m)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo")

if __name__ == "__main__":
    main()