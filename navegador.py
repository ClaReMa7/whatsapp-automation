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
        chrome_options.add_argument("--disable-sync")  # Desactivar sincronización
        chrome_options.add_argument("--disable-default-apps")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Opciones para evitar crashes al usar carpeta persistente
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # 1. Carpetta para persistencia de sesión
        if USER_DATA_PATH:
            # Crear directorio si no existe
            if not os.path.exists(USER_DATA_PATH):
                os.makedirs(USER_DATA_PATH, exist_ok=True)
                print(f"✔ Carpeta de sesión creada: {USER_DATA_PATH}")
            else:
                print(f"✔ Usando carpeta de sesión existente: {USER_DATA_PATH}")
            chrome_options.add_argument(f"--user-data-dir={os.path.abspath(USER_DATA_PATH)}")
            chrome_options.add_argument("--profile-directory=Default")  # Usar perfil Default
        else:
            print("ADVERTENCIA: No se definió 'CHROME_USER_DATA_PATH' en .env. La sesión NO será persistente.")
        
        # 2. Ubuicación del binario de Chrome
        if BINARY_PATH:
            if os.path.exists(BINARY_PATH):
                print(f"✔ Usando binario de Chrome en: {BINARY_PATH}")
                chrome_options.binary_location = BINARY_PATH
            else:
                print(f"⚠️  ADVERTENCIA: La ruta '{BINARY_PATH}' no existe.")
                print("Se usará Chrome de la ruta por defecto.")
        else:
            print("INFO: No se definió 'CHROME_BINARY_PATH'. Se usará Chrome de la ruta por defecto.")

        # Crear la instancia del navegador
        try:
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            print("✔ Chrome iniciado exitosamente con sesión persistente.")
            print("ℹ️  La sesión se guardará entre ejecuciones.")
        except Exception as e:
            print(f"❌ Error al iniciar Chrome: {e}")
            print("\nSolución:")
            print("  1. Cierra completamente todas las instancias de Chrome")
            print("  2. Elimina la carpeta chrome-profile si es corrupta:")
            print(f"     Remove-Item '{USER_DATA_PATH}' -Recurse -Force")
            print("  3. Intenta nuevamente")
            raise

        self.wait = WebDriverWait(self.driver, 20)

    def abrir_url(self, url):
        self.driver.get(url)

    def esperar(self, by, valor):
        return self.wait.until(EC.presence_of_element_located((by, valor)))

    def cerrar(self):
        self.driver.quit()


def crear_navegador():
    return Navegador().driver
