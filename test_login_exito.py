from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginExitoso:
    def __init__(self, driver):
        self.driver = driver
        # Se definen los Localizadores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def hacer_login(self, username, password): # Funcion principal
        wait = WebDriverWait(self.driver, 10) # Espera explícita de hasta 10s a que el campo de usuario sea visible
        user_field = wait.until(EC.visibility_of_element_located(self.username_input)) # condición de la espera
        user_field.clear()#Limpia el campo de texto
        user_field.send_keys(username)
        pass_field = self.driver.find_element(*self.password_input)#Busca en la página el campo de contraseña
        pass_field.clear()
        pass_field.send_keys(password)
        self.driver.find_element(*self.login_button).click() #Busca el botón de login y hace clic en él.