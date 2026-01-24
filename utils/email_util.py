import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_otp_from_yopmail(driver, email_address):
    print(f"\n[INFO] Fetching OTP from Yopmail for: {email_address}")
    
    main_window = driver.current_window_handle
    
    driver.switch_to.new_window('tab')
    driver.get("https://yopmail.com/")
    
    try:
        driver.find_element(By.ID, "login").send_keys(email_address)
        driver.find_element(By.ID, "refreshbut").click()
        
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "ifmail"))
        )
        
        body_text = driver.find_element(By.TAG_NAME, "body").text
        match = re.search(r'\b\d{6}\b', body_text)
        
        if match:
            otp = match.group(0)
            print(f"[INFO] OTP Found: {otp}")
            return otp
        else:
            print("[ERROR] OTP not found in email body!")
            return None

    except Exception as e:
        print(f"[ERROR] Yopmail Error: {e}")
        return None
        
    finally:
        driver.close()
        driver.switch_to.window(main_window)