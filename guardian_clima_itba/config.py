import os
from dotenv import load_dotenv

# Cargar automáticamente las variables definidas
# dentro del archivo .env al iniciar la aplicación.
load_dotenv()


# DATOS DEL GRUPO

INTEGRANTES = [
    "Elena Lucia Serrizuela",
    "Sofia Olivia Cho",
    "Olivia Stegmann",
    "Tiziana Zotti"
]

NOMBRE_GRUPO = "grupo 25"


# CONFIGURACIÓN

# Modelo de Gemini utilizado por defecto para
# generar recomendaciones de vestimenta.
MODELO_GEMINI = os.getenv(
    "MODELO_GEMINI",
    "gemini-2.5-flash"
)

# Archivos utilizados para persistir los datos
# de usuarios y consultas climáticas.
USUARIOS_CSV = "usuarios.csv"
HISTORIAL_CSV = "historial_global.csv"


def obtener_api_keys():
    """
    Obtiene las API Keys necesarias para el funcionamiento
    de la aplicación desde el archivo .env.
    """

    owm_key = os.getenv("OPENWEATHERMAP_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")

    # Verificar que la clave de OpenWeatherMap exista
    # antes de iniciar la aplicación.
    if not owm_key:
        raise ValueError(
            "No se encontró OPENWEATHERMAP_API_KEY en el archivo .env"
        )

    # Verificar que la clave de Gemini exista
    # antes de iniciar la aplicación.
    if not gemini_key:
        raise ValueError(
            "No se encontró GEMINI_API_KEY en el archivo .env"
        )

    return owm_key, gemini_key

