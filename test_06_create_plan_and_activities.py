from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.support.ui import Select
import os

class TestPlan(unittest.TestCase):
    
    def setUp(self):
        # Inicializar el WebDriver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://fonmala.nyc.dom.my.id/")

    def test_06__create_plan(self):
        start = time.time()
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

        name_field.send_keys("Plan de Prueba ", time.strftime("%Y-%m-%d %H:%M:%S"))
        description_field.send_keys("Plan de prueba para testeo")

        #Guardar plan
        submit_button = self.driver.find_element(By.CLASS_NAME, "create-plan__form__submit")
        submit_button.click()
        
        self.assertIn("https://fonmala.nyc.dom.my.id/plans", self.driver.current_url)
        end = time.time()
        print("Tiempo de ejecucion - create_plan: ", end - start)

    def test_06__create_activity(self):
        start = time.time()
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

        #Abrir plan
        view_button = self.driver.find_element(By.CLASS_NAME,  "table__action--edit")
        view_button.click()
        time.sleep(4)
         #Creamos actividad
        add_activity_button = self.driver.find_element(By.CLASS_NAME, "plan__add")
        add_activity_button.click()

        #Introducir datos de la actividad
        name_field = self.driver.find_element(By.NAME, "nombre")
        type_field = self.driver.find_element(By.NAME, "tipoId")
        modality_field = self.driver.find_element(By.NAME, "modalidad")
        realization_field = self.driver.find_element(By.NAME, "fecha")
        publication_field = self.driver.find_element(By.NAME, "fechaPublicacion")
        responsible_field = self.driver.find_element(By.NAME, "responsableId")
        description_field = self.driver.find_element(By.NAME, "descripcion")
        poster_field = self.driver.find_element(By.NAME, "afiche")

        name_field.send_keys("Actividad de Prueba ", time.strftime("%Y-%m-%d %H:%M:%S"))
        select_type = Select(type_field)
        select_type.select_by_index(1)
        modality_select = Select(modality_field)
        modality_select.select_by_index(1)
        # Publication date is tomorrow and realization date is the day after (mm/dd/yyyy)
        tomorrow = time.strftime("%m/%d/%Y", time.localtime(time.time() + 86400))
        after_tomorrow = time.strftime("%m/%d/%Y", time.localtime(time.time() + 172800))
        realization_field.send_keys(after_tomorrow)
        publication_field.send_keys(tomorrow)
        select_responsible = Select(responsible_field)
        select_responsible.select_by_index(1)
        description_field.send_keys("Actividad de prueba para testeo")

        # Subir afiche
        project_root = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(project_root, 'afiche.pdf')
        poster_field.send_keys(file_path)

        #Guardar actividad
        register_button = self.driver.find_element(By.CLASS_NAME, "add-activity__form__submit")
        register_button.click()

        self.assertIn("https://fonmala.nyc.dom.my.id/plan", self.driver.current_url)

        end = time.time()
        print("Tiempo de ejecucion - create_activity: ", end - start)


    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()