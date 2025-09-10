from botasaurus.browser import Driver
import time
from .config import SELECTORS, SEARCH_TERM

def search_torrents(driver: Driver):
    driver.type(SELECTORS["search_input"], SEARCH_TERM)
    time.sleep(0.5)
    driver.click(SELECTORS["search_button"])
    time.sleep(3)
    
    return driver.current_url, driver.title
