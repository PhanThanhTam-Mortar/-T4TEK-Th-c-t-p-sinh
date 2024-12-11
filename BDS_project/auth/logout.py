# Chức năng đăng xuất
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logout(driver):
    try:
        print("Đang thực hiện đăng xuất...")
        menu_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ant-dropdown-trigger"))
        )
        menu_button.click()

        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@role='menuitem' and .//div[text()='Đăng xuất']]"))
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_changes("/sign-in"))
        print("Đăng xuất thành công.")
    except Exception as e:
        print(f"Lỗi khi đăng xuất: {e}")
