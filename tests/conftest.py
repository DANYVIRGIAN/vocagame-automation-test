import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Setup: Buka Browser Chrome
    print("\n[INFO] Membuka Browser Chrome...")
    options = webdriver.ChromeOptions()
    
    # options.add_argument("--headless") # tanpa GUI 
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    # WebDriver Manager 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Implicit Wait
    driver.implicitly_wait(10)
    
    yield driver 
    
    # Teardown
    print("\n[INFO] Menutup Browser...")
    driver.quit()