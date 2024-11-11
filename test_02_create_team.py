from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time
import os

class TestEquipo(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_02_create_team(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")
        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        equipo_button = self.driver.find_element(By.LINK_TEXT, "Equipo Guía")
        equipo_button.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/guias", self.driver.current_url)

        crearEquipo_button = self.driver.find_element(By.LINK_TEXT, "Crear Equipo de Trabajo")
        crearEquipo_button.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/guias/crear/equipo", self.driver.current_url)

        checkbox = self.driver.find_element(By.XPATH, "//input[@name='professors[]' and @value='12']")
        checkbox.click()
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='professors[]' and @value='11']")
        checkbox.click()
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='professors[]' and @value='10']")
        checkbox.click()
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='professors[]' and @value='9']")
        checkbox.click()
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='professors[]' and @value='8']")
        checkbox.click()

        year = self.driver.find_element(By.XPATH, "//option[@value='2020']")
        year.click()

        crear_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        crear_button.click()

        equipo_button = self.driver.find_element(By.LINK_TEXT, "Equipo Guía")
        equipo_button.click()
        crearEquipo_button = self.driver.find_element(By.LINK_TEXT, "Ver y Eliminar Equipo de Trabajo")
        crearEquipo_button.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/ver/eliminar/equipo", self.driver.current_url)

        crearEquipo_button = self.driver.find_element(By.XPATH, "//a[contains(@href, '/ver/equipo/trabajo?id=Equipo Guía Primer Ingreso 2020')]")
        crearEquipo_button.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/ver/equipo/trabajo?id=Equipo%20Gu%C3%ADa%20Primer%20Ingreso%202020", self.driver.current_url)

        
    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()