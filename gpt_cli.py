import os
from openai import OpenAI
from dotenv import load_dotenv

def get_openai_api_key():
    """Obtiene la clave API de OpenAI de las variables de entorno o del archivo .env."""
    load_dotenv() # Carga las variables de entorno del archivo .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada en el sistema ni en el archivo .env.")
    return api_key

def send_message_to_gpt(message):
    """Envía un mensaje a GPT-4o mini y devuelve la respuesta."""
    try:
        client = OpenAI(api_key=get_openai_api_key())
        
        print("Enviando mensaje a GPT-4o mini...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al comunicarse con OpenAI: {e}"

def main():
    print("Bienvenido al cliente de GPT-4o mini CLI.")
    print("Escribe 'salir' para terminar la conversación.")

    while True:
        user_message = input("Tú: ")
        if user_message.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        gpt_response = send_message_to_gpt(user_message)
        print(f"GPT-4o mini: {gpt_response}")

if __name__ == "__main__":
    main()
