# Chức năng đăng nhập
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    try:
        login_url = "https://khonhapho.vn/sign-in"
        driver.get(login_url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        WebDriverWait(driver, 20).until(EC.url_changes(login_url))
        print("Đăng nhập thành công.")
    except Exception as e:
        print(f"Lỗi khi đăng nhập: {e}")
        raise
