from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    #Menu Navigation ---
    CUSTOMERS_MENU = (By.XPATH, "//p[contains(text(),'Customers')]/parent::a")
    CUSTOMERS_SUBMENU = (By.XPATH, "//p[text()=' Customers']/parent::a")

    # --- Customers List Page ---
    ADD_NEW_BTN = (By.XPATH, "//a[@class='btn btn-primary']")

    # --- Add Customer Page XPaths ---

    # Text fields
    EMAIL = (By.XPATH, "//input[@id='Email']")
    PASSWORD = (By.XPATH, "//input[@id='Password']")
    FIRST_NAME = (By.XPATH, "//input[@id='FirstName']")
    LAST_NAME = (By.XPATH, "//input[@id='LastName']")
    COMPANY = (By.XPATH, "//input[@id='Company']")
    ADMIN_COMMENT = (By.XPATH, "//textarea[@id='AdminComment']")

    # Radio buttons
    GENDER_MALE = (By.XPATH, "//input[@id='Gender_Male']")
    GENDER_FEMALE = (By.XPATH, "//input[@id='Gender_Female']")

    # Checkboxes
    IS_TAX_EXEMPT = (By.XPATH, "//input[@id='IsTaxExempt']")
    ACTIVE = (By.XPATH, "//input[@id='Active']")

    # Dropdowns
    NEWSLETTER = (By.XPATH, "//span[@class='select2-selection select2-selection--multiple']")
    NEWSLETTER_OPTION = "//li[contains(text(),'{0}')]"

    CUSTOMER_ROLES = (By.XPATH, "//ul[@class='select2-selection__rendered']")
    ROLE_REGISTERED = (By.XPATH, "//li[@title='Registered']/span[@role='presentation']")
    ROLE_GUESTS = (By.XPATH, "//li[@title='Guests']")

    ROLE_ADMINISTRATORS = (By.XPATH, "//li[contains(text(),'Administrators')]")
    ROLE_VENDORS = (By.XPATH, "//li[contains(text(),'Vendors')]")

    VENDOR = (By.XPATH, "//select[@id='VendorId']")

    # Buttons
    SAVE = (By.XPATH, "//button[@name='save']")
    SAVE_CONTINUE = (By.XPATH, "//button[@name='save-continue']")

    def __init__(self, driver):
        self.driver = driver


    # --- Methods for Navigation ---
    def go_to_customers_menu(self):
        self.driver.find_element(*self.CUSTOMERS_MENU).click()

    def go_to_customers_submenu(self):
        self.driver.find_element(*self.CUSTOMERS_SUBMENU).click()

    def click_add_new(self):
        self.driver.find_element(*self.ADD_NEW_BTN).click()

    # --- Methods for Form ---
    def set_email(self, email):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def set_company(self, company):
        self.driver.find_element(*self.COMPANY).clear()
        self.driver.find_element(*self.COMPANY).send_keys(company)

    def set_admin_comment(self, comment):
        self.driver.find_element(*self.ADMIN_COMMENT).clear()
        self.driver.find_element(*self.ADMIN_COMMENT).send_keys(comment)

    def select_gender(self,gender):
        if gender=='Male':
            self.driver.find_element(*self.GENDER_MALE).click()
        elif gender=='Female':
            self.driver.find_element(*self.GENDER_FEMALE).click()
        else:
            self.driver.find_element(*self.GENDER_MALE).click()

    def toggle_tax_exempt(self):
        self.driver.find_element(*self.IS_TAX_EXEMPT).click()

    def toggle_active(self):
        self.driver.find_element(*self.ACTIVE).click()

    def select_newsletter(self):
        wait = WebDriverWait(self.driver, 10)

        # 1. Click the dropdown
        self.driver.find_element(*self.NEWSLETTER).click()

        # 2. Wait until the option is clickable
        option_locator = (By.XPATH, self.NEWSLETTER_OPTION.format("nopCommerce admin demo store"))
        option =wait.until(EC.element_to_be_clickable(option_locator))

        # 3. Click the option
        option.click()
        time.sleep(5)

    def select_role_guest(self):
        def select_role_guest(self):
            # 1. Open the customer roles dropdown
            self.driver.find_element(*self.CUSTOMER_ROLES).click()
            time.sleep(1)

            # 2. Remove "Registered" if it exists
            try:
                registered_remove_icon = self.driver.find_element(*self.ROLE_REGISTERED)
                registered_remove_icon.click()
                time.sleep(1)
            except:
                pass  # If "Registered" is not present, continue

            # 3. Open the dropdown again (just in case)
            self.driver.find_element(*self.CUSTOMER_ROLES).click()
            time.sleep(1)

            # 4. Click "Guests" to select
            self.driver.find_element(*self.ROLE_GUESTS).click()
            time.sleep(1)

    def select_vendor(self, vendor_name):
        Select(self.driver.find_element(*self.VENDOR)).select_by_visible_text(vendor_name)

    def click_save(self):
        self.driver.find_element(*self.SAVE).click()

    def click_save_continue(self):
        self.driver.find_element(*self.SAVE_CONTINUE).click()