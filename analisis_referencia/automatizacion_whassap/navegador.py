from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config import SESSION_PATH, CHROME_PATH, WHATSAPP_URL

def iniciar_navegador():
    print("📌 Iniciando navegador...")

    options = Options()
    options.add_argument("--start-maximized")

    # Guardar sesión
    print(f"📌 Usando carpeta de sesión: {SESSION_PATH}")
    options.add_argument(f"--user-data-dir={SESSION_PATH}")

    # Ruta personalizada de Chrome
    if CHROME_PATH:
        print(f"📌 Usando Chrome en: {CHROME_PATH}")
        options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print("📌 Abriendo WhatsApp Web...")
    driver.get(WHATSAPP_URL)

    print("⏳ Esperando que WhatsApp cargue...")
    return driver
