from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config
import time
from utils.email_util import get_otp_from_yopmail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage(BasePage):
    
    # --- LOCATORS ---
    NAMA_DEPAN_INPUT = (By.XPATH, "//input[@name='first_name']")
    NAME_BELAKANG_INPUT = (By.XPATH, "//input[@name='last_name']")
    NOMOR_TELPON_INPUT = (By.XPATH, "//input[@name='phone_number']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    REINPUT_INPUT = (By.XPATH, "//input[@name='confirm_password']")
    TNC_CHECK = (By.XPATH, "//button[@role='checkbox']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    KIRIM_OTP_BUTTON = (By.XPATH, "//p[text()='Kirim OTP via Email']")
    LANJUTKAN_OTP_BUTTON = (By.XPATH, "//div[@role='dialog']//button[3]")
    VERIFIKASI_OTP_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Verifikasi']")
    OTP_INPUT = (By.XPATH, "//div[@data-input-otp-container]//input")
    DUPLICATED_TOAST = (By.XPATH, "//li[@role='status']/div[2]")

    # --- ACTIONS ---
    def open(self):
        self.open_url(config.REGISTER_URL)

    def register_new_user(self, first_name, last_name, phone, email, password):
        self.input_text(self.NAMA_DEPAN_INPUT, first_name)
        self.input_text(self.NAME_BELAKANG_INPUT, last_name)
        self.input_text(self.NOMOR_TELPON_INPUT, phone)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.REINPUT_INPUT, password)
        
        self.click(self.TNC_CHECK)
        self.click(self.SUBMIT_BUTTON)
        time.sleep(2)
    
    def proceed_to_otp_popup(self):
        print("[INFO] Handling Pop-up OTP...")
        self.click(self.KIRIM_OTP_BUTTON)
        self.click(self.LANJUTKAN_OTP_BUTTON)
        
    def input_otp_verification(self, email_address):
        otp_code = get_otp_from_yopmail(self.driver, email_address)
        
        if otp_code:
            self.input_text(self.OTP_INPUT, otp_code)
            self.click(self.VERIFIKASI_OTP_BUTTON)
            time.sleep(8)
            return True
        return False

    def get_error_message(self):
        try:
            print("[INFO] Waiting for Error Toast...")
            toast_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.DUPLICATED_TOAST)
            )
            error_text = toast_element.text
            print(f"[INFO] Toast found: '{error_text}'")
            return error_text
        except Exception as e:
            print(f"[WARNING] Toast not found: {e}")
            return None
        
    def is_submit_button_enabled(self):
        try:
            button = self.driver.find_element(*self.SUBMIT_BUTTON)
            return button.is_enabled()
        except:
            return False

    def fill_form_data(self, first_name, last_name, phone, email, password):
        self.input_text(self.NAMA_DEPAN_INPUT, first_name)
        self.input_text(self.NAME_BELAKANG_INPUT, last_name)
        self.input_text(self.NOMOR_TELPON_INPUT, phone)
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        self.input_text(self.REINPUT_INPUT, password)
        self.click(self.TNC_CHECK)