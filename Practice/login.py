import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://pnshk.cmb8j9fjhz-apj2aswat1-s1-public.model-t.cc.commerce.ondemand.com/zh-hk/foodBeverages")

wait = WebDriverWait(driver, 15)
personal_info_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-person")))
personal_info_button.click()

input_email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
input_email.clear()
input_email.send_keys("iamgroot@yopmail.com")

input_password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
input_password.click()
input_password.clear()
input_password.send_keys("Test1234")

submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
submit_btn.click()

# Wait for specific URL
expected_url = "https://pnshk.cmb8j9fjhz-apj2aswat1-s1-public.model-t.cc.commerce.ondemand.com/zh-hk/foodBeverages"
wait.until(EC.url_to_be(expected_url))
print("Login successful and redirected to homepage!")