import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = ""
PROFILE_DIR = r"C:\selenium_profile"

def start_browser():
    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    driver = webdriver.Chrome(options=options)

driver = start_browser()
input("Press Enter to close the browser...")