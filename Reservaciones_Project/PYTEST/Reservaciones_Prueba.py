import ssl
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones_Cobranza import Funciones_ModuloUNo

class Funciones_Reservaciones():

    def __init__(self, driver):
        self.driver = driver

    def Reservacion_Uno(self, email, clave, email2, nombre):
        driver = webdriver.Chrome()
        f = Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3)  # puesto 1
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre, 3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)

        # Obtener la fecha actual
        today = datetime.date.today()

        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)

        # Seleccionar el próximo martes y miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])[2]", 5)
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])[2]", 5)

        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)