import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = "iamgroot007@yopmail.com"
password = "Pass1234"

driver = webdriver.Chrome()
driver.get("https://pnshk.cmb8j9fjhz-apj2aswat1-s1-public.model-t.cc.commerce.ondemand.com/zh-hk/foodBeverages")
driver.maximize_window()

wait = WebDriverWait(driver, 20)
personal_info_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-person")))
personal_info_button.click()

# Enter email with verification
input_email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
input_email.clear()
input_email.send_keys(email)

# Wait for loading overlay to disappear before password field
wait.until(EC.invisibility_of_element_located((By.TAG_NAME, "e2-loading-overlay")))

# Enter password with verification
input_password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
input_password.click()
input_password.clear()
input_password.send_keys(password)

# Wait for any loading overlay to disappear
wait.until(EC.invisibility_of_element_located((By.TAG_NAME, "e2-loading-overlay")))

# Wait for submit button to be clickable
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
submit_btn.click()
print("Login button clicked")

# Wait for error message to appear after failed login
time.sleep(3)

# Check for error message
errormsg = driver.find_elements(By.CLASS_NAME, "form-alert-content")
expected_error = "error"

if errormsg:
    for error in errormsg:
        print(f"Error text found: '{error.text}'")
        if error.text == expected_error:
            print("Error message verified successfully.")
        else:
            print(f"Error message text doesn't match. Expected: '{expected_error}', Got: '{error.text}'")
else:
    print("No error message found")
    print(f"Current URL: {driver.current_url}")
    print(f"Page title: {driver.title}")

# Keep browser open for 5 seconds to see the result
time.sleep(5)
driver.quit()