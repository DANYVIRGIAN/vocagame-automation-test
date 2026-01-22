import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_otp_from_yopmail(driver, email_address):
    print(f"\n[INFO] OTW ambil OTP di Yopmail untuk: {email_address}")
    
    # 1. Simpan Window Asli (VocaGame)
    main_window = driver.current_window_handle
    
    # 2. Buka Tab Baru ke Yopmail
    driver.switch_to.new_window('tab')
    driver.get("https://yopmail.com/en/")
    
    try:
        # 3. Input Email & Cari
        driver.find_element(By.ID, "login").send_keys(email_address)
        driver.find_element(By.ID, "refreshbut").click()
        
        # 4. Pindah ke Iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "ifmail"))
        )
        
        # 5. Ambil Teks & Cari Angka OTP
        body_text = driver.find_element(By.TAG_NAME, "body").text
        match = re.search(r'\b\d{6}\b', body_text)
        
        if match:
            otp = match.group(0)
            print(f"[INFO] OTP Ditemukan: {otp}")
            return otp
        else:
            print("[ERROR] OTP tidak ketemu di email!")
            return None

    except Exception as e:
        print(f"[ERROR] Masalah di Yopmail: {e}")
        return None
        
    finally:
        # 6. Tutup Tab Yopmail & Balik ke VocaGame
        driver.close()
        driver.switch_to.window(main_window)