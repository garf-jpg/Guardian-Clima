import requests


def obtener_clima_ciudad_owm(ciudad, api_key):
    """
    Consulta el clima actual de una ciudad utilizando OpenWeatherMap.
    """

    url = "https://api.openweathermap.org/data/2.5/weather"

    parametros = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    try:

        response = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        print(f"Error al consultar OpenWeatherMap: {response.status_code}")

    except Exception as e:
        print(f"Error de conexión con OpenWeatherMap: {e}")

    return None