import pytest
import time
from pages.register_page import RegisterPage
from utils.data_util import generate_dynamic_email, generate_indonesia_phone
import config

def test_register_flow_success(driver):
    register_page = RegisterPage(driver)
    
    email_unik = generate_dynamic_email()
    phone_unik = generate_indonesia_phone()
    password = config.DEFAULT_PASSWORD
    
    print(f"\n[INFO] Testing with Email: {email_unik} | Phone: {phone_unik}")

    register_page.open()

    register_page.register_new_user(
        first_name="Dany", 
        last_name="QA", 
        phone=phone_unik, 
        email=email_unik, 
        password=password
    )

    print("[INFO] Proceeding to OTP Popup...")
    time.sleep(2)
    register_page.proceed_to_otp_popup() 
    
    print("[INFO] Waiting for OTP...")
    status_otp = register_page.input_otp_verification(email_unik)
    
    assert status_otp == True, "OTP Verification Failed!"
    print("[SUCCESS] OTP Input and Verification Successful!")