import pytest
from pages.login_page import LoginPage
from utils.data_util import generate_dynamic_email
import time
import config

def test_login_failed_wrong_password(driver):
    """Negative Case 1: Valid Email + Wrong Password"""
    login_page = LoginPage(driver)
    
    valid_email = "horegonuoihgc@gmail.com"
    wrong_password = "PasswordNgawur123!"
    
    print(f"\n[INFO] Test Negative: Wrong Password ({valid_email})...")
    login_page.open()
    login_page.login_user(valid_email, wrong_password)
    
    error_msg = login_page.get_error_message()
    print(f"[RESULT] Error Message: {error_msg}")
    time.sleep(2)   
    
    assert error_msg is not None
    assert "salah" in error_msg.lower() or "credentials" in error_msg.lower()

def test_login_failed_user_not_found(driver):
    """Negative Case 2: Unregistered Email + Random Password"""
    login_page = LoginPage(driver)
    
    unregistered_email = generate_dynamic_email()
    random_password = "Password123!"
    
    print(f"\n[INFO] Test Negative: User Not Found ({unregistered_email})...")
    login_page.open()
    login_page.login_user(unregistered_email, random_password)
    
    error_msg = login_page.get_error_message()
    print(f"[RESULT] Error Message: {error_msg}")
    time.sleep(2)   
    
    assert error_msg is not None
    assert "tidak ditemukan" in error_msg.lower() or "not found" in error_msg.lower()