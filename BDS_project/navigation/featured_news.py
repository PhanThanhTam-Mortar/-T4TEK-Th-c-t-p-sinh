# Tìm và chọn mục 'Tin mới nhất' trong dropdown.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_featured_news(driver):
    try:
        # Chờ phần tử dropdown "Tin nổi bật" có thể click được
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-select-selection-item' and @title='Tin nổi bật']"))           
        )

        # Click vào phần tử "Tin nổi bật"
        driver.find_element(By.XPATH, "//span[@class='ant-select-selection-item' and @title='Tin nổi bật']").click()
        print("Đã mở dropdown")

        # Chờ phần tử "Tin mới nhất" có thể click được
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item ant-select-item-option' and @title='Tin mới nhất']"))
        )

        # Click vào phần tử "Tin mới nhất"
        driver.find_element(By.XPATH, "//div[@class='ant-select-item ant-select-item-option' and @title='Tin mới nhất']").click()
        print("Đã click vào phần tử 'Tin mới nhất'!")

    except Exception as e:
        print(f"Lỗi khi xử lý dropdown: {e}")
        raise
