import pytest
import time
from pages.register_page import RegisterPage
import config

def test_register_duplicate_data(driver):
    """Negative Test Case: Verify Error Toast on duplicate data"""
    register_page = RegisterPage(driver)
    
    email_duplikat = "user_demo_voca@yopmail.com" 
    phone_duplikat = "081299998888"
    password = config.DEFAULT_PASSWORD

    print("[INFO] Negative Test: Register with duplicate data...")

    register_page.open()
    register_page.register_new_user("User", "Kedua", phone_duplikat, email_duplikat, password)
    
    actual_error = register_page.get_error_message()
    
    assert actual_error is not None, "FAILED: Error Toast did not appear!"
    
    expected_keyword = "User sudah terdaftar. Silahkan coba menggunakan email atau nomor handphone lain"
    assert expected_keyword in actual_error, \
        f"FAILED: Error message mismatch! Expected '{expected_keyword}', got '{actual_error}'"
        
    print(f"[SUCCESS] Test Passed! Valid error: {actual_error}")

def test_submit_button_disabled_when_mandatory_empty(driver):
    """Negative Test: Verify Submit button is disabled when mandatory fields are empty."""
    register_page = RegisterPage(driver)
    
    print("[INFO] Negative Test: Checking submit button state...")

    register_page.open()

    register_page.fill_form_data(
        first_name="Test", 
        last_name="User", 
        phone="081234567890", 
        email="",  # Intentionally empty
        password="Password123!"
    )

    is_active = register_page.is_submit_button_enabled()
    
    print(f"[INFO] Button Status: {'ACTIVE' if is_active else 'DISABLED'}")
    assert is_active == False, "BUG: Submit button is active while Email is empty!"
    
    print("[SUCCESS] Validation Successful.")