from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from CommonActions.CommonActions import *


driver = webdriver.Safari()
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
driver.maximize_window()

emailAddress = driver.find_element("name", "email_create")
emailAddress.click()
emailAddress.send_keys("amusatam@gmail.com")

createAccountButton = driver.find_element("xpath", "//span[normalize-space()='Create an account']")
createAccountButton.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h3[normalize-space()="Your personal information"]')))

mrMrsButton = driver.find_element("xpath", "//input[@id='id_gender1']")
mrMrsButton.click()

firstName = driver.find_element("xpath", "//input[@id='customer_firstname']")
firstName.send_keys("Amey")

lastName = driver.find_element("xpath", "//input[@id='customer_lastname']")
lastName.send_keys("Satam")

passwordField = driver.find_element("xpath", "//input[@id='passwd']")
passwordField.send_keys("A9shilpa")

select = Select(driver.find_element("xpath", "//select[@id='days']"))
select.select_by_value('28')

select = Select(driver.find_element("xpath", "//select[@id='months']"))
select.select_by_value('7')

select = Select(driver.find_element("xpath", "//select[@id='years']"))
select.select_by_value('1992')

addressField = driver.find_element("xpath", "//input[@id='address1']")
addressField.send_keys("1234 Elm Street")

cityField = driver.find_element("xpath", "//input[@id='city']")
cityField.send_keys("Clemson")

select = Select(driver.find_element("xpath", "//select[@id='id_state']"))
select.select_by_value('40')

zipCode = driver.find_element(By.XPATH, "// input[ @ id = 'postcode']")
zipCode.send_keys("29631")

phoneNumberField = driver.find_element("xpath", "//input[@id='phone_mobile']")
phoneNumberField.send_keys("675-123-9876")

# element = driver.find_element(By.XPATH,"//input[@id='address1']")
#
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()

registerButton = driver.find_element(By.XPATH, "//span[normalize-space()='Register']")
registerButton.click()

homePage = driver.find_element(By.XPATH,"// img[ @ alt = 'My Store']")
homePage.click()