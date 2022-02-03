from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class SafariDriverMac():

    def test(self):
        driver = webdriver.Safari()
        driver.get("https://www.wish.com/")
        emailAddress = driver.find_element_by_xpath("//input[@data-testid='login-username']")
        emailAddress.send_keys("leoboy1986@gmail.com")
        password = driver.find_element_by_xpath("//input[@autocomplete='current-password']")
        password.send_keys("Test@Selenium")
        logIn = driver.find_element_by_xpath("//div[@role='button'][normalize-space()='Log In']")
        logIn.click()
        time.sleep(5)

sf = SafariDriverMac()
sf.test()