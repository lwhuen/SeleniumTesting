import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)  # Create an instance of ActionChains
# action.double_click(driver.find_element(By.ID, "mousehover")).perform()  # Perform double-click action
# action.context_click(driver.find_element(By.ID, "mousehover")).perform()  # Perform right-click action
# action.drag_and_drop(driver.find_element(By.ID, "draggable"), driver.find_element(By.ID, "droppable")).perform()  # Perform drag and drop action
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()  # Move to the element
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  # Right-click on the "Top" link

time.sleep(2)