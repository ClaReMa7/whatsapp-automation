from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navegador:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        chrome_options.add_argument(r"--user-data-dir=C:\Users\andre\AppData\Local\ChromeSelenium")

        # Forzar la ruta del binario
        chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


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
