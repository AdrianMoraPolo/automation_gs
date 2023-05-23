
import time
import unittest
import pytest
import re


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from functions.global_functions import globalfunctions



class testgoogle(unittest.TestCase):

    @pytest.mark.validar
    # Importamos chromedriver para poder realizar los test en Chrome
    def setUp(self):
        driver_service = Service(executable_path="\path\chromedriver.exe")
        self.driver = webdriver.Chrome(service=driver_service)

    def test1(self):
        driver=self.driver
        f=globalfunctions(driver)
        # Link de la página y expandimos la ventana a pantalla completa
        f.route("https://www.google.es/")
        # Esperamos 1 segundo (importado arriba en time)
        time.sleep(1)
        # Hacemos click en el botón de aceptar terminos
        driver.find_element(By.ID, "L2AGLb").click()
        time.sleep(1)
        # Buscamos el elemento por ID
        search = driver.find_element(By.ID, "APjFqb")
        # Introducimos la palabra deseada para buscar en el input
        search.send_keys("Apple")
        time.sleep(1)
        # Hacemos click en buscar
        driver.find_element(By.XPATH, "(//input[@class='gNO89b'])[1]").click()
        time.sleep(1)
        # Recogemos la cantidad de resultados
        results_number = driver.find_element(By.ID, "result-stats").text
        # Extraemos solo los digitos
        number = re.findall(r'\d+', results_number)
        # Los unimos para tener un solo numero que poder manipular
        clean_text = ''.join(number)
        # Convertimos el texto limpio a uno entero
        results = int(clean_text)
        # Comprobamos si superamos los 100,000 resultados o no
        if results > 100000:
            print(" More than 100,000 results [OK]")
        else:
            print(" Less than 10,000 results [NOK]")
        #Obtenemos evidencias del resultado de la prueba
        element = driver.find_element(By.ID, "cnt")
        location = element.location
        size = element.size
        driver.save_screenshot("Screenshots\screenshot.png")
        driver.close()