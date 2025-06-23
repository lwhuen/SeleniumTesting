import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.popmart.com/hk/products/1413/THE-MONSTERS-%E5%89%8D%E6%96%B9%E9%AB%98%E8%83%BD%E7%B3%BB%E5%88%97-%E6%90%AA%E8%86%A0%E6%AF%9B%E7%B5%A8%E6%8E%9B%E4%BB%B6%E7%9B%B2%E7%9B%92")

wait = WebDriverWait(driver, 10)

try:
    try:
        driver.find_element(By.XPATH, "//div[@class='policy_acceptBtn__ZNU71']").click()
    except TimeoutException:
        print("Cookie policy accept button not found or already accepted.")
    except NoSuchElementException:
        print("Cookie policy accept button does not exist.")
    driver.find_element(By.XPATH, "//img[@srcset='/_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=640&q=75 640w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=750&q=75 750w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=828&q=75 828w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=1080&q=75 1080w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=1200&q=75 1200w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=1920&q=75 1920w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=2048&q=75 2048w, /_next/image?url=https%3A%2F%2Fcdn-global-eude.popmart.com%2Fglobal-web%2Fhk-prod%2F20250622233157%2F_next%2Fstatic%2Fmedia%2Fgoogle-icon.82804fca.png&w=3840&q=75 3840w']").click()
    driver.find_element(By.XPATH, "//div[@class='index_loginIcon__KGxWn index_container__IEy9N ']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index_sizeInfoTitle__kpZbS index_activeSizeTitle__QNbgr index_disabledSizeTitle__5viP0']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index_euBtn__7NmZ6 index_red__kx6Ql']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-dangerous index_placeOrderBtn__E2dbt']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index_optionItemActive__SEsVB']"))).click()
    print("All steps completed. Holding the page open.")
    while True:
        time.sleep(60)
except (NoSuchElementException, TimeoutException) as e:
    print("Could not find one of the required buttons. Stopping the program.")