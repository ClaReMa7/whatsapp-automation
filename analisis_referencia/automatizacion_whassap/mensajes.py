from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CONTACTO, MENSAJE
import time

def enviar_mensaje(driver):
    print("📌 Buscando el cuadro de búsqueda...")

    try:
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
        )
        print("✔ Cuadro de búsqueda encontrado.")

        print(f"📌 Buscando contacto: {CONTACTO}")
        search_box.clear()
        search_box.send_keys(CONTACTO)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)

        print("⏳ Abriendo conversación...")
        time.sleep(3)

        print("📌 Buscando el cuadro para escribir mensaje...")
        message_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']"))
        )
        print("✔ Cuadro de mensaje encontrado.")

        print(f"📌 Escribiendo mensaje: {MENSAJE}")
        message_box.send_keys(MENSAJE)
        time.sleep(1)

        print("📌 Enviando mensaje...")

        # PRIMER MÉTODO: Presionar ENTER
        message_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # SEGUNDO MÉTODO: Clic en botón de enviar (nuevo diseño WhatsApp)
        try:
            send_btn = driver.find_element(By.XPATH, "//span[@data-icon='send']")
            send_btn.click()
            print("✔ Botón de enviar presionado.")
        except:
            print("⚠ No se encontró botón de enviar, pero ENTER ya se envió.")

        print("✨ MENSAJE ENVIADO ✨")

    except Exception as e:
        print("❌ ERROR al enviar el mensaje:", e)
