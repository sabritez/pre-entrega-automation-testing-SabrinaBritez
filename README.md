# Pre-Entrega: Automatización QA con Selenium y Pytest

## 📌 Propósito del proyecto
Este proyecto forma parte de la pre-entrega del curso de Automatización QA. Su objetivo principal es aplicar los conceptos fundamentales de automatización de flujos basicos en la web, utilizando Selenium, WebDriver y Python.

La automatización cubre tres casos de prueba, sobre la aplicación (https://www.saucedemo.com/):
1. Caso 01 (Login): Validación de inicio de sesión exitoso con credenciales válidas y verificación de redirección al inventario.
2. Caso 02 (Inventario): Verificación del título de la página, presencia de productos en el catálogo, validación de elementos de interfaz (menús/filtros) y extracción del nombre y precio del primer producto
3. Caso 03 (Carrito de compras): Interacción con productos, adición del primer artículo al carrito, verificación del incremento en el contador y validación de que el ítem aparezca correctamente dentro de la sección del carrito.

## 🛠️ Tecnologías utilizadas
* Python: como lenguaje principal de programación.
* Selenium WebDriver: para la automatización e interacción con el navegador.
* Pytest: como framework de estructura y ejecución de pruebas.
* WebDriver Manager: para la gestión automática de los drivers de Chrome.

## ⚙️ Cómo instalar las dependencias
Asegúrate de tener Python instalado en tu equipo. Luego, abre la terminal en la raíz del proyecto e instala las librerías necesarias ejecutando el siguiente comando:
pip install pytest selenium webdriver-manager pytest-html

## 🚀 Cómo ejecutar las pruebas
Abre el proyecto en Visual Studio Code y asegúrate de aceptar la confianza del espacio de trabajo ("Yes, I trust the authors" si se solicita).
Abre la terminal integrada presionando `Ctrl + `` (o desde el menú superior en Terminal > Nueva terminal).
Para correr la suite completa de pruebas de manera estándar, ejecuta:
py -m pytest