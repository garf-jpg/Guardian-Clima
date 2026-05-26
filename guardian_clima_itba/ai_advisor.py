# -*- coding: utf-8 -*-

from google import genai


def obtener_consejo_ia_gemini(
    api_key_gemini,
    temperatura,
    condicion_clima,
    viento_kmh,
    humedad
):
    """
    Genera un consejo de vestimenta utilizando Google Gemini
    según las condiciones climáticas actuales.
    """

    try:
        # Crear cliente
        client = genai.Client(api_key=api_key_gemini)

        # Prompt para la IA
        prompt = f"""
Sos un asistente de clima y vestimenta.

Datos actuales:
- Temperatura: {temperatura}°C
- Condición climática: {condicion_clima}
- Viento: {viento_kmh} km/h
- Humedad: {humedad}%

Generá un consejo breve y claro sobre:
- Qué ropa usar
- Si conviene llevar abrigo
- Si conviene llevar paraguas
- Precauciones útiles según el clima

Máximo 3 oraciones.
"""

        # Generar respuesta
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        # Validar respuesta
        if response.text:
            return response.text.strip()

        return "No se pudo generar un consejo en este momento."

    except Exception as e:
        print(f"\nError al conectar con Gemini: {e}")

        return (
            "No se pudo generar el consejo con IA. "
            "Verificá la conexión o la API Key."
        )