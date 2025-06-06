import ssl
import time
import json
import unittest

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

class Funciones_ModuloUNo():

    def __init__(self,driver):
        self.driver=driver

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t

    def Open_Page(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def Click_ID_Validar(self, ID, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.ID, ID)
                val.click()

                print("Dimos click en el elemento requerido")
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + ID")

    def Texto_ID_Validar_Click(self, ID, texto, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, ID)
                val.click()
                val.clear()
                val.send_keys(texto)

                print("Dimos click en el campo {} ".format(ID))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + ID")

    def Click_XPATH_Validar(self, XPATH, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.XPATH, XPATH)
                val.click()

                print("Dimos click en el campo {} ".format(XPATH))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + XPATH")

    def Texto_XPATH_Validar_Click(self, XPATH, texto, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, XPATH)
                val.click()
                val.clear()
                val.send_keys(texto)

                print("Dimos click en el campo {} ".format(XPATH))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + XPATH")

    def Click_CSS_Validar(self, CSS, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.CSS_SELECTOR, CSS)
                val.click()

                print("Dimos click en el campo {} ".format(CSS))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + CSS")


    def Validar_Texto(self, ID , Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.ID, ID)


                print(" Si se encontro el elemento Requerido {} ".format(ID))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + ID")


    def Validar_Texto_XPATH(self, XPATH , Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH )))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.XPATH, XPATH)


                print(" Si se encontro el elemento Requerido {} ".format(XPATH))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + ID")



    def Click_LinkText_Validar(self, TXT, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, TXT)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.LINK_TEXT, TXT)
                val.click()

                print("Dimos click en el campo {} ".format(TXT))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + TXT")


    def Select_XPATH_Type(self, XPATH, Tipo, Dato, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.XPATH, XPATH)
                val=Select(val)
                if(Tipo=="text"):
                    val.select_by_visible_text(Dato)
                elif(Tipo=="index"):
                    val.select_by_index(Dato)
                elif(Tipo=="value"):
                    val.select_by_value(Dato)
                print("El campo seleccionado {} ".format(Dato))
                t = time.sleep(Tiempo)
                return t


        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + XPATH")




    def Mouse_Double(self,tipo,selector,Tiempo):
        if(tipo=="XPATH"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val= self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Double Click en {}" .format(selector))
                t =time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + selector")
        elif (tipo == "ID"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Double Click en {}".format(selector))

                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + selector")

    def Check_XPATH(self, XPATH, Tiempo):
        try :

                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val=self.driver.find_element(By.XPATH, XPATH)
                val.click()
                print(" Click acertado en el elemento {} ".format(XPATH))
                t=time.sleep(Tiempo)
                return t

        except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento + XPATH")
