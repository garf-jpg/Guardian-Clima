from google import genai


def obtener_consejo_ia_gemini(
    api_key_gemini,
    temperatura,
    condicion_clima,
    viento_kmh,
    humedad
):
    """
    Genera una recomendación de vestimenta utilizando
    Google Gemini a partir de las condiciones climáticas
    actuales.
    """

    try:
        # Crear el cliente que permitirá comunicarse
        # con la API de Gemini.
        client = genai.Client(api_key=api_key_gemini)

        # Prompt enviado a la IA con los datos del clima
        # y las instrucciones para generar la respuesta.
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

        # Solicitar a Gemini la generación del consejo.
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Si la respuesta contiene texto, devolverlo limpio.
        if response.text:
            return response.text.strip()

        # Caso poco frecuente donde Gemini responde
        # pero no devuelve contenido útil.
        return "No se pudo generar un consejo en este momento."

    except Exception as e:
        # Captura errores de conexión, autenticación
        # o problemas al utilizar la API.
        print(f"\nError al conectar con Gemini: {e}")

        return (
            "No se pudo generar el consejo con IA. "
            "Verificá la conexión o la API Key."
        )
