import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://pnshk.cmb8j9fjhz-apj2aswat1-s1-public.model-t.cc.commerce.ondemand.com/zh-hk/foodBeverages")

wait = WebDriverWait(driver, 50)
personal_info_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-person")))
personal_info_button.click()

input_email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
input_email.clear()
input_email.send_keys("iamgroot@yopmail.com")

input_password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
input_password.click()
input_password.clear()
input_password.send_keys("Pass1234")

# Wait for any loading overlay to disappear
wait.until(EC.invisibility_of_element_located((By.TAG_NAME, "e2-loading-overlay")))

# Then wait for submit button to be clickable
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
submit_btn.click()

errormsg = driver.find_elements(By.CLASS_NAME, "form-alert-content")
expected_error = "error"
if errormsg:
    for error in errormsg:
        if error.text == expected_error:
            print("Error message verified successfully.")
            break
else:
    print("Unexpected/No error message found, checking again after wait.")
    time.sleep(1)
    errormsg = driver.find_elements(By.CLASS_NAME, "form-alert-content")
    if errormsg:
        for error in errormsg:
            if error.text == expected_error:
                print("Error message verified successfully.")
                break
    else:
        for i in range(4):
            print("Unexpected/No error message found, checking again after wait.")
            time.sleep(1)
            errormsg = driver.find_elements(By.CLASS_NAME, "form-alert-content")
            if errormsg:
                for error in errormsg:
                    if error.text == expected_error:
                        print("Error message verified successfully.")