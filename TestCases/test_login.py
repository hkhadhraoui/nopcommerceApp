import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_login:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***********Test_001_login***********")
        self.logger.info("***********Verifying Home Page Title***********")
        self.driver=setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** home page title test passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homePageTitle.png")
            self.driver.close()
            self.logger.error("***********Home page title test failed***********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***********Verifying login test***********")
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title=self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
             assert True
             self.logger.info("***********login test passed***********")
             self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"testLogin.png")
            self.driver.close()
            self.logger.error("***********login test failed***********")
            assert False



