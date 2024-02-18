import requests

def precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def calcular_costo_bitcoins(btcs, precio_usd):
    return btcs * precio_usd

def main():
    btcs = float(input("Ingrese la cantidad de bitcoins: "))
    precio_usd = precio_bitcoin()
    if precio_usd:
        costo_usd = calcular_costo_bitcoins(btcs, precio_usd)
        print(f"El costo actual de {btcs} Bitcoin(s): ${costo_usd:,.4f} USD")
    else:
        print("No se pudo obtener el precio actual de Bitcoin")

if __name__ == "__main__":
    main()