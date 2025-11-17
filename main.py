# main.py

from navegador import crear_navegador
from whatsapp_web import WhatsAppWeb
import time

# --- Esta es la alternativa al API  ---
# ¡IMPORTANTE! Los números deben incluir el código de país,
# por ejemplo, 57 para Colombia, sin el '+' o '00'.
numeros_aprendices = [
    "573042836668",  
    "573044468766",  
    "573194989976"   
]

# Mensaje que se enviará
mensaje = "Hola ¿Cómo estás? Esto es una prueba."

def flujo_whatsapp():
    # 1. Crear navegador (ccon persistencia de sesión)
    print("Iniciando navegador...")
    driver = crear_navegador()

    # 2. Crear instancia del módulo de WhatsApp
    wp = WhatsAppWeb(driver)

    # 3. Abrir WhatsApp Web (esperará si no está cargado)
    wp.abrir_whatsapp()

    print("--- INICIANDO ENVÍO DE MENSAJES ---")
    
    for numero in numeros_aprendices:
        print("---------------------------------")
        # 4. Iniciar chat con el número
        cuadro_de_texto = wp.iniciar_chat_con_numero(numero)
        
        # 5. Si el chat se abrió (el número es válido)...
        if cuadro_de_texto:
            # 6. Enviar el mensaje
            wp.enviar_mensaje(cuadro_de_texto, mensaje)
        else:
            print(f"No se pudo enviar mensaje a {numero}. Saltando al siguiente.")
        
        # Pausa entre mensajes para evitar ser bloqueado
        print("Esperando 5 segundos antes del siguiente envío...")
        time.sleep(5)

    print("---------------------------------")
    print("✨ PROCESO FINALIZADO ✨")

    # 7. Mantener el navegador abierto para que veas el resultado
    input("Presiona ENTER para cerrar...")
    driver.quit()

if __name__ == "__main__":
    flujo_whatsapp()