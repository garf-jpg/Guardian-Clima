# GuardiánClima ITBA 🌦️

# GuardiánClima ITBA

Aplicación de consola desarrollada en Python para consultar información climática en tiempo real utilizando la API de OpenWeatherMap y generar recomendaciones automáticas de vestimenta mediante inteligencia artificial.

El sistema incluye:

- Registro e inicio de sesión de usuarios
- Validación de contraseñas
- Historial de consultas
- Estadísticas globales
- Integración con APIs externas
- Persistencia de datos en archivos CSV

---

# Características Principales

## Sistema de Usuarios

La aplicación permite:

- Registrar usuarios
- Iniciar sesión
- Validar credenciales
- Verificar seguridad mínima de contraseñas

Requisitos de contraseña:

- Mínimo 8 caracteres
- Al menos una letra mayúscula
- Al menos un número
- Al menos un carácter especial

---

## Consulta Climática

La aplicación utiliza OpenWeatherMap para obtener:

- Temperatura actual
- Sensación térmica
- Humedad
- Velocidad del viento
- Estado del clima

Todas las consultas quedan guardadas automáticamente en:

```txt
historial_global.csv
```

---

## Consejos Automáticos

La aplicación puede conectarse a Google Gemini para generar recomendaciones automáticas según el clima.

Si la API no está disponible o supera el límite gratuito, el sistema utiliza un generador local de consejos para evitar errores.

---

## Estadísticas

El sistema calcula automáticamente:

- Cantidad total de consultas
- Ciudad más consultada
- Temperatura promedio global

---

# Estructura del Proyecto

```txt
guardian_clima_itba/
│
├── main.py
├── auth.py
├── weather.py
├── stats.py
├── ai_advisor.py
├── config.py
├── tests.py
├── runtests.py
├── README.md
├── .env
│
├── usuarios.csv
└── historial_global.csv
```

---

# Requisitos

## Python

Se recomienda utilizar:

```txt
Python 3.11 o superior
```

---

# Actualizar Python

## Verificar versión instalada

Abrir PowerShell o CMD y ejecutar:

```bash
python --version
```

---

## Descargar Python 3.11

https://www.python.org/downloads/

Durante la instalación marcar:

```txt
Add Python to PATH
```

---

## Verificar que Python 3.11 quedó activo

Cerrar y volver a abrir la terminal.

Luego ejecutar:

```bash
python --version
```

Debe aparecer algo similar a:

```txt
Python 3.11.x
```

---

# Instalación

Abrir una terminal dentro de la carpeta del proyecto y ejecutar:

```bash
pip install requests google-genai python-dotenv
```

---

# Configuración de APIs

## Crear archivo `.env`

Crear un archivo llamado:

```txt
.env
```

en la misma carpeta donde está `main.py`.

Contenido:

```env
OPENWEATHERMAP_API_KEY=TU_API_KEY
GEMINI_API_KEY=TU_API_KEY
```

---

# Obtener las API Keys

## OpenWeatherMap

1. Crear cuenta en:

https://openweathermap.org/

2. Ir a:

```txt
API Keys
```

3. Generar una nueva clave

---

## Google Gemini

1. Entrar a:

https://aistudio.google.com/

2. Crear una API Key

---

# Ejecutar el Programa

## Método recomendado

Abrir PowerShell o CMD dentro de la carpeta del proyecto.

Ejecutar:

```bash
python main.py
```

---

## Alternativa usando Python Launcher

Si existen varias versiones de Python instaladas:

```bash
py -3.11 main.py
```

---

# Ejecutar Tests

Para ejecutar las pruebas automáticas:

```bash
python runtests.py
```

Los resultados se guardarán en:

```txt
results.txt
```

---

# Archivos CSV

## usuarios.csv

Guarda usuarios registrados.

Formato:

```csv
username,password
```

---

## historial_global.csv

Guarda consultas climáticas realizadas.

Formato:

```csv
NombreDeUsuario,Ciudad,Fecha/Hora,Temperatura_C,Condicion_Clima,Humedad_Porcentaje,Viento_kmh
```
---

# Tecnologías Utilizadas

- Python 3.11
- OpenWeatherMap API
- Google Gemini API
- requests
- google-genai
- python-dotenv
- CSV
- unittest

---

# Integrantes

Completar en `config.py`:

```python
INTEGRANTES = [
    "INTEGRANTE 1",
    "INTEGRANTE 2",
    "INTEGRANTE 3"
]

NOMBRE_GRUPO = "NOMBRE_DEL_GRUPO"
```

---

# Notas Importantes

- El archivo `.env` debe estar en la misma carpeta que `main.py`
- No compartir ni subir el archivo `.env`
- No subir API Keys a GitHub
- Gemini puede tener límites gratuitos diarios
- Si Gemini falla, el sistema usa consejos locales automáticamente

---

# Funcionalidades Implementadas

- Registro de usuarios
- Inicio de sesión
- Validación de contraseñas
- Consulta climática real
- Persistencia en CSV
- Estadísticas globales
- Integración con IA
- Manejo de errores
- Tests automáticos