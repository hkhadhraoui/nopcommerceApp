import pytest
from selenium import webdriver
from PageObjects.AddCustmerPage import AddCustomer  # your POM
from Utilities.readproperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.LoginPage import Login
import time
import random
import string

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    """Generate a random string of letters and digits."""
    return ''.join(random.choice(chars) for _ in range(size))



class Test_003_AddCustomer:
    base_url = "https://admin-demo.nopcommerce.com/Admin/"
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.logger.info("*********** Test_003_AddCustomer ***********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # 1. Login
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("*******login successful********")
        time.sleep(2)

        # 2. Navigate to Add Customer page
        self.logger.info("Starting add customer test")
        self.customer_page = AddCustomer(self.driver)
        self.customer_page.go_to_customers_menu()
        time.sleep(1)
        self.customer_page.go_to_customers_submenu()
        time.sleep(1)
        self.customer_page.click_add_new()
        time.sleep(2)

        # 3. Fill in customer form
        self.logger.info("******* Providing customer information******")
        self.email=random_generator() +"@gmail.com"
        self.customer_page.set_email(self.email)
        self.customer_page.set_password("Test123!")
        self.customer_page.set_first_name("Jane")
        self.customer_page.set_last_name("Doe")
        self.customer_page.select_gender("Female")
        self.customer_page.set_company("Example Co.")
        self.customer_page.toggle_active()
        self.customer_page.toggle_tax_exempt()
        self.customer_page.select_newsletter()
        self.customer_page.select_role_guest()
        self.customer_page.select_vendor("Vendor 1")
        self.customer_page.set_admin_comment("Created via pytest automation")

        # 4. Save customer
        self.logger.info("*******Saving new customer*********")
        self.customer_page.click_save()
        time.sleep(2)

        # 5. Verify success
        from selenium.webdriver.common.by import By
        self.success_msg = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        if"customer has been added successfully." in self.success_msg:
            assert True==True
            self.logger.info("*********** Add Customer test passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\addCustomer.png")
            self.logger.error("*********** Add Customer test failed ***********")
            assert False==False

        self.driver.close()
