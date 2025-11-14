# whatsapp_web.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time

class WhatsAppWeb:

    def __init__(self, driver):
        """
        driver: instancia del navegador creada desde navegador.py
        """
        self.driver = driver

    def abrir_whatsapp(self):
        """Abre WhatsApp Web y espera a que cargue."""
        self.driver.get("https://web.whatsapp.com")
        print("Abriendo WhatsApp Web...")

        time.sleep(8)  # Espera inicial para QR o carga

    def sesion_iniciada(self):
        """
        Retorna True si ya hay sesión iniciada.
        Verifica elementos que solo aparecen si WhatsApp está listo.
        """
        try:
            self.driver.find_element(By.XPATH, "//div[@role='textbox']")
            return True
        except NoSuchElementException:
            return False

    def esperar_sesion(self, timeout=60):
        """Espera a que el usuario escanee el código QR."""
        inicio = time.time()

        while time.time() - inicio < timeout:
            if self.sesion_iniciada():
                print("Sesión iniciada correctamente.")
                return True

            print("Esperando a que escanees el código QR...")
            time.sleep(5)

        return False

    def buscar_chat(self, nombre_contacto):
        """Busca un chat por nombre."""
        try:
            buscador = self.driver.find_element(By.XPATH, "//div[@role='textbox' and @data-tab='3']")
            buscador.click()
            buscador.clear()
            buscador.send_keys(nombre_contacto)
            time.sleep(2)

            chat = self.driver.find_element(By.XPATH, f"//span[@title='{nombre_contacto}']")
            chat.click()
            time.sleep(1)
            return True

        except NoSuchElementException:
            print(f"No se encontró el chat: {nombre_contacto}")
            return False

    def enviar_mensaje(self, texto):
        try:
            # Cuadro texto del mensaje
            cuadro = self.driver.find_element(
                By.XPATH,
                "//div[@data-tab='10' and @role='textbox']"
            )
            cuadro.click()
            cuadro.send_keys(texto)
            time.sleep(1)

            # Espera que aparezca el botón
            boton = self.driver.find_element(
                By.XPATH,
                "//*[@aria-label='Enviar' and @role='button']"
            )
            boton.click()
            time.sleep(1)

            return True

        except Exception as e:
            print("Error enviando mensaje:", e)
            return False