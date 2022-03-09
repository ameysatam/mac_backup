from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def getDriver(browser):
    if browser.lower() == "safari":
        driver = webdriver.Safari()
        return driver

def launchWebpage(driver,url):
    driver = getDriver("safari")
    if url == "automation":

        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
        driver.maximize_window()