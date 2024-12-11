import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .details import get_code, get_content

# Hàm tìm nút các nút trên trang
def find_buttons(driver, scroll_attempts=10, scroll_distance=300):
    buttons = []
    try:
        for _ in range(scroll_attempts):
            # Cuộn trang xuống một khoảng để tải thêm nút
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            time.sleep(random.uniform(2, 5))  # Thời gian nghỉ 

            # Tìm tất cả các nút với XPath mới
            buttons = driver.find_elements(
                By.XPATH,
                "//button[contains(@class, 'ant-btn') and contains(@class, 'css-h2e6id') and contains(@class, 'ant-btn-link') and contains(@class, 'ant-btn-icon-only') and contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'justify-center')]"
            )
            
            # Nếu tìm thấy ít nhất 10 nút, dừng việc cuộn
            if len(buttons) >= 10:
                break
        
        # Kiểm tra nếu số lượng nút đủ ít nhất 10
        if len(buttons) < 10:
            print(f"Chỉ tìm thấy {len(buttons)} nút.")
            raise Exception("Không đủ số nút để xử lý.")
        
        print(f"Tìm thấy {len(buttons)} nút.")

    except Exception as e:
        print(f"Lỗi khi tìm các nút: {e}")
        raise
    return buttons


# Hàm xử lý từng nút
def process_button(driver, button, index):
    try:
        # Cuộn đến vị trí của nút
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(random.uniform(2, 4))  # Thời gian nghỉ 

        # Click vào nút
        driver.execute_script("arguments[0].click();", button)
        print(f"Đã click vào nút {index}.")
        time.sleep(random.uniform(10, 15))  # Thời gian đợi trước khi cào

        # Lấy mã số từ trang sau khi click
        ma_so = get_code(driver)
        print(f"Nút {index} - Mã số: {ma_so if ma_so else 'Không có mã số'}")

        # Lấy nội dung từ trang sau khi click
        noi_dung = get_content(driver)
        print(f"Nút {index} - Nội dung: {noi_dung if noi_dung else 'Không có nội dung chính'}")
        time.sleep(random.uniform(12, 16))  # Thời gian đợi sau khi cào

        # # Cào hình ảnh và lưu vào thư mục theo mã số bất động sản
        # image_paths = get_images(driver, ma_so, image)  # Gọi hàm cào hình ảnh
        # print(f"Nút {index} - Số lượng hình ảnh đã cào: {len(image_paths)}")

        # Quay lại trang trước để tiếp tục xử lý nút tiếp theo
        driver.back()
        time.sleep(random.uniform(8, 11))  # Thời gian nghỉ giữa các lần quay lại
    except Exception as e:
        print(f"Lỗi khi xử lý nút {index}: {e}")

