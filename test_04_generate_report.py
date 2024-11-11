from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time
import os

class TestEstudiante(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")
        
    def test_01_create_report(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        # Navegación a inicio de sesión
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        # Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")
        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Iniciar sesión
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        students_button = self.driver.find_element(By.LINK_TEXT, "Estudiantes")
        students_button.click()

        report_button = self.driver.find_element(By.LINK_TEXT, "Generar Reporte")
        report_button.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/students/report", self.driver.current_url)

        all_button = self.driver.find_element(By.ID, "Todos")
        all_button.click()
        time.sleep(3)

        submit = self.driver.find_element(By.CLASS_NAME, "report__form__submit")
        submit.click()
        
        time.sleep(4)
        self.assertEqual("https://fonmala.nyc.dom.my.id/students/report", self.driver.current_url)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
