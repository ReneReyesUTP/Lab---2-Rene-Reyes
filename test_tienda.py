import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    # Se añade headless para que funcione bien en GitHub Actions (CI/CD)
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    driver.get("https://saucedemo.com")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_login_fallido(driver):
    driver.get("https://saucedemo.com")
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    
    # Esta prueba fallará intencionalmente o mostrará error si no validamos
    # la url de forma correcta, demostrando el reporte.
    assert "inventory.html" not in driver.current_url
