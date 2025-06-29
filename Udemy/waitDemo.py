import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")  # In CSS, the dot (.) indicates a class selector
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()  # Clicking the add to cart button for each product
    time.sleep(2)  # Adding a sleep to ensure the product is added to the cart

# Create a WebDriverWait instance
wait = WebDriverWait(driver, 10)

# Wait for the cart icon to be clickable
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-icon"))).click()  # Clicking the cart icon
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))).click()  # Proceeding to checkout

# Wait for the promo code input to be present
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode"))).send_keys("rahulshettyacademy")  # Entering promo code

# Wait for the promo button to be clickable
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".promoBtn"))).click()  # Clicking the promo button

# Wait for the promo info to be visible and print it
promo_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(promo_info.text)  # Printing the promo info