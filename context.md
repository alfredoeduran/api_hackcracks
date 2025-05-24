Guía para Ejecutar el Proyecto FastAPI y MySQL en Railway
Este documento te guiará a través de la configuración y ejecución de la API de FastAPI que interactúa con una base de datos MySQL alojada en Railway.

1. Requisitos Previos
Asegúrate de tener instalado lo siguiente en tu sistema:

Python 3.8+: Puedes descargarlo desde python.org.
Git: Para clonar el repositorio, descárgalo desde git-scm.com.
2. Configuración de Railway (MySQL)
Nota: Ya se ha configurado una base de datos MySQL en Railway. Necesitarás las credenciales de conexión para que la aplicación se conecte.

Obtén las Credenciales de MySQL de Railway:
Accede al panel de Railway del proyecto donde está alojada la base de datos MySQL. En la sección de "Variables" o "Connect", encontrarás las siguientes credenciales:

MYSQL_HOST
MYSQL_PORT
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE
Guarda estas credenciales, las necesitarás para el siguiente paso.

3. Configuración Local del Proyecto
Sigue estos pasos para preparar el entorno local:

Clona el Repositorio:
Abre tu terminal o línea de comandos y ejecuta el siguiente comando:

Bash

git clone <URL_DEL_REPOSITORIO>
cd fastapi_mysql_railway # Asegúrate de que este es el nombre del directorio clonado
Reemplaza <URL_DEL_REPOSITORIO> con la URL real de tu repositorio Git.

Crea un Entorno Virtual (Recomendado):
Es una buena práctica aislar las dependencias del proyecto.

Bash

python -m venv venv
Activa el Entorno Virtual:

En Linux/macOS:
Bash

source venv/bin/activate
En Windows:
Bash

venv\Scripts\activate
Instala las Dependencias:
Una vez activado el entorno virtual, instala las librerías necesarias:

Bash

pip install fastapi uvicorn mysql-connector-python pydantic python-dotenv
Crea el Archivo .env:
En la raíz del proyecto (donde se encuentra main.py), crea un archivo llamado .env y pega las credenciales de MySQL que obtuviste de Railway.

Fragmento de código

MYSQL_HOST=tu_host_de_railway
MYSQL_PORT=tu_puerto_de_railway
MYSQL_USER=tu_usuario_de_railway
MYSQL_PASSWORD=tu_contraseña_de_railway
MYSQL_DATABASE=tu_base_de_datos_de_railway
¡Importante! Asegúrate de reemplazar los valores con tus credenciales reales.

4. Ejecutar la Aplicación FastAPI
Con el entorno virtual activado y el archivo .env configurado, puedes iniciar la aplicación.

Ejecuta el Servidor Uvicorn:
Desde la raíz del proyecto en tu terminal:

Bash

uvicorn main:app --reload
main: Se refiere al archivo main.py.
app: Es el nombre de la instancia de FastAPI dentro de main.py (app = FastAPI(...)).
--reload: Recarga el servidor automáticamente cada vez que detecta cambios en el código (útil para desarrollo).
Verifica la Ejecución:
Verás un mensaje en la terminal indicando que Uvicorn está corriendo, usualmente en http://127.0.0.1:8000.

5. Probar la API
Abre tu navegador y accede a las siguientes URLs para interactuar con la API:

Documentación Interactiva (Swagger UI):
http://127.0.0.1:8000/docs
Desde aquí podrás ver todos los endpoints definidos (GET, POST, PUT, DELETE para items) y probarlos directamente.

Documentación Alternativa (ReDoc):
http://127.0.0.1:8000/redoc

Endpoint Raíz:
http://127.0.0.1:8000/
Debería mostrar un mensaje de bienvenida.

6. Estructura del Proyecto
Para referencia, aquí tienes un resumen de la estructura de archivos del proyecto:

fastapi_mysql_railway/
├── .env                  # Variables de entorno (credenciales de MySQL)
├── main.py               # La aplicación FastAPI principal y los endpoints
├── database.py           # Funciones para la conexión a la base de datos MySQL
├── models.py             # Definiciones de modelos de datos con Pydantic
└── crud.py               # Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) con la base de datos
