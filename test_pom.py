from selenium import webdriver
from login_page import LoginPage

def test_login_pom():
    driver = webdriver.Chrome()
    try:
        driver.get("https://saucedemo.com")
        
        # Instanciamos el objeto de la página
        login_page = LoginPage(driver)
        
        # Llamamos al método de negocio
        login_page.login("standard_user", "secret_sauce")
        
        assert "inventory.html" in driver.current_url
        print("✅ Prueba con POM completada con éxito.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_pom()
