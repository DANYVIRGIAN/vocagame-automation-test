from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config

class LoginPage(BasePage):
    
    # --- LOCATORS ---
    USERNAME_INPUT = (By.XPATH, "//input[@name='identifier']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_TOAST = (By.XPATH, "//li[@role='status']/div[2]")

    # --- ACTIONS ---
    def open(self):
        self.open_url(config.LOGIN_URL)

    def login_user(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.click(self.LOGIN_BUTTON)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        if self.is_element_present(self.ERROR_TOAST):
            return self.get_text(self.ERROR_TOAST)
        return None