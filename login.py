# coding=utf-8
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print('库导入完毕')

# Wait for the login botton to appear
login_box = WebDriverWait(webdriver, 60).until(
    EC.presence_of_element_located(By.XPATH, "//*[@id='nv_forum']")
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
print('点击另一个登录按钮')

# Wait for the head sculpture to appear
login_form = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located(By.XPATH, "//*[contains(@id, 'avt')]")
)
print('头像加载完毕')
