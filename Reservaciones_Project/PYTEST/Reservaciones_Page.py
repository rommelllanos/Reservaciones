import ssl
import time
import pytest
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from Funciones_Cobranza import Funciones_ModuloUNo

class Funciones_Reservaciones():

    def __init__(self,driver):
        self.driver=driver


    def Reservacion_Uno(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f=Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 5)
        f.Click_ID_Validar("idSIButton9", 3)
        time.sleep(2)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']",3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3)#puesto 1
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) #puesto 2
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) #puesto 3
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) #puesto 4
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3) #puesto 8
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3)#puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]",3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        #next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        #print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])[2]", 5)
        #f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)

        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Dos(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f=Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']",3)
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3)#puesto 1
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) #puesto 2
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) #puesto 3
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) #puesto 4
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3) #puesto 8
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3)#puesto 10
        time.sleep(3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]",3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')]", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Tres(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f=Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']",3)
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) #puesto 3
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3) #puesto 8
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre, 3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]",3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)



    def Reservacion_Cuatro(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f = Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u",5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']", 3)
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3)  # puesto 4
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3) #puesto 8
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]",email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre, 3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Cinco(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f = Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']", 2)
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption22']", 3)  #puesto 5
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3)  # puesto 8
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Seis(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
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
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3)  #puesto 5
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption23']", 3)  # puesto 6
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3)  # puesto 8
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Siete(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
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
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3)  #puesto 5
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption24']", 3)  # puesto 7
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3)  # puesto 8
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)
    def Reservacion_Ocho(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
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
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3)  # puesto 8
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Nueve(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f=Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']",3)
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3) #puesto 8
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        #f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3) #puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]",3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Diez(self, email, clave, email2, nombre):
        driver = webdriver.Chrome()
        f = Funciones_ModuloUNo(driver)
        f.Open_Page(
            "https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u",
            5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption6']", 3)
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3) # puesto 1
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3) # puesto 2
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3) # puesto 3
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption21']", 3) # puesto 4
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption25']", 3) #puesto 8
        # f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption26']", 3) #puesto 9
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption27']", 3)  # puesto 10
        time.sleep(3)

        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre, 3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Once(self, email, clave, email2, nombre):
        driver = webdriver.Chrome()
        f = Funciones_ModuloUNo(driver)
        f.Open_Page(
            "https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u",
            5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption7']", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption18']", 3)  # puesto 1
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre, 3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Doce(self, email, clave, email2, nombre):
        driver = webdriver.Chrome()
        f = Funciones_ModuloUNo(driver)
        f.Open_Page(
            "https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u",
            5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption7']", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption19']", 3)  # puesto 2
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre, 3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]", 3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)

    def Reservacion_Trece(self,email,clave,email2,nombre):
        driver= webdriver.Chrome()
        f=Funciones_ModuloUNo(driver)
        f.Open_Page("https://forms.office.com/pages/responsepage.aspx?id=2ua7Zek1GEyZO-4sFst-ZNqAzElf8tdMs1hvkR085LRUMDBBNElURzk0M1dGVTM5OUJWTVdVTThXRi4u", 5)
        f.Texto_ID_Validar_Click("i0116", email, 3)
        f.Click_ID_Validar("idSIButton9", 3)
        f.Texto_ID_Validar_Click("i0118", clave, 3)
        f.Click_ID_Validar("idSIButton9", 2)
        f.Click_ID_Validar("idSIButton9", 5)
        f.Click_XPATH_Validar("//div[@id='form-main-content1']/div/button/div", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption4']", 3)
        f.Check_XPATH("//*[@id='QuestionChoiceOption7']", 3)
        f.Click_XPATH_Validar("//*[@id='QuestionChoiceOption20']", 3)  # puesto 3
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[1]", email2, 3)
        f.Texto_XPATH_Validar_Click("(//input[contains(@aria-label,'Texto de una sola línea')])[2]", nombre,3)
        f.Click_XPATH_Validar("//i[contains(@data-icon-name,'Calendar')]",3)
        #f.Click_XPATH_Validar("//i[@data-icon-name='Down'][contains(.,'')]", 2)
        #f.Click_XPATH_Validar("(//span[@aria-hidden='true'][contains(.,'29')])[2]", 5)
        # Obtener la fecha actual
        today = datetime.date.today()
        print(f"Fecha actual: {today}")
        # Calcular el próximo martes y miércoles
        next_tuesday = today + datetime.timedelta((1 - today.weekday() + 7) % 7)
        print(f"Próximo martes: {next_tuesday}")
        # next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # print(f"Próximo miercoles: {next_wednesday}")
        # Seleccionar el próximo  miércoles
        f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_tuesday.day}')])", 5)
        # f.Click_XPATH_Validar(f"(//span[@aria-hidden='true'][contains(.,'{next_wednesday.day}')])", 5)'''
        f.Click_XPATH_Validar("//button[contains(@data-automation-id,'submitButton')]", 3)




        driver.close()