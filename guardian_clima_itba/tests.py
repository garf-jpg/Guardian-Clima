# -*- coding: utf-8 -*-

import unittest
import os
import csv

import auth
import stats


class TestGuardianClima(unittest.TestCase):

    def test_validacion_contrasenas_debiles(self):

        valida, incumplidas, _ = auth.validar_contrasena("Ab1$")
        self.assertFalse(valida)

        valida, incumplidas, _ = auth.validar_contrasena("password123$")
        self.assertFalse(valida)

        valida, incumplidas, _ = auth.validar_contrasena("Password$")
        self.assertFalse(valida)

        valida, incumplidas, _ = auth.validar_contrasena("Password123")
        self.assertFalse(valida)

    def test_validacion_contrasena_fuerte(self):

        valida, incumplidas, _ = auth.validar_contrasena(
            "Password123!"
        )

        self.assertTrue(valida)
        self.assertEqual(len(incumplidas), 0)

    def test_calculo_estadisticas(self):

        archivo_test = "historial_test.csv"

        with open(
            archivo_test,
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

            writer.writerow([
                "pepe",
                "Buenos Aires",
                "2026-05-25 10:00:00",
                "20.5",
                "Despejado",
                "60",
                "15.0"
            ])

            writer.writerow([
                "juan",
                "Buenos Aires",
                "2026-05-25 11:00:00",
                "22.5",
                "Nublado",
                "65",
                "12.0"
            ])

            writer.writerow([
                "pepe",
                "Madrid",
                "2026-05-25 12:00:00",
                "15.0",
                "Lluvia",
                "80",
                "25.0"
            ])

        original_csv = stats.HISTORIAL_CSV
        stats.HISTORIAL_CSV = archivo_test

        try:

            res = stats.calcular_estadisticas_globales()

            self.assertEqual(
                res["total_consultas"],
                3
            )

            self.assertEqual(
                res["ciudad_mas_consultada"],
                "Buenos Aires"
            )

            self.assertAlmostEqual(
                res["temp_promedio"],
                19.33,
                places=2
            )

        finally:

            stats.HISTORIAL_CSV = original_csv

            if os.path.exists(archivo_test):
                os.remove(archivo_test)


if __name__ == "__main__":

    print("Ejecutando tests...\n")

    unittest.main()