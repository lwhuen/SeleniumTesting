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

# Wait for any loading overlay to disappear
wait.until(EC.invisibility_of_element_located((By.TAG_NAME, "e2-loading-overlay")))

# Then wait for submit button to be clickable
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
submit_btn.click()

# Wait for specific URL
wait = WebDriverWait(driver, 30)
expected_url = "https://pnshk.cmb8j9fjhz-apj2aswat1-s1-public.model-t.cc.commerce.ondemand.com/zh-hk/foodBeverages"
try:
    wait.until(EC.url_to_be(expected_url))
    print("Login successful and redirected to homepage!")
except:
    print(f"Timeout waiting for expected URL")
    print(f"Expected URL: {expected_url}")
    print(f"Actual URL: {driver.current_url}")
    if "login" in driver.current_url:
        print("Still on login page - login failed")