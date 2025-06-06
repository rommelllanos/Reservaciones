# config.py

import os

# 1) Ruta al ejecutable de ChromeDriver en tu máquina.
#    Cámbiala según corresponda. Ejemplo:
#    CHROME_DRIVER_PATH = r"C:\ruta\a\chromedriver.exe"
CHROME_DRIVER_PATH = "C:/drivers/chromedriver.exe"


# 2) URL del formulario de Microsoft Forms (SharePoint Forms) donde se reservan las sillas.
FORM_LINK = (
    "https://forms.office.com/pages/responsepage.aspx?"
    "id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u"
)


# 3) Carpeta “User Data” donde está tu perfil de Chrome con sesión ya iniciada.
#    Para crear un perfil genérico en Windows y guardar las cookies en un directorio propio, sigue estos pasos:
#      1. Presiona Windows+R para abrir "Ejecutar".
#      2. Escribe (o pega) lo siguiente y presiona Enter:
#           chrome.exe --user-data-dir="C:\selenium_profiles\automation"
#         Esto abrirá Chrome usando esa carpeta como "User Data". En lugar de cargar tu perfil habitual,
#         se creará un perfil nuevo y vacío en C:\selenium_profiles\automation.
#      3. Una vez se abra esa ventana de Chrome:
#           • Navega a https://portal.office.com o a cualquier servicio de Microsoft 365.
#           • Inicia sesión con tu cuenta y completa el proceso de autenticación (incluido el MFA si aplica).
#           • Verifica que has entrado correctamente y que tu sesión queda activa.
#      4. Cierra esa ventana de Chrome. Al cerrar, todas las cookies, contraseñas y permisos se guardarán en
#         C:\selenium_profiles\automation.
#      5. A partir de ahora, cada vez que Selenium arranque Chrome con:
#           chrome_options.add_argument("--user-data-dir=C:\\selenium_profiles\\automation")
#         heredará esa sesión de Microsoft 365 y no pedirá login ni MFA.
#
#    En Windows, la ruta por defecto de “User Data” es:
#      C:\Users\<TuUsuario>\AppData\Local\Google\Chrome\User Data
#    Pero al crear un perfil separado con --user-data-dir, usas tu propia carpeta (C:\selenium_profiles\automation)
#    para aislar esa sesión de la que uses en tu navegador habitual.
#
USER_DATA_DIR = r"C:\selenium_profiles\automation"

# 4) Si en la carpeta especificada (C:\selenium_profiles\automation) se tienen varios perfiles,
#    se puede indicar cuál usar. Por ejemplo, si se crea un subperfil llamado "Profile 1":
#      PROFILE_DIRECTORY = "Profile 1"
#    Dejar en None si solo se tiene el perfil “Default” dentro de esa carpeta.
PROFILE_DIRECTORY = None


# 5) Lista de puestos
#    Formato:
#       [ Piso, País, PuestoID, Usuario (parte local del email), NombreCompleto ]
puestos = [
    ["17 - América del Norte", "Panamá",   "PA10", "pserrano",    "Patricia Serrano"],
    ["17 - América del Norte", "Panamá",   "PA9", "jortega",      "Jesus Ortega"],
    ["17 - América del Norte", "Panamá",   "PA8", "jalbornoz",    "Jacqueline Albornoz"],
    ["17 - América del Norte", "Panamá",   "PA7", "mcrubio",      "Maria Claudia Rubio"],
    ["17 - América del Norte", "Panamá",   "PA6", "kmonsalve",    "Karen Monsalve"],
    ["17 - América del Norte", "Panamá",   "PA5", "jalves",       "Jonathan Alvez"],
    ["17 - América del Norte", "Panamá",   "PA4", "eshernandez",  "Esther Hernandez"],
    ["17 - América del Norte", "Panamá",   "PA3", "yoliveros",    "Yotzy Oliveros"],
    ["17 - América del Norte", "Panamá",   "PA2", "kzapata",      "Kevin Zapata"],
    ["17 - América del Norte", "Panamá",   "PA1", "rllanos",      "Rommel Llanos"],
    ["17 - América del Norte", "Barbados", "BB1", "rrosa",        "Ronald de la Rosa"],
    ["17 - América del Norte", "Barbados", "BB2", "yusalazar",    "Yuraima Salazar"],
    ["17 - América del Norte", "Barbados", "BB3", "mcelis",       "Maurio Celis"],
    ["17 - América del Norte", "Barbados", "BB4", "jpaternina",   "Javier Paternina"],
    ["17 - América del Norte", "Barbados", "BB5", "elozada",      "Emerio Lozada"],
]

# Credenciales de Microsoft 365 (modificar aquí si cambian)
MSFT_EMAIL = "email corporativo"
MSFT_PASSWORD = "password"