import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    print("\n[INFO] Starting Chrome Browser...")
    options = webdriver.ChromeOptions()
    
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.implicitly_wait(10)
    
    yield driver 
    
    print("\n[INFO] Closing Browser...")
    driver.quit()