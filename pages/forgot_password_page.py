from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config
import time
from utils.email_util import get_otp_from_yopmail 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotPasswordPage(BasePage):
    
    # --- LOCATORS ---
    EMAIL_INPUT = (By.XPATH, "//input[@name='identifier']") 
    SUBMIT_REQUEST_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Popup & OTP
    KIRIM_OTP_BUTTON = (By.XPATH, "//*[contains(text(), 'Kirim OTP via Email')]")
    LANJUTKAN_OTP_BUTTON = (By.XPATH, "//div[@role='dialog']//button[3]")
    OTP_INPUT = (By.XPATH, "//div[@data-input-otp-container]//input")
    VERIFIKASI_OTP_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Verifikasi']")

    # Reset Password
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='confirmPassword']")
    RESET_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//li[@role='status']/div[2]")

    # --- ACTIONS ---

    def open(self):
        self.open_url(config.FORGOT_PASSWORD_URL)

    def perform_forgot_password(self, email, new_pass):
        print(f"[PAGE] Request reset for: {email}")
        self.input_text(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_REQUEST_BUTTON)
        time.sleep(1) 

        self.proceed_to_otp_popup()

        otp_success = self.input_otp_verification(email)
        
        if otp_success:
            print("[PAGE] Input New Password...")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.NEW_PASSWORD_INPUT)
            )
            self.input_text(self.NEW_PASSWORD_INPUT, new_pass)
            self.input_text(self.CONFIRM_PASSWORD_INPUT, new_pass)
            self.click(self.RESET_BUTTON)
        else:
            raise Exception("OTP Verification Failed")

    def proceed_to_otp_popup(self):
        print("[INFO] Handling OTP Popup...")
        if self.is_element_present(self.KIRIM_OTP_BUTTON):
            self.click(self.KIRIM_OTP_BUTTON)
        
        if self.is_element_present(self.LANJUTKAN_OTP_BUTTON):
            self.click(self.LANJUTKAN_OTP_BUTTON)
            
    def input_otp_verification(self, email_address):
        print(f"[PROCESS] Retrieving OTP for {email_address}...")
        otp_code = get_otp_from_yopmail(self.driver, email_address)
        
        if otp_code:
            print(f"[INFO] Input OTP: {otp_code}")
            self.input_text(self.OTP_INPUT, otp_code)
            self.click(self.VERIFIKASI_OTP_BUTTON)
            time.sleep(5) 
            return True
        return False

    def get_success_message(self):
        try:
            return self.get_text(self.SUCCESS_TOAST)
        except:
            return None