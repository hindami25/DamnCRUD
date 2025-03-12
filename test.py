from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Test Case 1: Login dan Verifikasi Arahkan ke Dashboard
def test_case_1():
    try:
        # Given Navigasi ke URL Login
        driver.get("http://localhost/damncrud/login.php")
        
        # Verifikasi halaman login terlihat
        assert "Login" in driver.title
        
        # Find elements untuk username dan password
        username = driver.find_element(By.ID, "inputUsername")
        password = driver.find_element(By.ID, "inputPassword")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Masukkan kredensial login yang valid
        username.send_keys("admin")  # Ganti dengan username yang valid
        password.send_keys("nimda666!")  # Ganti dengan password yang valid
        
        # Klik tombol login
        login_button.click()
        
        # Tunggu beberapa detik untuk memuat halaman dashboard
        time.sleep(3)
        
        # Verifikasi bahwa setelah login, diarahkan ke halaman dashboard
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source  # Verifikasi apakah nama pengguna muncul
        
        # Verifikasi apakah daftar kontak terlihat
        assert driver.find_element(By.ID, "employee").is_displayed()
        
        print("Test Case 1 Passed ✅: Login dan arahkan ke Dashboard berhasil.")
    except Exception as e:
        print(f"Test Case 1 Failed: {e}")

# Test Case 2: Memeriksa interface link antara Halaman Dashboard dan Halaman Update Contact
def test_case_2():
    try:
        # Given Navigasi ke URL Dashboard
        driver.get("http://localhost/damncrud/index.php")
        
        # Verifikasi halaman Dashboard terlihat
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source  # Pastikan nama pengguna muncul
        
        # Pilih salah satu kontak dan klik tombol "edit"
        edit_button = driver.find_element(By.XPATH, "//a[contains(text(), 'edit')]")
        edit_button.click()
        
        # Tunggu beberapa detik untuk memastikan halaman Update Contact dimuat
        time.sleep(3)
        
        # Verifikasi bahwa halaman Update Contact terbuka
        assert "Change contact" in driver.title
        assert "Update contact" in driver.page_source  # Memastikan halaman update muncul
        
        # Verifikasi bahwa data yang ada di halaman sesuai dengan data yang diambil
        contact_name = driver.find_element(By.NAME, "name").get_attribute("value")
        assert contact_name != ""  # Pastikan nama kontak ada
        
        contact_email = driver.find_element(By.NAME, "email").get_attribute("value")
        assert contact_email != ""  # Pastikan email kontak ada
        
        print("Test Case 2 Passed ✅: Interface link ke halaman Update Contact berhasil.")
    except Exception as e:
        print(f"Test Case 2 Failed: {e}")

# Test Case 4: Memeriksa interface link antara Halaman Dashboard dan Halaman Add New Contact
def test_case_4():
    try:
        # Given Navigasi ke URL Dashboard
        driver.get("http://localhost/damncrud/index.php")
        
        # Verifikasi halaman Dashboard terlihat
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source  # Pastikan nama pengguna muncul
        
        # Klik tombol "Add New Contact" untuk menuju halaman Add New Contact
        add_new_contact_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add New Contact')]")
        add_new_contact_button.click()
        
        # Tunggu beberapa detik untuk memastikan halaman Add New Contact dimuat
        time.sleep(3)
        
        # Verifikasi bahwa halaman Add New Contact terbuka
        assert "Add new contact" in driver.title
        assert "Add new contact" in driver.page_source  # Pastikan halaman Add New Contact terbuka
        
        print("Test Case 4 Passed ✅: Interface link ke halaman Add New Contact berhasil.")
    except Exception as e:
        print(f"Test Case 4 Failed: {e}")

# Test Case 6: Memeriksa interface link antara Halaman Dashboard dan Halaman Profil
def test_case_6():
    try:
        # Given Navigasi ke URL Dashboard
        driver.get("http://localhost/damncrud/index.php")
        
        # Verifikasi halaman Dashboard terlihat
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source  # Pastikan nama pengguna muncul
        
        # Klik tombol "Profil" untuk menuju halaman Profil
        profile_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Profil')]")
        profile_button.click()
        
        # Tunggu beberapa detik untuk memastikan halaman Profil dimuat
        time.sleep(3)
        
        # Verifikasi bahwa halaman Profil terbuka
        assert "Profil" in driver.title
        assert "Username" in driver.page_source  # Pastikan username muncul
        assert "*********" in driver.page_source  # Pastikan password tersembunyi
        
        print("Test Case 6 Passed ✅: Interface link ke halaman Profil berhasil.")
    except Exception as e:
        print(f"Test Case 6 Failed: {e}")

# Test Case 8: Memeriksa interface link antara Halaman Dashboard dan Halaman VPage
def test_case_8():
    try:
        # Given Navigasi ke URL Dashboard
        driver.get("http://localhost/damncrud/index.php")
        
        # Verifikasi halaman Dashboard terlihat
        assert "Dashboard" in driver.title
        assert "Howdy, damn" in driver.page_source  # Pastikan nama pengguna muncul
        
        # Klik tombol "VPage" untuk menuju halaman VPage
        vpage_button = driver.find_element(By.XPATH, "//a[contains(text(), 'VPage')]")
        vpage_button.click()
        
        # Tunggu beberapa detik untuk memastikan halaman VPage dimuat
        time.sleep(3)
        
        # Verifikasi bahwa halaman VPage terbuka
        assert "Dummy Page XSS Detect" in driver.page_source  # Pastikan halaman VPage terbuka
        assert "Type everything" in driver.page_source  # Pastikan form input muncul
        
        print("Test Case 8 Passed ✅: Interface link ke halaman VPage berhasil.")
    except Exception as e:
        print(f"Test Case 8 Failed: {e}")

# Menjalankan Test Cases
test_case_1()
test_case_2()
test_case_4()
test_case_6()
test_case_8()

# Menutup browser setelah pengujian
driver.quit()
