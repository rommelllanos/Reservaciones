# ReservaPuesto.py
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from config import CHROME_DRIVER_PATH, FORM_LINK, puestos, MSFT_EMAIL, MSFT_PASSWORD

# Opciones globales de Chrome con sesión activa de Office365
chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\selenium_profiles\automation")
chrome_options.add_argument(r"--user-data-dir=C:\selenium_profiles\automation")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-features=VoiceTranscription")
chrome_options.add_argument("--disable-features=GCM")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

def ensure_logged_in():
    """
    Verifica si la sesión de Microsoft 365 está activa. 
    Si expira o no existe, rellena usuario/contraseña, selecciona la cuenta adecuada
    en la pantalla “Pick an account” y espera la aprobación de MFA.
    Corre antes de ejecutar múltiples fill_form.
    """
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH, log_path="NUL"), options=chrome_options)
        wait = WebDriverWait(driver, 10)

        # Ir al enlace principal; esto forzará el login si la sesión expiró
        driver.get(FORM_LINK)
        time.sleep(1)

        # 1) ¿Apareció el campo de correo (i0116)? => hay que loguear
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
            email_field.clear()
            email_field.send_keys(MSFT_EMAIL)
            driver.find_element(By.ID, "idSIButton9").click()
            time.sleep(1)

            # 2) ¿Apareció la pantalla “Pick an account”? (lista de cuentas guardadas)
            try:
                # Esperar hasta que aparezca el texto de la cuenta actual
                account_tile = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f"//div[@role='button' and normalize-space(text())='{MSFT_EMAIL}']")
                    )
                )
                account_tile.click()
                print("Se seleccionó la cuenta existente en 'Pick an account'.")
                time.sleep(4)
            except:
                # Si no aparece la lista, quizás la sesión no la requiere o ya pasó directo a contraseña
                pass

            # 3) Ahora la página de contraseña (i0118)
            pwd_field = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
            pwd_field.clear()
            pwd_field.send_keys(MSFT_PASSWORD)
            driver.find_element(By.ID, "idSIButton9").click()
            time.sleep(4)

            # 4) “Mantener sesión iniciada” (idSIButton9) tras contraseña
            try:
                stay_signed_in = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
                stay_signed_in.click()
                print("Se aceptó 'Mantener sesión iniciada'. \n")
            except:
                pass

            print("Credenciales enviadas. Esperando aprobación de MFA en el dispositivo móvil...")
            # 5) Esperar a redirección final a Forms (MFA completado)
            wait.until(EC.url_contains("forms.office.com"))
            print("MFA aprobado. Sesión iniciada correctamente. \n")
        except:
            # Si en ~10s no apareció el campo de correo, la sesión sigue activa
            print("Sesión de Microsoft 365 válida. No se solicitó login. \n")
    except Exception as e:
        print(f"[Error en ensure_logged_in] {e}")
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

def fill_form(link, valores_puesto):
    """
    Abre el formulario (link), intenta hacer clic en 'Comenzar/Next' si existe,
    recarga la página para limpiar cualquier selección previa y luego continúa
    seleccionando según valores_puesto = (piso_value, area_value, puesto_id, usr_value, usr_name).
    """
    driver = None
    piso_value, area_value, puesto_id, usr_value, usr_name = valores_puesto
    

    try:
        # 1) Inicializa WebDriver (Chrome) apuntando al chromedriver y al perfil
        driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH, log_path="NUL"), options=chrome_options)
        wait = WebDriverWait(driver, 15)

        driver.refresh()

        # 2) Abre la URL del formulario
        driver.get(link)
        print(f"[{puesto_id}] Se abrió la URL del formulario")

        # 3) Intentar hacer clic en “Comenzar/Next”
        try:
            btn = driver.find_element(By.XPATH, "//div[text()='Start now']")
            btn.click()
            print(f"[{puesto_id}] Se hizo clic en 'Start now' rápidamente (sin WebDriverWait)")
        except Exception:
            # 2) Si no existe al instante, hacemos una espera muy corta:
            try:
                WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@id='form-main-content1']/div/button/div"))
                ).click()
                print(f"[{puesto_id}] Se hizo clic en 'Start now' con espera corta (2s)")
            except Exception as e:
                print(f"ERROR: no se pudo encontrar ni clicar 'Start now': {e}")

        # 4) Seleccionar “Piso” (por data-automation-value)
        try:
            xpath_piso = f"//span[@data-automation-value='{piso_value}']"
            radio_piso = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_piso)))
            radio_piso.click()
            print(f"[{puesto_id}] Se marcó la opción de piso '{piso_value}'")
        except Exception as e:
            print(f"[{puesto_id}] ERROR: no se pudo clicar el <span> para piso '{piso_value}': {e}")
            driver.quit()
            return

        # 5) Seleccionar “Área” (por data-automation-value)
        try:
            xpath_area = f"//span[contains(@data-automation-value,'{area_value}')]"
            radio_area = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_area)))
            radio_area.click()
            print(f"[{puesto_id}] Se marcó la opción de área '{area_value}'")
        except Exception as e:
            print(f"[{puesto_id}] ERROR: no se pudo clicar el <span> para área '{area_value}': {e}")
            driver.quit()
            return

        # 6) Seleccionar el puesto específico (por data-automation-value)
        try:
            xpath_puesto = f"//span[contains(@data-automation-value,'{puesto_id}')]"
            radio_puesto = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_puesto)))
            radio_puesto.click()
            print(f"[{puesto_id}] Se marcó la opción de puesto '{puesto_id}'")
        except Exception as e:
            print(f"[{puesto_id}] ERROR: no se pudo clicar el <span> para puesto '{puesto_id}': {e}")
            driver.quit()
            return

        # 7) Localizamos todos los inputs de “texto de una sola línea”:
        text_inputs = driver.find_elements(By.XPATH, "//input[@data-automation-id='textInput']")

        # 8) Rellenamos el correo corporativo:
        if len(text_inputs) >= 1:
            correo_input = text_inputs[0]
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-automation-id='textInput'][1]")))
            correo_input.clear()
            correo_input.send_keys(f"{usr_value}@veconinter.com")
            print(f"[{puesto_id}] Se agregó {usr_value}@veconinter.com en el primer campo de texto")

        # 9) Rellenamos el nombre y apellido:
        if len(text_inputs) >= 2:
            nombre_input = text_inputs[1]
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-automation-id='textInput'][1]")))
            nombre_input.clear()
            nombre_input.send_keys({usr_name})
            print(f"[{puesto_id}] Se agregó {usr_name} en el segundo campo de texto")

        # 10) Localizar el input de fecha dentro de dateContainer (independiente del idioma)
        try:
            date_inp = wait.until(
                EC.element_to_be_clickable((By.XPATH,
                    "//*[@data-automation-id='dateContainer']//input"
                ))
            )
            # Calculamos la fecha a 5 días desde hoy
            hoy = datetime.date.today()
            fecha_objetivo = hoy + datetime.timedelta(days=5)

            # Formateamos como M/D/YYYY (sin ceros a la izquierda)
            mes = fecha_objetivo.month
            dia = fecha_objetivo.day
            anio = fecha_objetivo.year
            fecha_str = f"{mes}/{dia}/{anio}"

            # Enviamos la fecha calculada
            # Limpiar el campo de fecha mediante Ctrl+A + Delete
            date_inp.send_keys(Keys.CONTROL, "a")
            date_inp.send_keys(Keys.DELETE)
            date_inp.send_keys(fecha_str)
            print(f"[{puesto_id}] Se ingresó '{fecha_str}' en el campo de fecha")
        except Exception as e:
            print(f"[{puesto_id}] ERROR: no se pudo localizar el input de fecha: {e}")

        # 11) Clic en “Enviar” (submitButton)
        try:
            
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-automation-id,'submitButton')]"))
            ).click()
            time.sleep(1)
            print(f"[{puesto_id}] Se hizo clic en el botón 'Enviar'")
        except Exception as e:
            print(f"[{puesto_id}] ERROR: no se pudo clicar botón de enviar: {e}")
            driver.quit()
            return

        print(f"[{puesto_id}] ✓ Reserva completada para '{puesto_id}'")

    except Exception as e:
        print(f"[Error general][{puesto_id}]: {e}")

    finally:
        if driver:
            try:
                driver.quit()
                print(f"[{puesto_id}] Se cerró el WebDriver\n")
            except:
                pass

if __name__ == "__main__":
    # Primero, asegurar que la sesión de Microsoft 365 esté activa y el MFA aprobado
    ensure_logged_in()

    # Luego, ejecutar fill_form para cada puesto
    for puesto in puestos:
        fill_form(FORM_LINK, puesto)
        time.sleep(1)

    # Pequeña espera final para revisar resultados
    time.sleep(10)
