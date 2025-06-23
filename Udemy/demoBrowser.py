import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
time.sleep(3)
# driver.maximize_window()
driver.set_window_size(2560, 1440)
print(driver.title)
print(driver.current_url)
