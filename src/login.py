from botasaurus.browser import Driver
import time
from .config import CREDENTIALS, URLS, SELECTORS

def login_to_ygg(driver: Driver):
    driver.get(URLS["login"], bypass_cloudflare=True)
    time.sleep(3)
    
    driver.wait_for_element(SELECTORS["login_form"])
    
    driver.click(SELECTORS["username_field"])
    driver.clear(SELECTORS["username_field"])
    driver.type(SELECTORS["username_field"], CREDENTIALS["username"])
    
    driver.click(SELECTORS["password_field"])
    driver.clear(SELECTORS["password_field"])
    driver.type(SELECTORS["password_field"], CREDENTIALS["password"])
    
    driver.click(SELECTORS["submit_button"])
    time.sleep(5)
    
    return driver.current_url, driver.title
