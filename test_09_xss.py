from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time

class XSS(unittest.TestCase):
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_01__create_xss_plan(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        # Navegacion a inicion de sesion
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        #Introducir credenciales
        username_field = self.driver.find_element(By.NAME, "correo")
        password_field = self.driver.find_element(By.NAME, "contrasenna")

        username_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        #Check de login 
        login_form_button = self.driver.find_element(By.CLASS_NAME, "form__submit")
        login_form_button.click()

        #Navegacion a gestion de planes
        plans_button = self.driver.find_element(By.LINK_TEXT, "Planes")
        plans_button.click()

        #Creacion de plan
        create_button = self.driver.find_element(By.CLASS_NAME, "plans__actions__create")
        create_button.click()

        #Introducir datos del plan
        name_field = self.driver.find_element(By.NAME, "nombre")
        description_field = self.driver.find_element(By.NAME, "descripcion")

        name_field.send_keys("XSS Plan - <script>alert('XSS');</script>")
        description_field.send_keys("Plan de prueba para XSS")

        #Guardar plan
        submit_button = self.driver.find_element(By.CLASS_NAME, "create-plan__form__submit")
        submit_button.click()


        time.sleep(2);

        # si hay un alert, aceptarlo
        try:
            print("XSS Detectado")
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

        time.sleep(2)
        self.assertEqual("https://fonmala.nyc.dom.my.id/plans", self.driver.current_url)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()