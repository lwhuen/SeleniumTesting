import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()      # Selecting the checkbox with value "option2"
        assert checkbox.is_selected()        # Verifying the selection, return AssertionError if False
        time.sleep(2)
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()      # Selecting the third radio button
assert radiobuttons[2].is_selected()        # Verifying the selection, return AssertionError if False
time.sleep(2)

assert driver.find_element(By.ID, "displayed-text").is_displayed()      # Verifying the text box is displayed
driver.find_element(By.ID, "hide-textbox").click()      # Hiding the text box
assert not driver.find_element(By.ID, "displayed-text").is_displayed()      # Verifying the text box is hidden
time.sleep(2)