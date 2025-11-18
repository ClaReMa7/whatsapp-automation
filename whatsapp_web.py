# whatsapp_web.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WhatsAppWeb:

    def __init__(self, driver):
        """
        driver: instancia del navegador creada desde navegador.py
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def abrir_whatsapp(self):
        """Abre WhatsApp Web y espera a que cargue."""
        self.driver.get("https://web.whatsapp.com")
        print("Abriendo WhatsApp Web...")
        # Esperamos a que aparezca el cuadro de búsqueda, señal de que cargó
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @data-tab='3']"))
            )
            print("[OK] WhatsApp Web cargado.")
        except TimeoutException:
            print("[ERROR] No se pudo cargar WhatsApp Web (quizás necesites escanear QR la primera vez).")

    # --- FUNCIÓN PARA INICICIAR CHAT CON UN NUMERO (NO GUARDADO) ---
    def iniciar_chat_con_numero(self, numero_telefono):
        """
        Abre la ventana de chat con un número específico usando la URL.
        El número debe tener el prefijo del país (ej: 57311... para Colombia)
        """
        try:
            print(f"[INFO] Iniciando chat con {numero_telefono}...")
            url_chat = f"https://web.whatsapp.com/send?phone={numero_telefono}"
            self.driver.get(url_chat)
            
            # Esperar a que el cuadro de texto del chat esté listo
            # Este es el indicador de que el número es válido y el chat se abrió
            cuadro = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-tab='10' and @role='textbox']"))
            )
            print("[OK] Chat abierto.")
            return cuadro # Devolvemos el cuadro de texto para usarlo
        except TimeoutException:
            print(f"[ERROR] No se pudo abrir el chat con {numero_telefono}.")
            print("Posibles causas: El número no es válido, o hubo un error de carga.")
            # Esperamos a ver si hay un popup de error
            try:
                error_popup = self.driver.find_element(By.XPATH, "//div[contains(text(), 'no es válido')]")
                print(f"Mensaje de WhatsApp: {error_popup.text}")
            except:
                pass # No hubo popup de error
            return None
        except Exception as e:
            print(f"[ERROR] Error inesperado al iniciar chat: {e}")
            return None

    # --- ESTA FUNCIÓN ESTÁ MODIFICADA ---
    def enviar_mensaje(self, cuadro_texto, texto):
        """
        Envía un mensaje usando el cuadro de texto que
        obtuvimos de 'iniciar_chat_con_numero'.
        """
        try:
            print(f"Enviando mensaje: {texto}")
            cuadro_texto.click()
            cuadro_texto.clear()
            cuadro_texto.send_keys(texto)
            time.sleep(1) # Pequeña pausa
            
            # Presionar Enter para enviar
            cuadro_texto.send_keys(Keys.ENTER)
            
            # Esperar un momento para que se envíe
            time.sleep(2) 
            print("[OK] Mensaje enviado.")
            return True

        except Exception as e:
            print(f"[ERROR] Error enviando mensaje: {e}")
            return False

  