import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Fixture untuk WebDriver
@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    server = 'http://localhost:4444'

    driver = webdriver.Remote(command_executor=server, options=options)

    # Cleanup setelah test selesai
    yield driver
    driver.quit()

# Test Case 1: Login dan Verifikasi Arahkan ke Dashboard
def test_case_1(driver):
    try:
        driver.get("http://localhost/damncrud/login.php")
        assert "Login" in driver.title
        
        username = driver.find_element(By.ID, "inputUsername")
        password = driver.find_element(By.ID, "inputPassword")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username.send_keys("admin")
        password.send_keys("nimda666!")
        login_button.click()
        
        time.sleep(3)
        
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source
        assert driver.find_element(By.ID, "employee").is_displayed()
        
        print("Test Case 1 Passed ✅: Login dan arahkan ke Dashboard berhasil.")
    except Exception as e:
        print(f"Test Case 1 Failed: {e}")

# Test Case 2: Memeriksa interface link antara Halaman Dashboard dan Halaman Update Contact
def test_case_2(driver):
    try:
        driver.get("http://localhost/damncrud/index.php")
        
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source
        
        edit_button = driver.find_element(By.XPATH, "//a[contains(text(), 'edit')]")
        edit_button.click()
        
        time.sleep(3)
        
        assert "Change contact" in driver.title
        assert "Update contact" in driver.page_source
        
        contact_name = driver.find_element(By.NAME, "name").get_attribute("value")
        assert contact_name != ""
        
        contact_email = driver.find_element(By.NAME, "email").get_attribute("value")
        assert contact_email != ""
        
        print("Test Case 2 Passed ✅: Interface link ke halaman Update Contact berhasil.")
    except Exception as e:
        print(f"Test Case 2 Failed: {e}")

# Test Case 4: Memeriksa interface link antara Halaman Dashboard dan Halaman Add New Contact
def test_case_4(driver):
    try:
        driver.get("http://localhost/damncrud/index.php")
        
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source
        
        add_new_contact_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add New Contact')]")
        add_new_contact_button.click()
        
        time.sleep(3)
        
        assert "Add new contact" in driver.title
        assert "Add new contact" in driver.page_source
        
        print("Test Case 4 Passed ✅: Interface link ke halaman Add New Contact berhasil.")
    except Exception as e:
        print(f"Test Case 4 Failed: {e}")

# Test Case 6: Memeriksa interface link antara Halaman Dashboard dan Halaman Profil
def test_case_6(driver):
    try:
        driver.get("http://localhost/damncrud/index.php")
        
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source
        
        profile_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Profil')]")
        profile_button.click()
        
        time.sleep(3)
        
        assert "Profil" in driver.title
        assert "Username" in driver.page_source
        assert "*********" in driver.page_source
        
        print("Test Case 6 Passed ✅: Interface link ke halaman Profil berhasil.")
    except Exception as e:
        print(f"Test Case 6 Failed: {e}")

# Test Case 8: Memeriksa interface link antara Halaman Dashboard dan Halaman VPage
def test_case_8(driver):
    try:
        driver.get("http://localhost/damncrud/index.php")
        
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source
        
        vpage_button = driver.find_element(By.XPATH, "//a[contains(text(), 'VPage')]")
        vpage_button.click()
        
        time.sleep(3)
        
        assert "Dummy Page XSS Detect" in driver.page_source
        assert "Type everything" in driver.page_source
        
        print("Test Case 8 Passed ✅: Interface link ke halaman VPage berhasil.")
    except Exception as e:
        print(f"Test Case 8 Failed: {e}")

# Menjalankan semua Test Cases
if __name__ == "__main__":
    pytest.main()
