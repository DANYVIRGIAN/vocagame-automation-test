import pytest
from pages.order_page import OrderPage
import config
import time

def test_order_flow_validation(driver):
    order_page = OrderPage(driver)
    
    user_id = "12345678" 
    email = "dany.qa@yopmail.com"

    # --- ORDER CREATION ---
    order_page.open_free_fire()
    order_page.input_order_data(user_id, email)
    order_page.select_item_5_diamonds()
    order_page.select_payment_qris()
    order_page.click_buy_now()
    
    # --- GET TRANSACTION DATA ---
    original_order_id = order_page.get_order_number_from_payment_page()
    assert original_order_id is not None, "Failed to create order! Order ID is empty."
    
    # --- HISTORY VALIDATION ---
    order_page.go_to_history_and_click_latest()
    history_order_id = order_page.get_order_number_from_payment_page()
    
    # --- FINAL ASSERTION ---
    print(f"\n[VALIDATION] Original ID: {original_order_id} vs History ID: {history_order_id}")
    
    assert original_order_id == history_order_id, \
        f"Mismatch! Original: {original_order_id}, History: {history_order_id}"
        
    print("[SUCCESS] Flow Order -> Payment -> History -> Payment Verified!")