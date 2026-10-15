import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='module')
def driver():
    options = Options()
    options.add_argument('--lang=es')
    
    # --- DESACTIVAR COMPLETAMENTE EL GESTOR Y ALERTAS DE CONTRASEÑAS ---
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # <-- Esta línea frena el aviso de "brecha de seguridad"
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # ------------------------------------------------------------------
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()