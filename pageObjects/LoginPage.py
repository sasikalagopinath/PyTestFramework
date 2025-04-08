from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    text_username_name ="userName"
    text_password_name="password"
    button_login_name="submit"



    # initialize the driver - For that we need create constructor
    #  will automatically invoke at the time of object creation
    # driver come from actual test case
    def __init__(self, driver):
        self.driver = driver  # this driver, i will initiate a local driver

    #implement action methods for every locator
    # username come from actual test case
    def setUsername(self, username):
        self.driver.find_element(By.NAME, self.text_username_name).clear()
        self.driver.find_element(By.NAME, self.text_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.text_password_name).clear()
        self.driver.find_element(By.NAME, self.text_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME, self.button_login_name).click()


