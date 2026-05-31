import os
import csv
from datetime import datetime
from collections import Counter
from config import HISTORIAL_CSV


def inicializar_historial_csv():
    """
    Crea el archivo de historial si todavía no existe.
    También escribe la fila de encabezados que utilizará
    el resto del programa.
    """

    if not os.path.exists(HISTORIAL_CSV):
        try:
            with open(
                HISTORIAL_CSV,
                mode="w",
                newline="",
                encoding="utf-8"
            ) as f:
                writer = csv.writer(f)

                writer.writerow([
                    "NombreDeUsuario",
                    "Ciudad",
                    "Fecha/Hora",
                    "Temperatura_C",
                    "Condicion_Clima",
                    "Humedad_Porcentaje",
                    "Viento_kmh"
                ])

        except Exception as e:
            print(f"Error al crear historial: {e}")


def guardar_consulta_historial(
    username,
    ciudad,
    temp_c,
    condicion,
    humedad,
    viento_kmh
):
    """
    Guarda una nueva consulta climática realizada por
    un usuario en el archivo de historial.
    """

    inicializar_historial_csv()

    # Registrar la fecha y hora exactas de la consulta
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(
            HISTORIAL_CSV,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as f:
            writer = csv.writer(f)

            writer.writerow([
                username,
                ciudad.title(),
                ahora,
                temp_c,
                condicion,
                humedad,
                viento_kmh
            ])

    except Exception as e:
        print(f"Error al guardar historial: {e}")


def obtener_historial_personal(username, ciudad):
    """
    Obtiene todas las consultas realizadas por un usuario
    para una ciudad determinada.
    """

    inicializar_historial_csv()

    resultados = []

    try:
        with open(
            HISTORIAL_CSV,
            mode="r",
            encoding="utf-8"
        ) as f:
            reader = csv.DictReader(f)

            for row in reader:

                # Filtrar únicamente los registros que
                # coincidan con el usuario y la ciudad.
                if (
                    row["NombreDeUsuario"].lower() == username.lower()
                    and row["Ciudad"].lower() == ciudad.lower()
                ):
                    fecha_hora = row["Fecha/Hora"]

                    try:
                        # Convertir la fecha guardada a un formato
                        # más amigable para mostrar en pantalla.
                        dt = datetime.strptime(
                            fecha_hora,
                            "%Y-%m-%d %H:%M:%S"
                        )

                        fecha = dt.strftime("%d/%m/%Y")
                        hora = dt.strftime("%H:%M:%S")

                    except ValueError:
                        fecha = fecha_hora
                        hora = "N/A"

                    resultados.append({
                        "Fecha": fecha,
                        "Hora": hora,
                        "Temperatura": row["Temperatura_C"],
                        "Condicion": row["Condicion_Clima"]
                    })

    except Exception as e:
        print(f"Error al leer historial: {e}")

    return resultados


def calcular_estadisticas_globales():
    """
    Calcula estadísticas generales a partir de todas las
    consultas almacenadas en el historial.
    """

    inicializar_historial_csv()

    ciudades = []
    temperaturas = []
    total_consultas = 0

    try:
        with open(
            HISTORIAL_CSV,
            mode="r",
            encoding="utf-8"
        ) as f:
            reader = csv.DictReader(f)

            for row in reader:
                ciudades.append(row["Ciudad"])

                # Intentar convertir la temperatura a número
                # para poder calcular el promedio.
                try:
                    temperaturas.append(
                        float(row["Temperatura_C"])
                    )
                except ValueError:
                    pass

                total_consultas += 1

    except Exception as e:
        print(f"Error al calcular estadísticas: {e}")
        return None

    # Si todavía no existen consultas registradas,
    # devolver estadísticas vacías.
    if total_consultas == 0:
        return {
            "total_consultas": 0,
            "ciudad_mas_consultada": "Ninguna",
            "temp_promedio": 0
        }

    # Obtener la ciudad que aparece más veces
    # en el historial.
    ciudad_mas_consultada = (
        Counter(ciudades)
        .most_common(1)[0][0]
    )

    # Calcular la temperatura promedio global.
    temp_promedio = (
        sum(temperaturas) / len(temperaturas)
        if temperaturas else 0
    )

    return {
        "total_consultas": total_consultas,
        "ciudad_mas_consultada": ciudad_mas_consultada,
        "temp_promedio": round(temp_promedio, 2)
    }
