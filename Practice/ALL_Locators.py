from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# 1. ID
driver.find_element(By.ID, "username").send_keys("john")

# 2. NAME
driver.find_element(By.NAME, "email").send_keys("john@example.com")

# 3. CLASS NAME
driver.find_element(By.CLASS_NAME, "submit-btn").click()

# 4. TAG NAME
all_paragraphs = driver.find_elements(By.TAG_NAME, "p")

# 5. LINK TEXT
driver.find_element(By.LINK_TEXT, "About Us").click()

# 6. PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "About").click()

# 7. CSS SELECTOR
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("abc123")

# 8. XPATH
driver.find_element(By.XPATH, "//button[@id='login']").click()