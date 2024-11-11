import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized


#Pruebas Funcionales Dinámicas:
class PruebasAutenticacion(unittest.TestCase):
    
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")
    
    def test_01_recover(self):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        # Ingresar a la página de login
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/login", self.driver.current_url)

        # Buscoar anchor por link
        recover_button = self.driver.find_element(By.LINK_TEXT, "¿Olvidaste tu contraseña?")
        recover_button.click()

        # Ingresar credenciales
        email = self.driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('admin@admin.com')    

        # Presiona el botón de login
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".form__submit")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/message", self.driver.current_url)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
