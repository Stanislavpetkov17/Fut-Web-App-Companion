import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.ea.com/ea-sports-fc/ultimate-team/web-app/"
PROFILE_DIR = r"C:\selenium_profile"

def start_browser():
    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    driver = webdriver.Chrome(options=options)
    return driver


def click_snipe(driver):
    wait = WebDriverWait(driver, 10)
    locator = (By.CSS_SELECTOR, "button.btn-standard.upgrade")
    button = wait.until(EC.element_to_be_clickable(locator))
    button.click()

def click_back(driver):
    wait = WebDriverWait(driver, 10)
    locator = (By.CSS_SELECTOR, "btn-standard.futgenie-empty-back-btn")
    button = wait.until(EC.element_to_be_clickable(locator))
    button.click()


driver = start_browser()
driver.get(URL)

input("Go to the search screen, enter your filters and then press Enter...")
click_snipe(driver)

wait = WebDriverWait(driver, 5)
try: 
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ut-no-results-view")))
    click_back(driver)
except TimeoutException:
    pass

input("Press Enter to close the browser...")
