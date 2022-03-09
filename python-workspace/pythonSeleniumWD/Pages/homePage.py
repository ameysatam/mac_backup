from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from CommonActions.CommonActions import *

driver = webdriver.Safari()
driver.get("http://automationpractice.com")
driver.maximize_window()

signIn = driver.find_element(By.XPATH, "//a[@title='Log in to your customer account']")
signIn.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))

signInUN = driver.find_element(By.XPATH, "//input[@id='email']")
signInUN.send_keys("amusatam@gmail.com")

signInPass = driver.find_element(By.XPATH, "//input[@id='passwd']")
signInPass.send_keys("A9shilpa")

signInButton = driver.find_element(By.XPATH, "//span[normalize-space()='Sign in']")
signInButton.click()

time.sleep(2)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='My Store']")))
# print("successfully located")

homePage = driver.find_element(By.XPATH, "//img[@alt='My Store']")
homePage.click()
# print("successfully clicked")
time.sleep(2)

homePageSearch = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search_query_top']")))
# print("successfully located")

homePageSearch.send_keys("dress")

homePageSearchButt = driver.find_element(By.XPATH, "//button[@name='submit_search']")
homePageSearchButt.click()

list_of_dresses = driver.find_elements(By.XPATH, 'ajax_block_product')

print((list_of_dresses))
time.sleep(10)


driver.quit()