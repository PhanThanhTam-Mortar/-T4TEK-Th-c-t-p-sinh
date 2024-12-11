# Điều hướng đến trang kho hàng
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_warehouse(driver, output_file="warehouse.html"):
    try:
        # URL của trang kho hàng
        warehouse_url = "https://khonhapho.vn/warehouse"
        
        # Điều hướng đến trang
        driver.get(warehouse_url)
        print(f"Đang điều hướng đến {warehouse_url}...")
        
        # Đợi trang tải xong (chờ phần tử body xuất hiện)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Đã điều hướng đến trang warehouse.")

        # # Chờ thêm thời gian để đảm bảo nội dung động được tải đầy đủ
        # time.sleep(10)

        # # Lưu mã HTML của trang
        # html_content = driver.page_source
        # with open(output_file, "w", encoding="utf-8") as file:
        #     file.write(html_content)
        # print(f"Đã lưu mã HTML của trang kho hàng vào tệp: {output_file}")

    except Exception as e:
        print(f"Lỗi khi điều hướng hoặc lưu mã HTML: {e}")
        raise
