from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    
    # --- LOCATORS ---
    USER_ID_INPUT = (By.XPATH, "//input[@name='data.user_id']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='identifier']")
    ITEM_5_DIAMONDS = (By.XPATH, "//div[@id='Diamonds']/div[2]/button[1]")
    
    QRIS_HEADER = (By.XPATH, "//button[@data-cy='payment-group-qris']")
    QRIS_SUB_OPTION = (By.XPATH, "//div[@data-cy='payment-item-qris']")
    
    BUY_BUTTON = (By.XPATH, "//button[contains(text(), 'Buy')]")
    
    ORDER_NUMBER_TEXT = (By.XPATH, "//h4[contains(text(), 'Nomor Pesanan')]/following-sibling::div/span") 
    LATEST_ORDER_CARD = (By.XPATH, "(//a[contains(@class, 'shadow-card-box') and contains(@class, 'lg:flex')])[1]")

    # --- ACTIONS ---

    def open_free_fire(self):
        print("[ORDER] Open Free Fire Page...")
        self.open_url(config.FREEFIRE_URL)

    def input_order_data(self, user_id, email):
        print(f"[ORDER] Input User ID: {user_id} | Email: {email}")
        self.input_text(self.USER_ID_INPUT, user_id)
        self.input_text(self.EMAIL_INPUT, email)

    def select_item_5_diamonds(self):
        print("[ORDER] Select Item: 5 Diamonds")
        self.click(self.ITEM_5_DIAMONDS)

    def select_payment_qris(self):
        print("[ORDER] Select Payment: QRIS")
        
        # Find all matching elements to handle responsive design (mobile vs desktop)
        qris_buttons = self.driver.find_elements(*self.QRIS_HEADER)
        
        clicked = False
        for btn in qris_buttons:
            if btn.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", btn)
                clicked = True
                break
        
        if not clicked:
            print("[WARN] No visible QRIS button found.")

        time.sleep(1) 
        
        sub_options = self.driver.find_elements(*self.QRIS_SUB_OPTION)
        for sub in sub_options:
            if sub.is_displayed():
                self.driver.execute_script("arguments[0].click();", sub)
                break

    def click_buy_now(self):
        print("[ORDER] Click Buy Button...")
        
        BUY_LOCATOR = (By.XPATH, "//button[contains(text(), 'Beli') or contains(text(), 'Buy')]")
        buttons = self.driver.find_elements(*BUY_LOCATOR)
        
        is_clicked = False
        for btn in buttons:
            if btn.is_displayed() and btn.size['width'] > 0:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", btn)
                is_clicked = True
                break
        
        if not is_clicked:
            raise Exception("Failed to click Buy button (Element not visible)")

    def get_order_number_from_payment_page(self):
        print("[ORDER] Waiting for Payment Page...")
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.ORDER_NUMBER_TEXT)
            )
            order_id = element.text.strip()
            print(f"[ORDER] Order ID Captured: {order_id}")
            return order_id
        except Exception as e:
            print(f"[ERROR] Failed to get Order ID: {e}")
            return None

    def go_to_history_and_click_latest(self):
        print("[ORDER] Navigate to History Page...")
        self.open_url(config.HISTORY_URL)
        
        print("[ORDER] Click latest order...")
        self.click(self.LATEST_ORDER_CARD)