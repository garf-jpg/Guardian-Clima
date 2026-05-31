
import sys
from getpass import getpass

from config import (
    obtener_api_keys,
    INTEGRANTES,
    NOMBRE_GRUPO
)

import auth
import weather
import stats
import ai_advisor



# COLORES ANSI

RESET = "\033[0m"
NEGRITA = "\033[1m"

CELESTE = "\033[36m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
ROJO = "\033[31m"
MAGENTA = "\033[35m"



# UTILIDADES


def limpiar_pantalla():

    #Limpia parcialmente la consola.

    print("\n" * 3)


def mostrar_titulo():

    print(
        CELESTE
        + r"  ____ _   _   _    ____  ____ ___    _    _   _  ____ _     ___ __  __    _    "
        + RESET
    )

    print(
        CELESTE
        + r" / ___| | | | / \  |  _ \|  _ |_ _|  / \  | \ | |/ ___| |   |_ _|  \/  |  / \   "
        + RESET
    )

    print(
        CELESTE
        + r"| |  _| | | |/ _ \ | |_) | | | | |  / _ \ |  \| | |   | |    | || |\/| | / _ \  "
        + RESET
    )

    print(
        CELESTE
        + r"| |_| | |_| / ___ \|  _ <| |_| | | / ___ \| |\  | |___| |___ | || |  | |/ ___ \ "
        + RESET
    )

    print(
        CELESTE
        + r" \____|\___/_/   \_|_| \_|____|___/_/   \_|_| \_|\____|_____|___|_|  |_/_/   \_\ "
        + RESET
    )

    print(
        CELESTE
        + "\n"
        + " " * 24
        + NEGRITA
        + "GUARDIÁNCLIMA ITBA"
        + RESET
    )

    print(
        CELESTE
        + " " * 12
        + "Aplicación de consola para consultas climáticas"
        + RESET
    )

    print(CELESTE + "=" * 95 + RESET)



# MENÚS

def menu_acceso():

    limpiar_pantalla()

    mostrar_titulo()

    print(f" {AMARILLO}--- Menú de Acceso ---{RESET}")

    print(" 1. Iniciar Sesión")
    print(" 2. Registrar Usuario")
    print(" 3. Salir")

    print(CELESTE + "-" * 60 + RESET)

    return input("Elegí una opción (1-3): ").strip()


def menu_principal(username):

    limpiar_pantalla()

    print(CELESTE + "=" * 60 + RESET)

    print(
        CELESTE
        + f" GuardiánClima ITBA | Usuario activo: {VERDE}{username}{RESET}"
    )

    print(CELESTE + "=" * 60 + RESET)

    print(" 1. Consultar Clima")
    print(" 2. Ver Historial Personal")
    print(" 3. Estadísticas Globales")
    print(" 4. Consejo de Vestimenta (IA)")
    print(" 5. Acerca De")
    print(" 6. Cerrar Sesión")

    print(CELESTE + "-" * 60 + RESET)

    return input("Elegí una opción (1-6): ").strip()



# CLIMA

def ejecutar_consulta_clima(username, owm_key):

    print(f"\n{AMARILLO}--- Consultar Clima ---{RESET}")

    ciudad = input(
        "Ingresá una ciudad: "
    ).strip()

    if not ciudad:

        print(
            f"{ROJO}Debés ingresar una ciudad válida.{RESET}"
        )

        return None

    datos_clima = weather.obtener_clima_ciudad_owm(
        ciudad,
        owm_key
    )

    if not datos_clima:

        print(
            f"{ROJO}No se pudo obtener información climática.{RESET}"
        )

        return None

    try:

        nombre = datos_clima.get(
            "name",
            ciudad.title()
        )

        temp = datos_clima["main"]["temp"]

        sensacion = datos_clima["main"]["feels_like"]

        humedad = datos_clima["main"]["humidity"]

        viento_ms = datos_clima["wind"]["speed"]

        viento_kmh = round(viento_ms * 3.6, 2)

        descripcion = (
            datos_clima["weather"][0]["description"]
            .capitalize()
        )

        print(f"\n{VERDE}====================================")

        print(f" Clima actual en: {nombre}")

        print(f"===================================={RESET}")

        print(f" Temperatura:       {temp}°C")
        print(f" Sensación térmica: {sensacion}°C")
        print(f" Estado del cielo:  {descripcion}")
        print(f" Humedad:           {humedad}%")
        print(f" Viento:            {viento_kmh} km/h")

        print(f"{VERDE}===================================={RESET}")

        stats.guardar_consulta_historial(
            username,
            nombre,
            temp,
            descripcion,
            humedad,
            viento_kmh
        )

        print(
            f"\n{VERDE}Consulta guardada correctamente.{RESET}"
        )

        return {
            "ciudad": nombre,
            "temp": temp,
            "condicion": descripcion,
            "humedad": humedad,
            "viento": viento_kmh
        }

    except KeyError as e:

        print(
            f"{ROJO}Error al interpretar la respuesta: {e}{RESET}"
        )

        return None


# HISTORIAL

def ejecutar_historial_personal(username):

    print(
        f"\n{AMARILLO}--- Historial Personal ---{RESET}"
    )

    ciudad = input(
        "Ingresá una ciudad: "
    ).strip()

    if not ciudad:

        print(
            f"{ROJO}Debés ingresar una ciudad válida.{RESET}"
        )

        return

    registros = stats.obtener_historial_personal(
        username,
        ciudad
    )

    if not registros:

        print(
            f"\n{AMARILLO}No hay registros para esa ciudad.{RESET}"
        )

        return

    print(f"\n{VERDE}==========================================================")

    print(
        f" Historial de consultas para: {ciudad.title()}"
    )

    print(f"=========================================================={RESET}")

    print(
        f"{NEGRITA}{'Fecha':<12} | {'Hora':<10} | {'Temp':<10} | {'Condición':<20}{RESET}"
    )

    print("-" * 65)

    for r in registros:

        print(
            f"{r['Fecha']:<12} | "
            f"{r['Hora']:<10} | "
            f"{r['Temperatura']:<10} | "
            f"{r['Condicion']:<20}"
        )



# ESTADÍSTICAS

def ejecutar_estadisticas_globales():

    print(
        f"\n{AMARILLO}--- Estadísticas Globales ---{RESET}"
    )

    info = stats.calcular_estadisticas_globales()

    if not info:

        print(
            f"{ROJO}No se pudieron calcular estadísticas.{RESET}"
        )

        return

    print(f"\n{VERDE}====================================")

    print(" Resumen Global")

    print(f"===================================={RESET}")

    print(
        f" Ciudad más consultada: {info['ciudad_mas_consultada']}"
    )

    print(
        f" Total de consultas:   {info['total_consultas']}"
    )

    print(
        f" Temperatura promedio: {info['temp_promedio']}°C"
    )

    print(f"{VERDE}===================================={RESET}")


# IA

def ejecutar_consejo_ia(
    gemini_key,
    ultimo_clima
):

    if not ultimo_clima:

        print(
            f"{ROJO}Primero debés consultar el clima.{RESET}"
        )

        return

    consejo = ai_advisor.obtener_consejo_ia_gemini(
        gemini_key,
        ultimo_clima["temp"],
        ultimo_clima["condicion"],
        ultimo_clima["viento"],
        ultimo_clima["humedad"]
    )

    print(f"\n{MAGENTA}====================================")

    print(
        f" Consejo para {ultimo_clima['ciudad']}"
    )

    print(f"===================================={RESET}")

    print(consejo)

    print(f"{MAGENTA}===================================={RESET}")



# ACERCA DE

def ejecutar_acerca_de():

    print(f"\n{AMARILLO}--- Acerca De ---{RESET}")

    print(f"\n{NEGRITA}Proyecto:{RESET} GuardiánClima ITBA")

    print(f"{NEGRITA}Grupo:{RESET} {NOMBRE_GRUPO}")

    print(f"{NEGRITA}Integrantes:{RESET}")

    for integrante in INTEGRANTES:

        print(f" - {integrante}")

    print("\n" + "-" * 50)

    print("""

GuardiánClima ITBA es una aplicación de consola desarrollada en Python que permite consultar el clima de cualquier ciudad en tiempo real, guardar un historial global de consultas, ver estadísticas sobre el uso de la aplicación y recibir consejos de vestimenta generados por inteligencia artificial.

¿Cómo se usa?:

Menú de acceso:
1. Iniciar Sesión: ingresá tu usuario y contraseña para acceder.
2. Registrar Usuario: creá una cuenta nueva con una contraseña segura.
3. Salir: cerrá la aplicación.

Menú Principal:
1. Consultar Clima: ingresá una ciudad y obtené su clima actual.
2. Ver Historial Personal: observá tus consultas anteriores filtrando por ciudad.
3. Estadísticas Globales: obtené la ciudad más consultada, el total de consultas y la temperatura promedio.
4. Consejo de Vestimenta (IA): recibí una recomendación de qué ponerte según el clima consultado.
5. Acerca De: muestra esta pantalla.
6. Cerrar Sesión: volvé al Menú de Acceso.

Registro y validación de contraseñas:
Al registrarse, el sistema verifica que el nombre de usuario no esté tomado y luego valida que la contraseña cumpla con cuatro criterios de seguridad: mínimo 8 caracteres, al menos una mayúscula, un número y un carácter especial. Si no cumple alguno, el sistema informa en qué falló y hace sugerencias para mejorarla.

Advertencia sobre el almacenamiento de credenciales:
Las contraseñas se guardan en texto plano dentro de usuarios.csv. Esto es una simulación con fines educativos y no es seguro para aplicaciones reales. En un sistema real, las contraseñas deberían almacenarse usando hashing, una técnica que las transforma en un código irreversible que imposibilita hasta a la aplicación recuperar la contraseña original.

Datos de clima y guardado del historial global:
Los datos climáticos se obtienen en tiempo real desde la API de OpenWeatherMap. Cada consulta se guarda automáticamente en historial_global.csv, un archivo compartido que almacena todas las consultas realizadas.

Estadísticas globales y preparación de CSV para gráficos:
Las estadísticas se calculan procesando todo historial_global.csv sin filtros. Ese mismo archivo puede abrirse en Excel para generar gráficos de barras, líneas y torta sobre los datos globales.

Uso de Inteligencia Artificial:
El consejo de vestimenta se genera enviando los datos de la última consulta climática realizada a la API de Google Gemini, que a partir de un prompt diseñado por el equipo devuelve una recomendación breve y práctica según la temperatura, humedad, viento y condición del cielo de la ciudad tratada.
""")

# MAIN

def main():

    auth.inicializar_usuarios_csv()

    stats.inicializar_historial_csv()

    owm_key, gemini_key = obtener_api_keys()

    usuario_logeado = None

    ultimo_clima = None

    while True:

        if not usuario_logeado:

            opcion = menu_acceso()

            # LOGIN
            if opcion == "1":

                while True:

                    print(
                        f"\n{AMARILLO}--- Iniciar Sesión ---{RESET}"
                    )

                    username = input(
                        "Usuario: "
                    ).strip()

                    if not auth.usuario_existe(username):

                        print(
                            f"\n{ROJO}El usuario no existe.{RESET}"
                        )

                        retry = input(
                            "\n¿Deseás intentar nuevamente? (s/n): "
                        ).strip().lower()

                        if retry != "s":
                            break

                        continue

                    password = getpass(
                        "Contraseña: "
                    ).strip()

                    if auth.verificar_credenciales(
                        username,
                        password
                    ):

                        usuario_logeado = username

                        ultimo_clima = None

                        print(
                            f"\n{VERDE}Inicio de sesión correcto.{RESET}"
                        )

                        input(
                            "\nPresioná Enter para continuar..."
                        )

                        break

                    else:

                        print(
                            f"\n{ROJO}Contraseña incorrecta.{RESET}"
                        )

                        retry = input(
                            "\n¿Deseás intentar nuevamente? (s/n): "
                        ).strip().lower()

                        if retry != "s":
                            break

            # REGISTRO
            elif opcion == "2":

                print(
                    f"\n{AMARILLO}--- Registrar Usuario ---{RESET}"
                )

                username = input(
                    "Elegí un nombre de usuario: "
                ).strip()

                if not username:

                    print(
                        f"{ROJO}El nombre de usuario no puede estar vacío.{RESET}"
                    )

                    input("\nPresioná Enter para volver...")

                    continue

                if auth.usuario_existe(username):

                    print(
                        f"{ROJO}Ese usuario ya existe.{RESET}"
                    )

                    input("\nPresioná Enter para volver...")

                    continue

                auth.mostrar_requisitos_password()

                while True:

                    password = getpass(
                        "\nElegí una contraseña segura: "
                    ).strip()

                    exito, mensaje = auth.registrar_usuario(
                        username,
                        password
                    )

                    if exito:

                        print(
                            f"\n{VERDE}{mensaje}{RESET}"
                        )

                        usuario_logeado = username

                        ultimo_clima = None

                        print(
                            f"{VERDE}Inicio de sesión automático realizado correctamente.{RESET}"
                        )

                        input(
                            "\nPresioná Enter para continuar..."
                        )

                        break

                    print(f"\n{ROJO}{mensaje}{RESET}")

                    retry = input(
                        "\n¿Deseás intentar nuevamente? (s/n): "
                    ).strip().lower()

                    if retry != "s":
                        break

            # SALIR
            elif opcion == "3":

                print(
                    f"\n{CELESTE}Gracias por usar GuardiánClima ITBA.{RESET}"
                )

                sys.exit(0)

            else:

                print(
                    f"\n{ROJO}Opción inválida.{RESET}"
                )

                input(
                    "\nPresioná Enter para continuar..."
                )

        # MENÚ PRINCIPAL

        else:

            opcion = menu_principal(usuario_logeado)

            if opcion == "1":

                clima = ejecutar_consulta_clima(
                    usuario_logeado,
                    owm_key
                )

                if clima:
                    ultimo_clima = clima

                input("\nPresioná Enter para continuar...")

            elif opcion == "2":

                ejecutar_historial_personal(
                    usuario_logeado
                )

                input("\nPresioná Enter para continuar...")

            elif opcion == "3":

                ejecutar_estadisticas_globales()

                input("\nPresioná Enter para continuar...")

            elif opcion == "4":

                ejecutar_consejo_ia(
                    gemini_key,
                    ultimo_clima
                )

                input("\nPresioná Enter para continuar...")

            elif opcion == "5":

                ejecutar_acerca_de()

                input("\nPresioná Enter para continuar...")

            elif opcion == "6":

                print(
                    f"\n{AMARILLO}Sesión cerrada correctamente.{RESET}"
                )

                usuario_logeado = None

                ultimo_clima = None

                input(
                    "\nPresioná Enter para volver..."
                )

            else:

                print(
                    f"\n{ROJO}Opción inválida.{RESET}"
                )

                input(
                    "\nPresioná Enter para continuar..."
                )


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print(
            f"\n\n{CELESTE}Aplicación finalizada.{RESET}"
        )

        sys.exit(0)
