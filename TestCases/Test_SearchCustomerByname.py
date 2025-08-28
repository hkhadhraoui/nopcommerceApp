import pytest
import time
from PageObjects.LoginPage import Login
from PageObjects.AddCustmerPage import AddCustomer
from PageObjects.SearchCustomer import SearchCustomerPage
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()   # Logger instance


    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*************** Test_SearchCustomerByName_005 ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # ---- Login ----
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("*************** Login successful ***************")

        # ---- Navigate to Customer Menu ----
        self.logger.info("*************** Starting Search Customer By Name ***************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.go_to_customers_menu()
        self.addcust.go_to_customers_submenu()

        # ---- Search by Name ----
        self.searchcust = SearchCustomerPage(self.driver)
        self.searchcust.set_first_name("Victoria")
        self.searchcust.set_last_name("Terces")
        self.searchcust.click_search()
        time.sleep(3)

        status = self.searchcust.search_customer_by_name("Victoria Terces")
        assert status == True
        self.logger.info("*************** Test_SearchCustomerByName_005 Finished ***************")

        self.driver.close()
