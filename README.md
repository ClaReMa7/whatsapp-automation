# WhatsApp Automation

Automatización para enviar mensajes a través de WhatsApp Web utilizando Selenium y Python.

## 📋 Descripción

Este proyecto permite automatizar el envío de mensajes masivos por WhatsApp Web. La herramienta utiliza Selenium para controlar un navegador Chrome automatizado y envía mensajes a números telefónicos específicos.

**Características principales:**
- ✅ Persistencia de sesión entre ejecuciones
- ✅ No requiere escanear QR en ejecuciones posteriores
- ✅ Envío de mensajes automático a múltiples números
- ✅ Interfaz simple y directa
- ✅ Compatible con Windows

## 🛠️ Requisitos

- **Python 3.8+** (probado con 3.14)
- **Google Chrome** instalado en `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **pip** (gestor de paquetes de Python)

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ClaReMa7/whatsapp-automation.git
cd whatsapp-automation
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
CHROME_USER_DATA_PATH=./chrome-profile
CHROME_BINARY_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe
```

**O** copia el archivo de ejemplo:
```bash
copy .env.example .env
```

## 🚀 Uso

### Primera ejecución

```bash
python main.py
```

En la primera ejecución:
1. Se abrirá una ventana de Chrome
2. Deberás escanear el código QR de WhatsApp Web manualmente
3. La sesión se guardará automáticamente

### Ejecuciones posteriores

```bash
python main.py
```

Las siguientes ejecuciones **no requerirán escanear QR** porque la sesión se mantiene guardada en la carpeta `chromeWhatsapp/`.

## 📁 Estructura del proyecto

```
whatsapp_automation/
├── main.py              # Script principal de automatización
├── navegador.py         # Gestor del navegador Chrome/Selenium
├── whatsapp_web.py      # Interacción con WhatsApp Web
├── requirements.txt     # Dependencias del proyecto
├── .env                 # Variables de entorno (NO se sube a Git)
├── .env.example         # Plantilla de variables de entorno
├── .gitignore           # Archivos ignorados por Git
├── chromeWhatsapp/      # Sesión persistente de Chrome (NO se sube a Git)
└── README.md            # Este archivo
```

## 📜 Descripción de archivos

### `main.py`
Script principal que orquesta el flujo de automatización:
- Obtiene lista de números telefónicos
- Inicia el navegador Chrome
- Abre WhatsApp Web
- Envía mensajes a cada número con retrasos entre envíos

### `navegador.py`
Gestor de Selenium WebDriver:
- Configura y crea instancia de Chrome
- Define opciones de seguridad y rendimiento
- Implementa métodos para abrir URLs y cerrar navegador

### `whatsapp_web.py`
Controlador de la interfaz de WhatsApp Web:
- `abrir_whatsapp()`: Navega a WhatsApp Web
- `iniciar_chat_con_numero()`: Abre un chat con un número específico
- `enviar_mensaje()`: Envía un mensaje de texto

## 🔧 Configuración avanzada

### Cambiar el binario de Chrome

Si tienes Chrome instalado en una ruta diferente, edita `.env`:

```env
CHROME_BINARY_PATH=C:\ruta\a\tu\chrome.exe
```

### Cambiar la ruta de datos del usuario

Para usar una carpeta diferente de sesión:

```env
CHROME_USER_DATA_PATH=C:\ruta\a\otra\sesion
```

### Agregar más números

En `main.py`, función `obtener_numeros_del_api()`, cambia la lista de prueba:

```python
numeros_prueba = [
    '573042836000',  # Reemplaza con tus números
    '573001214567',
    # ... más números
]
```

## ⚙️ Dependencias

- **selenium** (4.38.0): Automatización del navegador
- **webdriver-manager** (4.0.2): Gestión automática del ChromeDriver
- **python-dotenv**: Carga de variables de entorno

## 🔒 Seguridad

⚠️ **Importante:**
- El archivo `.env` contiene rutas sensibles y **NO debe subirse a Git**
- La carpeta `chromeWhatsapp/` contiene datos de sesión y **NO debe subirse a Git**
- Ambos están protegidos en `.gitignore`

## 🐛 Solución de problemas

### "No Chrome binary at..."
- Verifica que Chrome esté instalado en la ruta especificada en `.env`
- O instala Chrome en la ruta por defecto: `C:\Program Files\Google\Chrome\Application\chrome.exe`

### "invalid session id"
- Elimina la carpeta `chromeWhatsapp/`
- Ejecuta nuevamente para crear una nueva sesión
- Escanea el QR cuando aparezca

### "element not found"
- WhatsApp Web puede haber cambiado su estructura HTML
- Los selectores en `whatsapp_web.py` podrían necesitar actualización
- Abre WhatsApp Web manualmente en Chrome para verificar los cambios

### Se pide QR en cada ejecución
- Verifica que `chromeWhatsapp/` exista y esté en la raíz del proyecto
- Comprueba que `.gitignore` incluya `chromeWhatsapp/` (para que no se elimine)
- Puede ocurrir si WhatsApp considera la sesión expirada (después de ~7-30 días sin usar)

## 📱 Consideraciones importantes

- ⏱️ Hay un retraso de 5 segundos entre cada mensaje para evitar bloqueos
- 🔐 La sesión puede expirar después de 7-30 días sin usar
- 📲 Debes tener WhatsApp instalado en tu teléfono y activo
- 🌐 Requiere conexión a Internet activa
- ⚠️ No intentes usar múltiples instancias simultáneamente (WhatsApp Web detectará la sesión duplicada)

## 🎯 Flujo de ejecución

```
1. Lanzar main.py
   ↓
2. Crear instancia de navegador Chrome con sesión persistente
   ↓
3. Abrir WhatsApp Web
   ↓
4. [Primera vez] Escanear QR (sesión se guarda en chromeWhatsapp/)
   [Veces posteriores] Cargar sesión guardada automáticamente
   ↓
5. Para cada número telefónico:
   - Abrir chat con el número
   - Enviar mensaje
   - Esperar 5 segundos
   ↓
6. Cerrar navegador
   ↓
7. Fin
```

## 👨‍💻 Desarrollador

**Claudia Redondo** - Automatización de WhatsApp Web con Selenium

## 📝 Licencia

Este proyecto es privado.

## 🤝 Contribuciones

Para reportar bugs o sugerencias, contacta con el desarrollador.

---

**Nota:** Este script está diseñado para uso personal y educativo. Asegúrate de cumplir con los términos de servicio de WhatsApp.
