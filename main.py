# main.py

from navegador import crear_navegador
from whatsapp_web import WhatsAppWeb

def flujo_whatsapp():
    # 1. Crear navegador
    driver = crear_navegador()

    # 2. Crear instancia del módulo de WhatsApp
    wp = WhatsAppWeb(driver)

    # 3. Abrir WhatsApp Web
    wp.abrir_whatsapp()

    # 4. Esperar a que el usuario escanee el QR
    if not wp.esperar_sesion(timeout=80):
        print("No se inició sesión a tiempo. Terminando...")
        driver.quit()
        return

    # 5. Buscar el chat
    nombre = input("Escribe el nombre del contacto o grupo: ")

    if not wp.buscar_chat(nombre):
        print("No se pudo abrir el chat. Cerrando navegador...")
        driver.quit()
        return

    # 6. Enviar el mensaje
    mensaje = input("Escribe el mensaje a enviar: ")

    if wp.enviar_mensaje(mensaje):
        print("Mensaje enviado correctamente.")
    else:
        print("No fue posible enviar el mensaje.")

    # 7. Mantener el navegador abierto para que veas el resultado
    input("Presiona ENTER para cerrar...")
    driver.quit()

if __name__ == "__main__":
    flujo_whatsapp()
