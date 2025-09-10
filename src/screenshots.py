from botasaurus.browser import Driver

def take_screenshots(driver: Driver, step: str):
    screenshot_path = driver.save_screenshot(f"screenshot_{step}.png")
    return screenshot_path
