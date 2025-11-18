# main.py

import os
from dotenv import load_dotenv
import requests  # Importar 'requests' para consumir el API
from navegador import crear_navegador
from whatsapp_web import WhatsAppWeb
import time

# Cargar todas las variables de entorno
load_dotenv()

# --- Variables cargadas desde .env ---
API_URL = os.getenv("API_URL_NUMERO_APRENDICES")
API_TOKEN = os.getenv("API_AUTH_TOKEN")

# Mensaje que se enviará
MENSAJE_A_ENVIAR = "Hola ¿Cómo estás? Esto es una prueba."

def obtener_numeros_del_api():
    """
    Se conecta al API para obtener los números.
    Si el API no está configurada, devuelve una lista de prueba.
    """
    if API_URL and API_TOKEN:
        print(f"Obteniendo números desde API: {API_URL}")
        # try:
        #     headers = {"Authorization": f"Bearer {API_TOKEN}"}
        #     respuesta = requests.get(API_URL, headers=headers)
        #     respuesta.raise_for_status()
        #     datos = respuesta.json()
        #     # Asumiendo que el API devuelve una lista de strings:
        #     numeros = [item['telefono'] for item in datos] 
        #     print(f"✔ {len(numeros)} números obtenidos del API.")
        #     return numeros
        # except Exception as e:
        #     print(f"❌ ERROR al conectar al API: {e}")
        #     print("Usando lista de prueba como fallback.")
    
    # --- Fallback: Lista de prueba ---
    # Si el API no está en el .env o falla, usamos esto:
    print("ADVERTENCIA: API no implementada o falló. Usando lista de prueba.")
    numeros_de_prueba = [
        "573042836668",
        "573044468766",
        "573194989976",
        "573126691379", 
        "573042836640"
    ]
    return numeros_de_prueba


def flujo_whatsapp():
    # 1. Obtener la lista de números PRIMERO
    numeros_aprendices = obtener_numeros_del_api()
    
    # 1b. Verificar si tenemos números antes de abrir el navegador
    if not numeros_aprendices:
        print("❌ No se obtuvieron números para enviar. Terminando proceso.")
        return  # Salir del script si no hay nada que hacer

    # 2. Crear navegador (con persistencia de sesión)
    print("Iniciando navegador...")
    driver = crear_navegador()

    # 3. Crear instancia del módulo de WhatsApp
    wp = WhatsAppWeb(driver)

    # 4. Abrir WhatsApp Web (esperará si no está cargado)
    wp.abrir_whatsapp()

    print("--- INICIANDO ENVÍO DE MENSAJES ---")
    
    for numero in numeros_aprendices:
        print("---------------------------------")
        # 5. Iniciar chat con el número
        cuadro_de_texto = wp.iniciar_chat_con_numero(numero)
        
        # 6. Si el chat se abrió (el número es válido)...
        if cuadro_de_texto:
            # 7. Enviar el mensaje
            wp.enviar_mensaje(cuadro_de_texto, MENSAJE_A_ENVIAR)
        else:
            print(f"No se pudo enviar mensaje a {numero}. Saltando al siguiente.")
        
        # Pausa entre mensajes para evitar ser bloqueado
        print("Esperando 5 segundos antes del siguiente envío...")
        time.sleep(5)

    print("---------------------------------")
    print("✨ PROCESO FINALIZADO ✨")

    print("Proceso terminado. La ventana se cerrará en 10 segundos...")
    print("La sesión de WhatsApp Web quedará guardada.")
    time.sleep(10)

if __name__ == "__main__":
    flujo_whatsapp()