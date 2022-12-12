#coding=utf-8
Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Initialize the webdriver
driver = webdriver.Chrome()

#Navigate to the login page
driver.get("https://www.imslr.com")

#Wait for the login button to appear
login_box = WebDriverWait(driver, 60).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='nv_forum']"))
)

#Click the login button
login_box.click()

#Wait for the login form to appear
login_form = WebDriverWait(driver, 60).until(
EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'loginform')]"))
)

#Input the username
username = driver.find_element_by_xpath("//*[contains(@id, 'username')]")
username.send_keys("零星")

#Input the password
password = driver.find_element_by_xpath("//*[contains(@id,'password')]")
password.send_keys("Xingxue1234")

#Click the login button
login_button = driver.find_element_by_xpath("//*[contains(@id, 'loginform')]")
login_button.click()

#Wait for the head sculpture to appear
login_form = WebDriverWait(driver, 60).until(
EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'avt')]"))
)

#程序完成，关闭浏览器
driver.close()
