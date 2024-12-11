# Tệp chạy chương trình
from config.browser import configure_driver
from auth.login import login
from auth.logout import logout
from navigation.warehouse import navigate_to_warehouse
from navigation.featured_news import navigate_to_featured_news
from actions.button_handler import find_buttons, process_button

def main():
    driver = configure_driver()
    try:
        # Bước 1: Đăng nhập
        login(driver, "0969619679", "0969619679")

        # Bước 2: Điều hướng đến trang warehouse
        navigate_to_warehouse(driver)

        # Bước 3: Click vào "Tin nổi bật"
        navigate_to_featured_news(driver)

        # # Bước 4: Tìm và xử lý các button
        buttons = find_buttons(driver)
        for index, button in enumerate(buttons[:10], start=1):
            process_button(driver, button, index)
    except Exception as e:
        print(f"Lỗi trong quy trình chính: {e}")
    finally:
        # Đăng xuất và đóng trình duyệt
        logout(driver)
        driver.quit()
        print("Đã đóng trình duyệt.")

if __name__ == "__main__":
    main()




