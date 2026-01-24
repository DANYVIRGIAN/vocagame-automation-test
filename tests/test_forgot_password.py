import pytest
from pages.forgot_password_page import ForgotPasswordPage

def test_forgot_password_success(driver):
    fp_page = ForgotPasswordPage(driver)
    
    # Use an email that is already registered
    registered_email = "nuitrooo@yopmail.com" 
    new_password = "PasswordBaru123!"
    
    fp_page.open()
    fp_page.perform_forgot_password(registered_email, new_password)
    
    msg = fp_page.get_success_message()
    print(f"{msg}")
    assert msg is not None