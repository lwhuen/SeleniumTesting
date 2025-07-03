import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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

actuallist = []
productname = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
for name in productname:
    if name.is_displayed():
        actuallist.append(name.text)

expectedlist = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

try:
    assert expectedlist == actuallist, "The expected list match the actual list"
except AssertionError as e:
    print(e)
else:
    print("The expected list match the actual list")

