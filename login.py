# coding=utf-8
# Import necessary libraries
import os
# Set the path to the Chrome webdriver
os.environ["CHROME_DRIVER"] = "/path/to/chromedriver"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
# Use the Chrome webdriver to control the browser
driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER", None), chrome_options=chrome_options)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print('库导入完毕')

# Get Chrome binary path
chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', None)

# Initialize the webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_bin
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER", None), chrome_options=chrome_options)

# Navigate to the login page
driver.get("https://www.imslr.com")
print('打开www.imslr.com')

# Wait for the login button to appear
login_box = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='nv_forum']"))
)
print('网页加载完毕')

# Click the login button
login_box.click()
print('点击登录按钮')

# Wait for the login form to appear
login_form = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'loginform')]"))
)
print('登录框加载完毕')

# Input the username
username = driver.find_element_by_xpath("//*[contains(@id, 'username')]")
username.send_keys("零星")
print('账号输入完毕')

# Input the password
password = driver.find_element_by_xpath("//*[contains(@id,'password')]")
password.send_keys("Xingxue1234")
print('密码输入完毕')

# Click the login button
login_button = driver.find_element_by_xpath("//*[contains(@id, 'loginform')]")
login_button.click()
print('点击另一个登录按钮')

# Wait for the head sculpture to appear
login_form = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'avt')]"))
)
# Click the login button
login_button = driver.find_element_by_xpath("//*[contains(@id, 'loginform')]")
print('点击另一个登录按钮')

# Wait for the head sculpture to appear
login_form = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'avt')]"))
)
print('头像加载完毕')
