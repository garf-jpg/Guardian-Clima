# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# =========================
# DATOS DEL GRUPO
# =========================

INTEGRANTES = [
    "Elena Lucia Serrizuela",
    "Sofia Olivia Cho",
    "Olivia Stegmann",
    "Tizianna Zotti"

]

NOMBRE_GRUPO = "COMPLETAR_NOMBRE_GRUPO"

# =========================
# CONFIGURACIÓN
# =========================

MODELO_GEMINI = os.getenv("MODELO_GEMINI", "gemini-1.5-flash")

USUARIOS_CSV = "usuarios.csv"
HISTORIAL_CSV = "historial_global.csv"


def obtener_api_keys():
    """
    Obtiene las API keys desde el archivo .env
    """

    owm_key = os.getenv("OPENWEATHERMAP_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")

    if not owm_key:
        raise ValueError(
            "No se encontró OPENWEATHERMAP_API_KEY en el archivo .env"
        )

    if not gemini_key:
        raise ValueError(
            "No se encontró GEMINI_API_KEY en el archivo .env"
        )

    return owm_key, gemini_key, False
