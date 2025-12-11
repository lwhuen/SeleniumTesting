import time
from selenium import webdriver
from selenium.webdriver.common.by import By
name = "Lee"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()  # Clicking the alert button
time.sleep(2)  # Wait for the alert to appear
alert = driver.switch_to.alert  # Switching to the alert
alertText = alert.text  # Getting the text of the alert
print(alertText)  # Printing the alert text
assert name in alertText  # Asserting that the alert text contains the name
alert.accept()  # Accepting the alert, another option is alert.dismiss() to cancel the alert
time.sleep(2)