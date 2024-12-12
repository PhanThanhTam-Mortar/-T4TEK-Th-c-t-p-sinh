import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .details import get_code, get_title, get_content, get_address,get_new_time_updated, get_characteristic, get_price, get_district, get_owner_head, get_parameter, get_phone_number, get_posting_date, get_price_m2, get_street
###========================================================================================###
# Hàm tìm 10 <div>
def scroll_and_load(driver, target_count=10, scroll_distance=300):
    try:
        # Lặp cho đến khi tải đủ 10 <div>
        while True:
            divs = driver.find_elements(By.XPATH, "//div[contains(@data-index, '')]")
            if len(divs) >= target_count:  # Nếu đã có đủ 10 <div>
                print(f"Đã tải đủ {target_count} <div>")
                break
            # Cuộn xuống để tải thêm
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            time.sleep(random.uniform(2, 4))
    except Exception as e:
        print(f"Lỗi khi cuộn trang: {e}")
        raise

# Hàm xử lý từng <div data-index="...">
def process_div(driver, index):
    try:
        # Tìm <div data-index="index">
        div_xpath = f"//div[@data-index='{index}']"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, div_xpath))
        )
        div_element = driver.find_element(By.XPATH, div_xpath)
        time.sleep(random.uniform(7, 11))

        # Cuộn đến <div> cần xử lý
        driver.execute_script("arguments[0].scrollIntoView(true);", div_element)
        time.sleep(random.uniform(5, 10))

        # Chờ đợi và lấy địa chỉ từ <div> cụ thể
        dia_chi = get_address(driver, div_xpath)  # Lấy địa chỉ từ phần tử <div> tương ứng
        print(f"[Index {index}] Địa chỉ: {dia_chi if dia_chi else 'Không có địa chỉ'}")

        pho = get_street(driver, div_xpath)
        print(f"[Index {index}] Phố: {pho if pho else 'Không có phố'}")

        quan = get_district(driver, div_xpath)
        print(f"[Index {index}] Quận: {quan if quan else 'Không có quận'}")

        thong_so = get_parameter(driver, div_xpath)
        print(f"[Index {index}] Thông số: {thong_so if thong_so else 'Không có thông số'}")

        gia = get_price(driver, div_xpath)
        print(f"[Index {index}] Giá: {gia if gia else 'Không có giá'}")

        gia_m2 = get_price_m2(driver, div_xpath)
        print(f"[Index {index}] Giá trên mét vuông: {gia_m2 if gia_m2 else 'Không có giá trên mét vuông'}")

        dau_chu = get_owner_head(driver, div_xpath)
        print(f"[Index {index}] Đầu chủ: {dau_chu if dau_chu else 'Không có đầu chủ'}")

        sdt = get_phone_number(driver, div_xpath)
        print(f"[Index {index}] SĐT: {sdt if sdt else 'Không có SĐT'}")

        dac_diem = get_characteristic(driver, div_xpath)
        print(f"[Index {index}] Đặc điểm: {dac_diem if dac_diem else 'Không có đặc điểm'}")
        time.sleep(random.uniform(5, 10))

        # Tìm nút trong <div> cụ thể với data-index
        button = driver.find_elements(
            By.XPATH,
            f"{div_xpath}//button[contains(@class, 'ant-btn') and contains(@class, 'css-h2e6id') and contains(@class, 'ant-btn-link') and contains(@class, 'ant-btn-icon-only') and contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'justify-center')]"
        )
        
        # Kiểm tra nếu nút tồn tại và click
        if button:
            driver.execute_script("arguments[0].click();", button[0])
            print(f"Đã click vào nút trong <div data-index='{index}'>.")
        else:
            print(f"Không tìm thấy nút trong <div data-index='{index}'>.")

        # Thêm thời gian chờ ngẫu nhiên
        time.sleep(random.uniform(10, 15))

        # Lấy thông tin sau khi click
        ma_so = get_code(driver)
        print(f"[Index {index}] Mã số: {ma_so if ma_so else 'Không có mã số'}")

        thoi_gian_cap_nhat = get_new_time_updated(driver)
        print(f"[Index {index}] Thời gian cập nhật: {thoi_gian_cap_nhat if thoi_gian_cap_nhat else 'Không có thời gian cập nhật'}")        

        tieu_de = get_title(driver)
        print(f"[Index {index}] Tiêu đề: {tieu_de if tieu_de else 'Không có tiêu đề'}")

        noi_dung = get_content(driver)
        print(f"[Index {index}] Nội dung: {noi_dung if noi_dung else 'Không có nội dung'}")

        # Quay lại trang trước
        driver.back()
        time.sleep(random.uniform(15, 20))

    except Exception as e:
        print(f"Lỗi khi xử lý <div data-index='{index}'>: {e}")

