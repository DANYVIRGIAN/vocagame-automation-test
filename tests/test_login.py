import pytest
import time
from pages.login_page import LoginPage
import config

def test_login_success(driver):
    """Positive Test Case: Verify user can login with valid credentials."""
    login_page = LoginPage(driver)
    
    valid_username = "horegonuoihgc@gmail.com"
    valid_password = config.DEFAULT_PASSWORD
    
    print(f"\n[INFO] Starting Login Test for User: {valid_username}")

    login_page.open()
    login_page.login_user(valid_username, valid_password)

    print("[INFO] Waiting for login process...")
    time.sleep(3) 
    
    current_url = driver.current_url
    print(f"[INFO] Current URL: {current_url}")

    assert "login" not in current_url, "FAILED: Still on login page!"
    print("[SUCCESS] Login Successful.")