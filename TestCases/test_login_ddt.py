import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtility
import time
class Test_002_DDT_login:
    base_url = ReadConfig.getApplicationUrl()
    path = ".//TestData/sheet1.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_002_DDT_login **********")
        self.logger.info("*********** Verifying login test ***********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)

        self.rows = ExcelUtility.getRowCount(self.path,'sheet1')
        print("number of rows in Excel: ", self.rows)

        lst_status = []  # empty list

        for r in range(2, self.rows + 1):
            self.user = ExcelUtility.readData(self.path,'sheet1',r,1)
            self.password = ExcelUtility.readData(self.path,'sheet1',r,2)
            self.exp = ExcelUtility.readData(self.path,'sheet1',r,3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(3)  # wait for login to complete

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***********Login passed**********")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***********Login failed (expected fail)**********")
                    lst_status.append("Fail")
                self.lp.click_logout()  # logout after successful login
                time.sleep(2)  # wait for logout to complete
            else:
                if self.exp == "Pass":
                    self.logger.info("***********Login failed**********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***********Login failed as expected**********")
                    lst_status.append("Pass")

        # After all iterations, close driver and assert overall result
        self.driver.close()

        if "Fail" in lst_status:
            self.logger.info("***********DDT login test failed**********")
            assert False
        else:
            self.logger.info("***********DDT login test passed**********")
            assert True

        self.logger.info("***********End of login DDT test**********")
