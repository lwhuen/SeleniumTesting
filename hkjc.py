from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 設定 WebDriver（以 Chrome 為例）
driver = webdriver.Chrome()  # 需先安裝 chromedriver

# 設定全螢幕
driver.maximize_window()

# 開啟目標網頁
driver.get('https://special.hkjc.com/e-win/zh-HK/betting-info/marksix/types-of-entry/')

# 等待網頁載入（可視情況調整秒數）
time.sleep(3)

# 使用 XPath 取得所有目標元素，存成 list
xpath = '//*[@title="投注資訊"]/parent::*[1]/following-sibling::*[contains(@class,"ant-menu-submenu ant-menu-submenu-inline")]/child::*/child::*[@class="ant-menu-title-content"]'
listMobileElement = driver.find_elements(By.XPATH, xpath)

# 逐一點擊每個元素
for element in listMobileElement:
    # 打開
    element.click()

    time.sleep(1.5) # 點擊後可視情況等待

    # 關閉
    element.click()

    time.sleep(1.5) # 點擊後可視情況等待



# 關閉瀏覽器
driver.quit()