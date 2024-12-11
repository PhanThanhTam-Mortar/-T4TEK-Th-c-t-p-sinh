# Lấy mã số và nội dung
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import requests
# import os

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

def get_content(driver):
    try:
        # Chờ đợi phần tử có class 'font-medium' và style 'white-space: pre-line' xuất hiện
        noi_dung_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'font-medium') and contains(@style, 'white-space: pre-line')]"))
        )
        # Trả về nội dung đã được cắt bỏ khoảng trắng thừa
        return noi_dung_element.text.strip()
    except Exception as e:
        print(f"Không thể lấy nội dung. Lỗi: {e}")
        return None
    



# # Hàm lưu hình ảnh từ URL
# def save_image_from_url(img_url, folder, img_filename):
#     try:
#         # Tải hình ảnh từ URL
#         img_data = requests.get(img_url).content
#         img_path = os.path.join(folder, img_filename + ".jpeg")

#         # Lưu hình ảnh
#         with open(img_path, 'wb') as f:
#             f.write(img_data)

#         print(f"Hình ảnh đã được lưu thành {img_path}")
#         return img_path
#     except Exception as e:
#         print(f"Lỗi khi lưu hình ảnh từ URL {img_url}: {e}")
#         return None

# # Hàm lấy tất cả hình ảnh
# def get_images(driver, ma_so, image):
#     try:
#         # Tạo thư mục lưu hình ảnh cho bất động sản nếu chưa có
#         image_folder = os.path.join(image, ma_so)
#         os.makedirs(image_folder, exist_ok=True)

#         # Tìm tất cả các phần tử hình ảnh
#         image_elements = driver.find_elements(By.CSS_SELECTOR, "div.swiper-slide a[data-fancybox]")
#         image_urls = [anchor.get_attribute('href') for anchor in image_elements]

#         image_paths = []  # Danh sách lưu đường dẫn hình ảnh

#         # Lấy URL tất cả hình ảnh và lưu vào thư mục
#         for i, img_url in enumerate(image_urls):
#             try:
#                 if img_url.startswith("http"):
#                     img_filename = f"image_{ma_so}_{i + 1}"
#                     img_path = save_image_from_url(img_url, image_folder, img_filename)
#                     if img_path:
#                         image_paths.append(img_path)  # Thêm đường dẫn hình ảnh vào danh sách

#             except Exception as e:
#                 print(f"Lỗi khi tải hình ảnh {i + 1}: {e}")

#         print(f"Số lượng hình ảnh đã cào: {len(image_paths)}")
#         return image_paths
#     except Exception as e:
#         print(f"Lỗi khi cào hình ảnh: {e}")
#         return []
