from botasaurus.browser import browser, Driver
from src.login import login_to_ygg
from src.search import search_torrents
from src.screenshots import take_screenshots
from src.scraper import extract_torrents_data

@browser(headless=False)
def scrape_heading_task(driver: Driver, data):
    try:
        current_url, page_title = login_to_ygg(driver)
        login_success = "/auth/process_login" not in current_url
        
        if login_success:
            search_url, search_title = search_torrents(driver)
            torrents_data = extract_torrents_data(driver)
            
            return {
                "login_success": True,
                "login_url": current_url,
                "login_title": page_title,
                "search_url": search_url,
                "search_title": search_title,
                "torrents": torrents_data
            }
        else:
            return {
                "login_success": False,
                "login_url": current_url,
                "login_title": page_title
            }
            
    except Exception as e:
        print(e)
        take_screenshots(driver, "error")
        return {"error": str(e)}
     
scrape_heading_task()