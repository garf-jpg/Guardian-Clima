import requests


def obtener_clima_ciudad_owm(ciudad, api_key):
    """
    Obtiene el clima actual de una ciudad utilizando OpenWeatherMap.
    """

    # Endpoint que devuelve información climática actual
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Parámetros enviados a la API
    parametros = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    try:
        # Realiza la consulta y espera hasta 10 segundos
        response = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        # Si la respuesta es correcta, devuelve el JSON recibido
        if response.status_code == 200:
            return response.json()

        print(f"Error al consultar OpenWeatherMap: {response.status_code}")

    except Exception as e:
        # Captura errores de conexión u otros problemas de la solicitud
        print(f"Error de conexión con OpenWeatherMap: {e}")

    return None
