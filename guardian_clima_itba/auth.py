# -*- coding: utf-8 -*-

import os
import csv
import re
from config import USUARIOS_CSV


def mostrar_requisitos_password():
    """
    Muestra los requisitos mínimos de seguridad
    para la contraseña.
    """

    print("\nLa contraseña debe cumplir con los siguientes requisitos:")
    print(" - Tener al menos 8 caracteres")
    print(" - Contener al menos una letra mayúscula")
    print(" - Contener al menos un número")
    print(" - Contener al menos un carácter especial (@, $, !, %, etc.)")


def inicializar_usuarios_csv():
    """
    Crea el archivo CSV de usuarios
    si todavía no existe.
    """

    if not os.path.exists(USUARIOS_CSV):

        try:

            with open(
                USUARIOS_CSV,
                mode='w',
                newline='',
                encoding='utf-8'
            ) as f:

                writer = csv.writer(f)

                writer.writerow([
                    "username",
                    "password"
                ])

        except Exception as e:

            print(f"Error al crear el archivo de usuarios: {e}")


def verificar_credenciales(username, password):
    """
    Verifica si el usuario y contraseña coinciden.
    """

    inicializar_usuarios_csv()

    try:

        with open(
            USUARIOS_CSV,
            mode='r',
            encoding='utf-8'
        ) as f:

            reader = csv.DictReader(f)

            for row in reader:

                if (
                    row['username'] == username
                    and row['password'] == password
                ):

                    return True

    except Exception as e:

        print(f"Error al leer usuarios: {e}")

    return False


def usuario_existe(username):
    """
    Verifica si el usuario ya existe.
    """

    inicializar_usuarios_csv()

    try:

        with open(
            USUARIOS_CSV,
            mode='r',
            encoding='utf-8'
        ) as f:

            reader = csv.DictReader(f)

            for row in reader:

                if row['username'].lower() == username.lower():

                    return True

    except Exception as e:

        print(f"Error al verificar usuario: {e}")

    return False


def validar_contrasena(password):
    """
    Valida la contraseña según los requisitos mínimos.
    """

    reglas_incumplidas = []
    recomendaciones = []

    # Mínimo 8 caracteres
    if len(password) < 8:

        reglas_incumplidas.append(
            "Debe tener al menos 8 caracteres."
        )

        recomendaciones.append(
            "Agregá más caracteres."
        )

    # Al menos una mayúscula
    if not any(c.isupper() for c in password):

        reglas_incumplidas.append(
            "Debe contener al menos una letra mayúscula."
        )

        recomendaciones.append(
            "Incluí una letra mayúscula."
        )

    # Al menos un número
    if not any(c.isdigit() for c in password):

        reglas_incumplidas.append(
            "Debe contener al menos un número."
        )

        recomendaciones.append(
            "Incluí un número."
        )

    # Al menos un carácter especial
    caracteres_especiales = r"[@$!%*?&+\-=_\[\]{}|;:',.<>/?~^#]"

    if not re.search(caracteres_especiales, password):

        reglas_incumplidas.append(
            "Debe contener al menos un carácter especial."
        )

        recomendaciones.append(
            "Agregá un símbolo como @, $, ! o %."
        )

    # Resultado final
    if not reglas_incumplidas:

        return True, [], []

    return False, reglas_incumplidas, recomendaciones


def registrar_usuario(username, password):
    """
    Registra un nuevo usuario
    si cumple todas las validaciones.
    """

    inicializar_usuarios_csv()

    # Validar usuario vacío
    if not username.strip():

        return (
            False,
            "El nombre de usuario no puede estar vacío."
        )

    # Verificar si ya existe
    if usuario_existe(username):

        return (
            False,
            "El nombre de usuario ya existe."
        )

    # Validar contraseña
    es_valida, incumplidas, sugerencias = validar_contrasena(password)

    if not es_valida:

        lista_reglas = "\n - " + "\n - ".join(incumplidas)

        lista_sugerencias = "\n - " + "\n - ".join(sugerencias)

        mensaje_error = (
            f"La contraseña no cumple con:\n"
            f"{lista_reglas}\n\n"
            f"Sugerencias:\n"
            f"{lista_sugerencias}"
        )

        return False, mensaje_error

    try:

        with open(
            USUARIOS_CSV,
            mode='a',
            newline='',
            encoding='utf-8'
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                username,
                password
            ])

        return (
            True,
            "Usuario registrado correctamente."
        )

    except Exception as e:

        return (
            False,
            f"Error al guardar el usuario: {e}"
        )