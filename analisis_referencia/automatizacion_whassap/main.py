from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

print("🚀 INICIANDO AUTOMATIZACIÓN DE WHATSAPP...")

options = Options()
options.add_argument("--user-data-dir=" + CHROME_PROFILE)
service = Service(CHROMEDRIVER_PATH)

print("📌 Iniciando navegador...")
print(f"📌 Usando carpeta de sesión: {CHROME_PROFILE}")

driver = webdriver.Chrome(service=service, options=options)

print("📌 Abriendo WhatsApp Web...")
driver.get(WHATSAPP_URL)
time.sleep(8)

print("⏳ Verificando si WhatsApp Web cargó...")

# --- Paso 1: Buscar contacto ---
try:
    print("📌 Buscando el cuadro de búsqueda...")
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    print("✔ Cuadro de búsqueda encontrado.")
except:
    print("❌ ERROR: No se encontró el cuadro de búsqueda.")
    driver.quit()
    exit()

search_box.click()
time.sleep(1)
search_box.send_keys(CONTACTO)
print(f"📌 Buscando contacto: {CONTACTO}")
time.sleep(3)
search_box.send_keys(Keys.ENTER)

print("⏳ Abriendo conversación...")
time.sleep(3)

# --- Paso 2: Escribir mensaje ---
try:
    print("📌 Buscando el cuadro para escribir mensaje...")
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    print("✔ Cuadro de mensaje encontrado.")
except:
    print("❌ ERROR: No se encontró el cuadro para escribir el mensaje.")
    driver.quit()
    exit()

print(f"📌 Escribiendo mensaje: {MENSAJE}")
message_box.click()
message_box.send_keys(MENSAJE)
time.sleep(1)

print("📌 Enviando mensaje...")
message_box.send_keys(Keys.ENTER)

print("✨ MENSAJE ENVIADO (SI LA CONVERSACIÓN SE ABRIÓ CORRECTAMENTE) ✨")
print("🏁 PROCESO FINALIZADO.")

# 👉 AGREGA ESTO PARA QUE LA VENTANA NO SE CIERRE
print("⏳ Esperando antes de cerrar el navegador...")
time.sleep(10)  # Espera 10 segundos
