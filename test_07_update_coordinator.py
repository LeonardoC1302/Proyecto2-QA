import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Update_Coordinator(unittest.TestCase):
    
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")
    
    def test_01_give_coordinator(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        # Ingresar a la página de login
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/login", self.driver.current_url)

        # Ingresar credenciales
        email = self.driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys("admin@admin.com")

        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("admin")

        # Presiona el botón de login
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".form__submit")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id", self.driver.current_url)

        # Acceder a la pagina de profesores
        login_button = self.driver.find_element(By.LINK_TEXT, "Profesores")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/professors", self.driver.current_url)

        self.driver.find_element(By.XPATH, "//a[@href='/professors/coordinator' and @class='professors_actions__coordinator']").click()

        self.assertIn("https://fonmala.nyc.dom.my.id/professors/coordinator", self.driver.current_url)

        button = self.driver.find_element(By.CLASS_NAME, 'coordinator__form__label--radio')
        button.click()

        sleep(2)

        coordinador_button = self.driver.find_element(By.XPATH, '//label[.//input[@type="radio" and @class="coordinator__form__radio" and @value="12"]]')
        coordinador_button.click()

        submit_button = self.driver.find_element(By.CLASS_NAME, 'coordinator__form__submit')
        submit_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/professors", self.driver.current_url)

    def test_02_view_team(self):
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
        viewButton = self.driver.find_element(By.LINK_TEXT, "Ver y Eliminar Equipo de Trabajo")
        viewButton.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/ver/eliminar/equipo", self.driver.current_url)

        viewButton = self.driver.find_element(By.XPATH, "//a[contains(@href, '/ver/equipo/trabajo?id=Equipo Guía Primer Ingreso 2010')]") # Ca,mbiar de acuerdo al profesor que se le asigno coordinador
        viewButton.click()

        self.assertEqual("https://fonmala.nyc.dom.my.id/ver/equipo/trabajo?id=Equipo%20Gu%C3%ADa%20Primer%20Ingreso%202010", self.driver.current_url)
        sleep(3)


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()