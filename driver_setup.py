# driver_setup.py
from selenium import webdriver

driver = None

def initialize_driver():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

def quit_driver():
    global driver
    if driver:
        driver.quit()
        driver = None
