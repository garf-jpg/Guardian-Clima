import os
import csv
import re
from config import USUARIOS_CSV


def mostrar_requisitos_password():
    """
    Muestra los requisitos mínimos que debe cumplir
    una contraseña para ser aceptada.
    """

    print("\nLa contraseña debe cumplir con los siguientes requisitos:")
    print(" - Tener al menos 8 caracteres")
    print(" - Contener al menos una letra mayúscula")
    print(" - Contener al menos un número")
    print(" - Contener al menos un carácter especial (@, $, !, %, etc.)")


def inicializar_usuarios_csv():
    """
    Crea el archivo CSV de usuarios si todavía
    no existe en el sistema.
    """

    if not os.path.exists(USUARIOS_CSV):
        try:
            with open(
                USUARIOS_CSV,
                mode="w",
                newline="",
                encoding="utf-8"
            ) as f:
                writer = csv.writer(f)

                # Encabezados utilizados para almacenar
                # nombre de usuario y contraseña.
                writer.writerow([
                    "username",
                    "password"
                ])

        except Exception as e:
            print(f"Error al crear el archivo de usuarios: {e}")


def verificar_credenciales(username, password):
    """
    Verifica si el usuario y la contraseña ingresados
    coinciden con algún registro almacenado.
    """

    inicializar_usuarios_csv()

    try:
        with open(
            USUARIOS_CSV,
            mode="r",
            encoding="utf-8"
        ) as f:
            reader = csv.DictReader(f)

            # Recorrer todos los usuarios registrados
            # buscando coincidencia exacta.
            for row in reader:
                if (
                    row["username"] == username
                    and row["password"] == password
                ):
                    return True

    except Exception as e:
        print(f"Error al leer usuarios: {e}")

    return False


def usuario_existe(username):
    """
    Comprueba si un nombre de usuario ya se
    encuentra registrado.
    """

    inicializar_usuarios_csv()

    try:
        with open(
            USUARIOS_CSV,
            mode="r",
            encoding="utf-8"
        ) as f:
            reader = csv.DictReader(f)

            # La comparación se realiza sin distinguir
            # mayúsculas y minúsculas.
            for row in reader:
                if row["username"].lower() == username.lower():
                    return True

    except Exception as e:
        print(f"Error al verificar usuario: {e}")

    return False


def validar_contrasena(password):
    """
    Verifica que la contraseña cumpla con los
    requisitos mínimos de seguridad establecidos.
    """

    reglas_incumplidas = []
    recomendaciones = []

    # Verificar longitud mínima.
    if len(password) < 8:
        reglas_incumplidas.append(
            "Debe tener al menos 8 caracteres."
        )

        recomendaciones.append(
            "Agregá más caracteres."
        )

    # Verificar presencia de letras mayúsculas.
    if not any(c.isupper() for c in password):
        reglas_incumplidas.append(
            "Debe contener al menos una letra mayúscula."
        )

        recomendaciones.append(
            "Incluí una letra mayúscula."
        )

    # Verificar presencia de números.
    if not any(c.isdigit() for c in password):
        reglas_incumplidas.append(
            "Debe contener al menos un número."
        )

        recomendaciones.append(
            "Incluí un número."
        )

    # Verificar presencia de caracteres especiales.
    caracteres_especiales = r"[@$!%*?&+\-=_\[\]{}|;:',.<>/?~^#]"

    if not re.search(caracteres_especiales, password):
        reglas_incumplidas.append(
            "Debe contener al menos un carácter especial."
        )

        recomendaciones.append(
            "Agregá un símbolo como @, $, ! o %."
        )

    # Si no hay reglas incumplidas, la contraseña es válida.
    if not reglas_incumplidas:
        return True, [], []

    return False, reglas_incumplidas, recomendaciones


def registrar_usuario(username, password):
    """
    Registra un nuevo usuario si el nombre elegido
    está disponible y la contraseña es válida.
    """

    inicializar_usuarios_csv()

    # Evitar nombres vacíos o compuestos solo por espacios.
    if not username.strip():
        return (
            False,
            "El nombre de usuario no puede estar vacío."
        )

    # Verificar que el usuario no exista previamente.
    if usuario_existe(username):
        return (
            False,
            "El nombre de usuario ya existe."
        )

    # Validar la contraseña ingresada.
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
            mode="a",
            newline="",
            encoding="utf-8"
        ) as f:
            writer = csv.writer(f)

            # Guardar el nuevo usuario en el archivo.
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
