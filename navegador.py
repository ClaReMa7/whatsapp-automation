from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# PERSISTENCIA DE SESIÓN:
# Chrome guarda automáticamente las cookies y sesión en la carpeta --user-data-dir
# Primera ejecución: Se pedirá escanear el QR de WhatsApp
# Ejecuciones posteriores: Chrome recordará la sesión, sin necesidad de QR nuevamente
# La carpeta chrome-profile/ está en .gitignore - no se sube a GitHub
# 
# Funciona en: Windows, Linux, Mac (rutas multiplataforma)

CHROME_PROFILE_PATH = os.path.abspath("./chrome-profile")

class Navegador:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        
        # --user-data-dir especifica dónde guardar la sesión de Chrome
        chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        self.wait = WebDriverWait(self.driver, 20)

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
