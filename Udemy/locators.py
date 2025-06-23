import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# locators: ID, Xpath, CSS Selector, Class Name, Tag Name, Link Text, Partial Link Text
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click() #click the checkbox

# Xpath: //tagname[@attribute='value'] -> //input[@type='submit']
# CSS: tagname[attribute='value'] -> //input[@type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Lee")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)          # Success! The Form has been submitted successfully!.
assert "Success" in message    # verify that the string "Success" appears somewhere within the variable