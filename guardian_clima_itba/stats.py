
import os
import csv
from datetime import datetime
from collections import Counter
from config import HISTORIAL_CSV


def inicializar_historial_csv():

    if not os.path.exists(HISTORIAL_CSV):

        try:

            with open(
                HISTORIAL_CSV,
                mode='w',
                newline='',
                encoding='utf-8'
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

    inicializar_historial_csv()

    ahora = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    try:

        with open(
            HISTORIAL_CSV,
            mode='a',
            newline='',
            encoding='utf-8'
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

    inicializar_historial_csv()

    resultados = []

    try:

        with open(
            HISTORIAL_CSV,
            mode='r',
            encoding='utf-8'
        ) as f:

            reader = csv.DictReader(f)

            for row in reader:

                if (
                    row['NombreDeUsuario'].lower() == username.lower()
                    and
                    row['Ciudad'].lower() == ciudad.lower()
                ):

                    fecha_hora = row['Fecha/Hora']

                    try:

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
                        "Temperatura": row['Temperatura_C'],
                        "Condicion": row['Condicion_Clima']
                    })

    except Exception as e:
        print(f"Error al leer historial: {e}")

    return resultados


def calcular_estadisticas_globales():

    inicializar_historial_csv()

    ciudades = []
    temperaturas = []
    total_consultas = 0

    try:

        with open(
            HISTORIAL_CSV,
            mode='r',
            encoding='utf-8'
        ) as f:

            reader = csv.DictReader(f)

            for row in reader:

                ciudades.append(row['Ciudad'])

                try:
                    temperaturas.append(
                        float(row['Temperatura_C'])
                    )
                except:
                    pass

                total_consultas += 1

    except Exception as e:
        print(f"Error al calcular estadísticas: {e}")
        return None

    if total_consultas == 0:

        return {
            "total_consultas": 0,
            "ciudad_mas_consultada": "Ninguna",
            "temp_promedio": 0
        }

    ciudad_mas_consultada = (
        Counter(ciudades)
        .most_common(1)[0][0]
    )

    temp_promedio = (
        sum(temperaturas) / len(temperaturas)
        if temperaturas else 0
    )

    return {
        "total_consultas": total_consultas,
        "ciudad_mas_consultada": ciudad_mas_consultada,
        "temp_promedio": round(temp_promedio, 2)
    }