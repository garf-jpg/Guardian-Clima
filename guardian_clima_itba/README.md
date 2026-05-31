# GuardiánClima ITBA

## Descripción del Proyecto

GuardiánClima ITBA es una aplicación de consola desarrollada en Python que permite consultar información climática en tiempo real mediante la API de OpenWeatherMap, almacenar un historial global de consultas, generar estadísticas de uso y obtener recomendaciones de vestimenta utilizando Inteligencia Artificial a través de Google Gemini.

El proyecto fue desarrollado como parte del Challenge Tecnológico Integrador, aplicando conceptos de Programación, Ciberseguridad, Análisis de Datos, Inteligencia Artificial y Cloud Computing.

---

## Funcionalidades Principales

### 1. Gestión de Usuarios

La aplicación permite:

* Registrar nuevos usuarios.
* Iniciar sesión.
* Verificar credenciales almacenadas en CSV.
* Validar contraseñas según criterios mínimos de seguridad.

#### Requisitos de Contraseña

La contraseña debe cumplir con:

* Al menos 8 caracteres.
* Al menos una letra mayúscula.
* Al menos un número.
* Al menos un carácter especial.

Si la contraseña no cumple los requisitos, el sistema informa qué reglas fueron incumplidas y ofrece recomendaciones para crear una contraseña más segura.

### Importante

El almacenamiento de usuarios utilizado en este proyecto es una simulación educativa solicitada por la consigna.

Las contraseñas se almacenan en texto plano únicamente con fines académicos. En aplicaciones reales se deben utilizar técnicas de seguridad como hashing y salting para proteger las credenciales.

---

### 2. Consulta Climática

La aplicación utiliza la API de OpenWeatherMap para obtener información actualizada de cualquier ciudad.

Datos obtenidos:

* Temperatura actual.
* Sensación térmica.
* Humedad.
* Velocidad del viento.
* Estado del clima.

Cada consulta realizada se almacena automáticamente en el archivo:

historial_global.csv

---

### 3. Historial Personal

Los usuarios pueden consultar su historial de búsquedas filtrando por ciudad.

La información mostrada incluye:

* Fecha.
* Hora.
* Temperatura registrada.
* Condición climática.

---

### 4. Estadísticas Globales

La aplicación procesa todas las consultas almacenadas en el historial global y calcula:

* Ciudad más consultada.
* Cantidad total de consultas.
* Temperatura promedio registrada.

Los datos almacenados pueden utilizarse posteriormente para generar gráficos en Excel o Google Sheets.

---

### 5. Consejo de Vestimenta con IA

Utilizando los datos de la última consulta climática realizada, la aplicación se conecta a Google Gemini para generar recomendaciones relacionadas con:

* Tipo de ropa sugerida.
* Necesidad de abrigo.
* Uso de paraguas.
* Precauciones según las condiciones climáticas.

---

### 6. Acerca de

La aplicación incluye una sección informativa donde se describe:

* El funcionamiento general del sistema.
* El flujo de uso.
* Las tecnologías empleadas.
* Los integrantes del equipo.
* El nombre del grupo.

---

## Flujo de Uso

1. Ejecutar la aplicación.

2. Registrar un nuevo usuario o iniciar sesión.

3. Acceder al menú principal.

4. Seleccionar una de las siguientes opciones:

   * Consultar clima.
   * Ver historial personal.
   * Ver estadísticas globales.
   * Obtener consejo de vestimenta mediante IA.
   * Acerca de.
   * Cerrar sesión.

5. Al cerrar sesión, el sistema regresa al menú de acceso.

---

## Estructura del Proyecto

```text
guardian_clima_itba/
│
├── main.py
├── auth.py
├── weather.py
├── stats.py
├── ai_advisor.py
├── config.py
├── README.md
├── .env
│
├── usuarios.csv
└── historial_global.csv
```

---

## Requisitos

### Python

Se recomienda utilizar:

```text
Python 3.11 o superior
```

Verificar instalación:

```bash
python --version
```

---

## Instalación de Dependencias

Desde la carpeta raíz del proyecto ejecutar:

```bash
pip install requests google-genai python-dotenv
```

---

## Configuración de APIs

Crear un archivo llamado:

```text
.env
```

en la misma carpeta donde se encuentra `main.py`.

Contenido:

```env
OPENWEATHERMAP_API_KEY=TU_API_KEY
GEMINI_API_KEY=TU_API_KEY
```

---

## Obtención de API Keys

### OpenWeatherMap

1. Crear una cuenta en OpenWeatherMap.
2. Acceder a la sección API Keys.
3. Generar una nueva clave.

### Google Gemini

1. Ingresar a Google AI Studio.
2. Crear una API Key.

---

## Ejecución del Programa

Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

Si existen varias versiones de Python instaladas:

```bash
py -3.11 main.py
```

---

## Archivos CSV

### usuarios.csv

Almacena los usuarios registrados.

Formato:

```csv
username,password
```

### historial_global.csv

Almacena todas las consultas climáticas realizadas.

Formato:

```csv
NombreDeUsuario,Ciudad,Fecha/Hora,Temperatura_C,Condicion_Clima,Humedad_Porcentaje,Viento_kmh
```

---

## Tecnologías Utilizadas

* Python 3.11
* OpenWeatherMap API
* Google Gemini API
* Requests
* Google GenAI
* Python Dotenv
* CSV
* Datetime
* Collections (Counter)

---

## Integrantes

Grupo: grupo 25

Integrantes:

* Elena Lucia Serrizuela
* Sofia Olivia Cho
* Olivia Stegmann
* Tizianna Zotti

---

## Consideraciones Importantes

* No compartir el archivo `.env`.
* No publicar las API Keys en repositorios.
* Mantener los archivos CSV dentro del proyecto.
* Verificar conexión a Internet para utilizar las APIs externas.
* Ante errores de conexión, la aplicación mostrará mensajes informativos para el usuario.

---

## Funcionalidades Implementadas

* Registro de usuarios.
* Inicio de sesión.
* Validación de contraseñas.
* Consulta climática en tiempo real.
* Historial global de consultas.
* Historial personal por ciudad.
* Estadísticas globales.
* Integración con Inteligencia Artificial.
* Persistencia de datos mediante CSV.
* Manejo de errores.
* Arquitectura modular.
