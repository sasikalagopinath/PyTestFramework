import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readConfigData import ReadConfig
from utilities import customLogger
from utilities import excelUtils

class Test_001_Login:
    baseURL = ReadConfig.getCommonData("commonData", "baseURL")
    username = ReadConfig.getCommonData("commonData", "username")
    password = ReadConfig.getCommonData("commonData", "password")
    logger=customLogger.get_logger("Login")
    path = ".\\TestData\\loginData.xlsx"

    @pytest.mark.sanity
    def test_verifying_home_title(self, setup):
        #create a driver
        self.driver = setup
        self.logger.info("************* Test_001 verifying home title**********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        self.logger.info("************* Getting Title =" +actual_title )
       # if actual_title == "Welcome: Mercury Tours":
        if actual_title == ReadConfig.getCommonData("message", "home_title"):
            self.driver.save_screenshot(".\\screenshots\\home_title.png")
            assert True
            self.logger.info("HomePageTitle Test Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\home_title_failed.png")
            assert False
        self.logger.error("HomePageTitle Test Failed")

        self.driver.close()
        self.logger.info("******* Ending Home Page Title Test **********")

    @pytest.mark.smoke
    def test_login(self, setup):
        self.driver = setup
        self.logger.info("************* Test_002 verifying home title**********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.logger.info("************* Providing Username**********")
        self.lp.setUsername(self.username)
        self.logger.info("************* Providing Password**********")
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.logger.info("************* Getting Title =" + actual_title)
      #  if actual_title=="Login: Mercury Tours":
        if actual_title == ReadConfig.getCommonData("message", "login_title"):
            self.driver.save_screenshot(".\\screenshots\\login_title.png")
            assert True
            self.logger.info("Login Test Passed")

        else:
            self.driver.save_screenshot(".\\screenshots\\login_title_failed.png")
            assert False
        self.logger.error("LoginPageTitle Test Failed")

        self.driver.close()
        self.logger.info("******* Ending Login Page Title Test **********")

    @pytest.mark.regression
    def test_excelLogin_Page_Validation(self, setup):
        
        rows_count = excelUtils.getRowCount(self.path, "Sheet1")
        list_status = []
        for r in range(2, rows_count+1):
            username = excelUtils.readData(self.path, "Sheet1", r, 1)
            password = excelUtils.readData(self.path, "Sheet1", r, 2)
            result = excelUtils.readData(self.path, "Sheet1", r, 3)
            
            self.logger.info("************* Test_003 verifying Login title**********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.lp = LoginPage(self.driver)
            time.sleep(2)
            self.logger.info("************* Providing Username**********")
            self.lp.setUsername(username)
            self.logger.info("************* Providing Password**********")
            self.lp.setPassword(password)
            self.lp.clickLogin()
            actual_title = self.driver.title
            self.logger.info("************* Getting Title =" + actual_title)
      #  if actual_title=="Login: Mercury Tours":
            if actual_title == ReadConfig.getCommonData("message", "login_title"):
                if result == "Pass":
                    self.logger.info("Login Test Passed")
                    self.driver.save_screenshot(".\\screenshots\\login_title.png")
                    list_status.append("Pass")
                elif result == "Fail":
                    self.logger.info("Login Test Failed")
                    self.driver.save_screenshot(".\\screenshots\\login_title_Failed.png")
                    list_status.append("Fail")
            elif actual_title != ReadConfig.getCommonData("message", "login_title"):
                if result == "Pass":
                    self.logger.error("Login Test Passed")
                    self.driver.save_screenshot(".\\screenshots\\login_title.png")
                    list_status.append("Fail")
                elif result == "Fail":
                    self.logger.info("Login Test Failed")
                    self.driver.save_screenshot(".\\screenshots\\login_title_Failed.png")
                    list_status.append("Pass")

            if "Fail" not in list_status:
                self.logger.info("Login is success")
                assert True
            else:
                self.logger.info("Login is Failed")
                assert False












