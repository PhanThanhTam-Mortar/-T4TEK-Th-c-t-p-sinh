# Lấy mã số và nội dung
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
###========================================================================================###
def get_posting_date(driver, div_xpath):
    try:
        # Xác định XPath cho ngày đăng trong <div> cụ thể
        ngay_dang_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 62px')]"))
        )
        
        # Trả về ngày đăng sau khi cắt bỏ khoảng trắng thừa
        return ngay_dang_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy ngày đăng. Lỗi: {e}")
        return None

def get_address(driver, div_xpath):
    try:
        # Xác định XPath cho địa chỉ trong <div> cụ thể
        dia_chi_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //span[@class='truncate font-bold']"))
        )
        
        # Trả về địa chỉ sau khi cắt bỏ khoảng trắng thừa 
        return dia_chi_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy địa chỉ. Lỗi: {e}")
        return None

def get_street(driver, div_xpath):
    try:
        # Xác định XPath cho phố trong <div> cụ thể
        pho_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 80px')]//span[@class='font-semibold']"))
        )

        # Trả về phố sau khi cắt bỏ khoảng trắng thừa
        return pho_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Phố. Lỗi: {e}")
        return None

def get_district(driver, div_xpath):
    try:
        # Xác định XPath cho quận trong <div> cụ thể
        quan_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 70px')]"))
        )

        # Trả về quận sau khi cắt bỏ khoảng trắng thừa
        return quan_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Quận. Lỗi: {e}")
        return None

def get_parameter(driver, div_xpath):
    try:
        # Xác định XPath cho thông số trong <div> cụ thể
        thong_so_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 80px')]"))
        )

        # Trả về thông số sau khi cắt bỏ khoảng trắng thừa
        return thong_so_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Thông số. Lỗi: {e}")
        return None

def get_price(driver, div_xpath):
    try:
        # Xác định XPath cho giá trong <div> cụ thể
        gia_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 65px')]//span[@class='font-bold']"))
        )

        # Trả về giá sau khi cắt bỏ khoảng trắng thừa
        return gia_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Giá. Lỗi: {e}")
        return None

def get_price_m2(driver, div_xpath):
    try:
        # Xác định XPath cho giá/m² trong <div> cụ thể
        gia_m2_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 78px')]"))
        )

        # Trả về giá/m² sau khi cắt bỏ khoảng trắng thừa
        return gia_m2_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Giá/m². Lỗi: {e}")
        return None

def get_owner_head(driver, div_xpath):
    try:
        # Xác định XPath cho đầu chủ trong <div> cụ thể
        dau_chu_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 120px')]"))
        )

        # Trả về đầu chủ sau khi cắt bỏ khoảng trắng thừa
        return dau_chu_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Đầu chủ. Lỗi: {e}")
        return None

def get_phone_number(driver, div_xpath):
    try:
        # Xác định XPath cho số điện thoại trong <div> cụ thể
        SDT_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 147px')]"))
        )

        # Trả về số điện thoại sau khi cắt bỏ khoảng trắng thừa
        return SDT_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy SĐT. Lỗi: {e}")
        return None

def get_characteristic(driver, div_xpath):
    try:
        # Xác định XPath cho đặc điểm trong <div> cụ thể
        dac_diem_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{div_xpath} //div[contains(@style, 'width: 110px')]"))
        )

        # Trả về đặc điểm sau khi cắt bỏ khoảng trắng thừa
        return dac_diem_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy Đặc điểm. Lỗi: {e}")
        return None
    
###========================================================================================###
def get_code(driver):
    try:
        # Chờ đợi cho đến khi phần tử chứa mã số có thể truy cập được
        ma_so_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='opacity-75 text-[13px] font-semibold whitespace-nowrap hidden md:block']//a"))
        )
        # Trả về mã số sau khi cắt bỏ khoảng trắng thừa
        return ma_so_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy mã số. Lỗi: {e}")
        return None
    
def get_new_time_updated(driver):
    try:
        # Chờ đợi cho đến khi phần tử chứa thời gian cập nhật có thể truy cập được
        thoi_gian_cap_nhat_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='flex items-center text-xs space-x-1.5']//span"))
        )
        # Trả về thời gian cập nhật sau khi cắt bỏ khoảng trắng thừa
        return thoi_gian_cap_nhat_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy mã số. Lỗi: {e}")
        return None
    
def get_title(driver):
    try:
        # Chờ đợi phần tử có class 'font-medium' và style 'white-space: pre-line' xuất hiện
        tieu_de_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'font-medium') and contains(@style, 'white-space: pre-line')]"))
        )
        # Trả về tiêu đề đã được cắt bỏ khoảng trắng thừa
        return tieu_de_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy tiêu đề. Lỗi: {e}")
        return None

def get_content(driver):
    try:
        # Chờ đợi phần tử có class 'font-medium' và style 'white-space: pre-line' xuất hiện
        noi_dung_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'overflow-y-auto') and contains(@style, 'line-height: 20px')]"))
        )
        # Trả về nội dung đã được cắt bỏ khoảng trắng thừa
        return noi_dung_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy nội dung. Lỗi: {e}")
        return None
    
###========================================================================================###


# Hàm lưu hình ảnh từ URL
def save_image_from_url(img_url, folder, img_filename):
    try:
        # Tải hình ảnh từ URL
        img_data = requests.get(img_url).content
        img_path = os.path.join(folder, img_filename + ".jpeg")

        # Lưu hình ảnh
        with open(img_path, 'wb') as f:
            f.write(img_data)

        print(f"Hình ảnh đã được lưu thành {img_path}")
        return img_path
    except Exception as e:
        print(f"Lỗi khi lưu hình ảnh từ URL {img_url}: {e}")
        return None

# Hàm lấy tất cả hình ảnh
def get_images(driver, ma_so, image):
    try:
        # Tạo thư mục lưu hình ảnh cho bất động sản nếu chưa có
        image_folder = os.path.join(image, ma_so)
        os.makedirs(image_folder, exist_ok=True)

        # Tìm tất cả các phần tử hình ảnh
        image_elements = driver.find_elements(By.CSS_SELECTOR, "div.swiper-slide a[data-fancybox]")
        image_urls = [anchor.get_attribute('href') for anchor in image_elements]

        image_paths = []  # Danh sách lưu đường dẫn hình ảnh

        # Lấy URL tất cả hình ảnh và lưu vào thư mục
        for i, img_url in enumerate(image_urls):
            try:
                if img_url.startswith("http"):
                    img_filename = f"image_{ma_so}_{i + 1}"
                    img_path = save_image_from_url(img_url, image_folder, img_filename)
                    if img_path:
                        image_paths.append(img_path)  # Thêm đường dẫn hình ảnh vào danh sách

            except Exception as e:
                print(f"Lỗi khi tải hình ảnh {i + 1}: {e}")

        print(f"Số lượng hình ảnh đã cào: {len(image_paths)}")
        return image_paths
    except Exception as e:
        print(f"Lỗi khi cào hình ảnh: {e}")
        return []
