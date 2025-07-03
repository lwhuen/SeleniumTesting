import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.implicitly_wait(5)    # Implicit wait for elements to be present

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)    #it's necessary, if no, it will return empty list
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")    #returns a list of elements
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))


totalAmount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
DiscounttotalAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

print("Total amount: ", totalAmount)
print("Total amount of discounted price: ", DiscounttotalAmount)

assert totalAmount > DiscounttotalAmount, "The total amount is less than the discounted amount"