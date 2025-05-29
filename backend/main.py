import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import markdown

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# Configurar CORS para permitir solicitudes desde el frontend
origins = [
    "http://127.0.0.1:8000", # Si el frontend se sirve desde el mismo uvicorn
    "null", # Para cuando se abre index.html directamente desde el navegador (file://)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar el directorio 'frontend' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Sirve el archivo index.html del frontend."""
    with open("../frontend/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat")
async def chat_endpoint(msg: Message):
    """Endpoint para enviar mensajes a GPT-4o mini."""
    user_message = msg.message
    
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada.")
        
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        # Convertir la respuesta de Markdown a HTML
        html_response = markdown.markdown(response.choices[0].message.content)
        return {"response": html_response}
    except Exception as e:
        print(f"Error al comunicarse con OpenAI: {e}")
        return {"response": f"Error: {e}"}
