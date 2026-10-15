import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_login_exito import LoginExitoso

def test_01_login(driver):
    # Navegar a la página de login
    driver.get("https://www.saucedemo.com/")
    
    # Ingresar credenciales válidas
    login = LoginExitoso(driver)
    login.hacer_login("standard_user", "secret_sauce")
    
    # Espera explícita a que cargue la lista de productos
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_container")))
    
    # A. Verificar la URL /inventory.html
    assert "/inventory.html" in driver.current_url, "ERROR: No se redirigió a /inventory.html"
    
    # B. Verificar el texto "Products" en el encabezado
    header_title = driver.find_element(By.CLASS_NAME, "title").text
    assert header_title == "Products", f"ERROR: Se esperaba 'Products' pero se encontró '{header_title}'"

def test_02_verificar_inventario(driver):
    # Navegar e iniciar sesión
    driver.get("https://www.saucedemo.com/")
    login = LoginExitoso(driver)
    login.hacer_login("standard_user", "secret_sauce")
    
    # Esperar a que el inventario cargue completamente
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_container")))
    
    # A. Validar el título de la pestaña del navegador
    page_title = driver.title
    assert page_title == "Swag Labs", f"ERROR: Se esperaba 'Swag Labs' pero fue '{page_title}'"
    
    # B. Validar el título visual dentro de la página
    section_title = driver.find_element(By.CLASS_NAME, "title").text
    assert section_title == "Products", f"ERROR: Se esperaba 'Products' pero fue '{section_title}'"
    
    # C. Validar Elementos de Interfaz (Menú y Filtro)
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu_button.is_displayed(), "ERROR: El botón del menú no está presente/visible"
    assert filter_dropdown.is_displayed(), "ERROR: El filtro de productos no está presente/visible"
    
    # D. Validar Presencia de Productos
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "ERROR: No se encontraron productos en el catálogo"
    
    # E. Obtener y Mostrar Nombre y Precio del Primer Producto
    primer_producto_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n[INFO] Primer producto encontrado: {primer_producto_nombre} Precio: {primer_producto_precio}")
    assert primer_producto_nombre != "", "ERROR: El nombre del producto está vacío"
    assert primer_producto_precio != "", "ERROR: El precio del producto está vacío"

def test_03_carrito_compras(driver):
    # Navegar e iniciar sesión previamente
    driver.get("https://www.saucedemo.com/")
    login = LoginExitoso(driver)
    login.hacer_login("standard_user", "secret_sauce")
    
    # Esperar a que cargue la tienda
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_container")))
    
    # Añadir el primer producto al carrito
    # A. Buscamos el botón de añadir al carrito del primer producto ("add-to-cart-sauce-labs-backpack")
    primer_boton_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    
    # B. Obtenemos el nombre del producto para verificarlo después
    nombre_producto_esperado = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_boton_agregar.click()
    
    # C. Verificar que el contador del carrito se incremente (debe mostrar "1")
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge_carrito.text == "1", f"ERROR: Se esperaba un ítem en el carrito pero muestra '{badge_carrito.text}'"
    
    # D. Navegar al carrito de compras haciendo clic en el icono del carrito
    icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    icono_carrito.click()
    
    # E. Esperar a que cargue la página del carrito
    wait.until(EC.url_contains("/cart.html"))
    
    # F. Comprobar que el producto añadido aparezca correctamente en el carrito
    nombre_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == nombre_producto_esperado, f"ERROR: El producto en el carrito '{nombre_en_carrito}' no coincide con '{nombre_producto_esperado}'"
   