# GPT-4o Mini Chat

Este proyecto proporciona una interfaz de línea de comandos (CLI) y una interfaz web para interactuar con el modelo GPT-4o Mini de OpenAI.

## Características

*   **Interfaz CLI**: Permite enviar mensajes a GPT-4o Mini directamente desde la terminal.
*   **Interfaz Web**: Una aplicación web moderna, limpia y responsive para chatear con el bot, con animación de escritura y respuestas en formato HTML.
*   **Gestión de Dependencias**: Uso de entornos virtuales y `requirements.txt` para una fácil replicación del entorno.
*   **Control de Versiones**: Integración con Git para el seguimiento de cambios.

## Estructura del Proyecto

```
.
├── .env                  # Archivo para la clave API de OpenAI (IGNORADO por Git)
├── .gitignore            # Reglas para ignorar archivos en Git
├── requirements.txt      # Lista de dependencias del proyecto
├── gpt_cli.py            # Script para la interfaz de línea de comandos
├── frontend/             # Archivos de la interfaz web (HTML, CSS, JavaScript)
│   ├── index.html
│   ├── style.css
│   └── script.js
└── backend/              # Archivos del servidor backend (FastAPI)
    └── main.py
```

## Requisitos

*   Python 3.8+
*   Una clave API de OpenAI.

## Configuración e Instalación

Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Clonar el Repositorio (si aún no lo has hecho)

```bash
git clone [URL_del_repositorio]
cd botvibe # O el nombre de tu directorio de proyecto
```

### 2. Configurar la Clave API de OpenAI

Crea un archivo llamado `.env` en la raíz de tu proyecto (al mismo nivel que `requirements.txt`) y añade tu clave API de OpenAI de la siguiente manera:

```
OPENAI_API_KEY = 'tu_clave_api_aqui'
```

**Importante**: Este archivo `.env` está incluido en `.gitignore` y no debe ser subido a tu repositorio público por razones de seguridad.

### 3. Crear y Activar el Entorno Virtual

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows (CMD):
.\venv\Scripts\activate
# En Linux/macOS (Bash/Zsh):
source venv/bin/activate
```

### 4. Instalar Dependencias

Con el entorno virtual activado, instala las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si necesitas generar o actualizar el `requirements.txt` después de instalar nuevas librerías:

```bash
pip freeze > requirements.txt
```

## Uso

### Interfaz de Línea de Comandos (CLI)

Para usar el bot desde la terminal:

1.  Asegúrate de que tu entorno virtual esté activado.
2.  Ejecuta el script:
    ```bash
    python gpt_cli.py
    ```
3.  Escribe tus mensajes. Escribe `salir` para terminar la conversación.

### Interfaz Web

Para usar la interfaz web:

1.  Asegúrate de que tu entorno virtual esté activado.
2.  Navega al directorio `backend`:
    ```bash
    cd backend
    ```
3.  Inicia el servidor FastAPI:
    ```bash
    uvicorn main:app --reload
    ```
    El servidor se iniciará en `http://127.0.0.1:8000`.
4.  Abre tu navegador web y ve a `http://127.0.0.1:8000`.

¡Disfruta chateando con GPT-4o Mini!
