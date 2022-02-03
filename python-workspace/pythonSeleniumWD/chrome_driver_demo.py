from selenium import webdriver
from selenium.webdriver.common.by import By

class ChromeDriverMac():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(executable_path="/Users/amey/Devs/python-workspace/pythonSeleniumWD/drivers/chromedriver")
        driver.get(baseUrl)
        elementById = driver.find_element(By.ID, "displayed-text")

        if elementById is not None:
            print("We found the element by ID")

        elementByName = driver.find_element(By.NAME, "enter-name")
        if elementByName is not None:
            print("We found the element by name")
cc = ChromeDriverMac()
cc.test()