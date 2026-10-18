import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.ea.com/ea-sports-fc/ultimate-team/web-app/"
PROFILE_DIR = r"C:\selenium_profile"

def start_browser():
    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    driver = webdriver.Chrome(options=options)
    return driver


def click_search(driver):
    wait = WebDriverWait(driver, 10)
    locator = (By.CSS_SELECTOR, "button.btn-standard.primary")
    button = wait.until(EC.element_to_be_clickable(locator))
    button.click()


driver = start_browser()
driver.get(URL)

input("Go to the search screen, then press Enter...")
click_search(driver)



input("Press Enter to close the browser...")