import pytest
from pages.register_page import RegisterPage
from utils.data_util import generate_dynamic_email, generate_indonesia_phone
import config

def test_register_flow_success(driver):
    # 1. Inisialisasi Page & Data
    register_page = RegisterPage(driver)
    
    # Generate Data Unik
    email_unik = generate_dynamic_email()
    phone_unik = generate_indonesia_phone()
    password = config.DEFAULT_PASSWORD
    
    print(f"\n[INFO] Testing dengan Email: {email_unik} | Phone: {phone_unik}")

    # 2. Buka Halaman
    register_page.open()

    # 3. Isi Form
    register_page.register_new_user(
        first_name="Dany", 
        last_name="QA", 
        phone=phone_unik, 
        email=email_unik, 
        password=password
    )

    print("[INFO] Menunggu halaman OTP loading...")
    import time
    time.sleep(3)
    
    # Eksekusi ambil & input OTP
    status_otp = register_page.input_otp_verification(email_unik)
    
    assert status_otp == True, "Gagal proses OTP!"
    print("[SUCCESS] OTP Berhasil diinput!")