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
    
    @parameterized.expand([
        ("admin@admin.com", "admin", True),  # Credenciales válidas
        ("user@wrongemail.com", "wrongpassword", False),  # Email incorrecto
        ("admin@admin.com", "wrongpassword", False),  # Contraseña incorrecta
        ("", "", False),  # Campos vacíos
        ("admin@admin.com", "", False),  # Contraseña vacía
        ("", "admin", False),  # Email vacío
    ])
    def test_login(self, email_input, password_input, expected_result):
        check_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '✅ I understand, I trust this site.')]")
        check_button.click()
        # Ingresar a la página de login
        login_button = self.driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
        login_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/login", self.driver.current_url)

        # Ingresar credenciales
        email = self.driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys(email_input)

        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys(password_input)

        # Presiona el botón de login
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".form__submit")
        login_button.click()

        if expected_result:
            # Esperamos que la autenticación sea exitosa
            self.assertIn("https://fonmala.nyc.dom.my.id", self.driver.current_url)
        else:
            # Validar que el login haya fallado y permanezcamos en la página de login
            self.assertIn("https://fonmala.nyc.dom.my.id/login", self.driver.current_url)

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
