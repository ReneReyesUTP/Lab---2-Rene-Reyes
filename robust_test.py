from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_robust_login():
    driver = webdriver.Chrome()
    try:
        driver.get("https://saucedemo.com")
        
        # Espera explícita de hasta 10 segundos
        wait = WebDriverWait(driver, 10)
        
        # Espera hasta que el campo de usuario sea visible
        user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_input.send_keys("standard_user")
        
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Espera hasta que el botón sea clickeable
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        
        # Espera hasta que la URL cambie
        wait.until(EC.url_contains("inventory.html"))
        print("✅ Login robusto exitoso usando Explicit Waits")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_robust_login()
