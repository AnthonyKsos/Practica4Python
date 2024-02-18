import random
from pyfiglet import Figlet

def seleccionar_fuente():
    # Permite al usuario seleccionar una fuente o asigna una aleatoriamente
    figlet = Figlet()
    disponibles = figlet.getFonts()
    eleccion = input("Escriba la fuente deseada o presione Enter para una aleatoria: ").strip()
    if eleccion and eleccion in disponibles:
        return eleccion
    return random.choice(disponibles)

def obtener_texto():
    # Solicita al usuario que ingrese el texto a mostrar
    return input("Introduzca el texto a mostrar: ")

def mostrar_texto_con_fuente(texto, fuente):
    # Muestra el texto con la fuente especificada
    figlet = Figlet(font=fuente)
    print(figlet.renderText(texto))

def main():
    fuente = seleccionar_fuente()
    texto = obtener_texto()
    mostrar_texto_con_fuente(texto, fuente)

if __name__ == "__main__":
    main()