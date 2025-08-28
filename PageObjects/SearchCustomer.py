from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchCustomerPage:
    # --- Locators ---
    SEARCH_EMAIL = (By.ID, "SearchEmail")
    SEARCH_FIRST_NAME = (By.ID, "SearchFirstName")
    SEARCH_LAST_NAME = (By.ID, "SearchLastName")
    SEARCH_BUTTON = (By.ID, "search-customers")
    CUSTOMER_TABLE = (By.XPATH, "//table[@id='customers-grid']")
    TABLE_ROWS = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Actions ---
    def set_email(self, email):
        self.driver.find_element(*self.SEARCH_EMAIL).clear()
        self.driver.find_element(*self.SEARCH_EMAIL).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element(*self.SEARCH_FIRST_NAME).clear()
        self.driver.find_element(*self.SEARCH_FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.SEARCH_LAST_NAME).clear()
        self.driver.find_element(*self.SEARCH_LAST_NAME).send_keys(last_name)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(self.CUSTOMER_TABLE))

    # --- Table helpers ---
    def get_no_of_rows(self):
        return len(self.driver.find_elements(*self.TABLE_ROWS))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_no_of_rows() + 1):
            emailid = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]"
            ).text
            if emailid.strip() == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name):
        flag = False
        for r in range(1, self.get_no_of_rows() + 1):
            customer_name = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[3]"
            ).text
            if customer_name.strip() == name:
                flag = True
                break
        return flag
