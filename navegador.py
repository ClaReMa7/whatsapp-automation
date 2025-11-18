import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Carga las variables del archivo .env al entorno
load_dotenv()

USER_DATA_PATH = os.getenv("CHROME_USER_DATA_PATH")
BINARY_PATH = os.getenv("CHROME_BINARY_PATH")

class Navegador:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # 1. Carpetta para persistencia de sesión
        if USER_DATA_PATH:
            print(f"Usando carpeta de sesión: {USER_DATA_PATH}")
            chrome_options.add_argument(f"--user-data-dir={USER_DATA_PATH}")
        else:
            print("ADVERTENCIA: No se definió 'CHROME_USER_DATA_PATH' en .env. La sesión NO será persistente.")
        # 2. Ubuicación del binario de Chrome
        if BINARY_PATH:
            print(f"Usando binario de Chrome en: {BINARY_PATH}")
            chrome_options.binary_location = BINARY_PATH
        else:
            print("INFO: No se definió 'CHROME_BINARY_PATH'. Se usará Chrome de la ruta por defecto.")

        # Crear la instancia del navegador
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        self.wait = WebDriverWait(self.driver, 20)

    def abrir_url(self, url):
        self.driver.get(url)

    def esperar(self, by, valor):
        return self.wait.until(EC.presence_of_element_located((by, valor)))

    def cerrar(self):
        self.driver.quit()


def crear_navegador():
    return Navegador().driver
