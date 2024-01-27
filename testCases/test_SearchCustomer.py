import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomer_003:
    base_URL = ReadConfig.getApplicationURl()
    username = ReadConfig.getAdminEmail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()

    @pytest.fixture
    def search_setup(self, setup):
        # Setup Driver and Open Index page
        self.logger.info("Test_SearchCustomer__003")
        self.logger.info("Setup started")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.base_URL)

        # Login
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        # Navigate to Search page
        self.navigate_search_page = AddNewCustomer(self.driver)
        self.navigate_search_page.clickOnCustomersMenu()
        self.navigate_search_page.clickOnCustomersSubMenu()
        self.logger.info("Setup Completed")
        yield self.driver
        self.logger.info("Test Completed.")

    def search_customer_setup(self, search_setup, search_by, search_value, expected_result):
        self.driver = search_setup
        self.search_by = search_by
        self.search_value = search_value
        self.expected_result = expected_result

        self.search_customer = SearchCustomer(self.driver)
        self.logger.info(f"Test Case: Search by {self.search_by}")

        if self.search_by == "Email":
            self.search_customer.setEmail(self.search_value)
        elif self.search_by == "FirstName":
            self.search_customer.setFirstName(self.search_value)
        elif self.search_by == "LastName":
            self.search_customer.setLastName(self.search_value)
        elif self.search_by == "BirthDate":
            self.search_customer.setBirthMonth(self.search_value[0])
            self.search_customer.setBirthDay(self.search_value[1])
        elif self.search_by == "RegistrationDate":
            self.search_customer.setRegistrationDateFrom(self.search_value[0])
            self.search_customer.setRegistrationDateTo(self.search_value[1])
        elif self.search_by == "LastActivityDate":
            self.search_customer.setLastActivityDateFrom(self.search_value[0])
            self.search_customer.setLastActivityDateTo(self.search_value[1])
        elif self.search_by == "Company":
            self.search_customer.setCompany(self.search_value)
        elif self.search_by == "CustomerRole":
            self.search_customer.setCustomerRole(self.search_value)

        self.search_customer.clickSearchButton()
        time.sleep(1)
        self.data = self.search_customer.getTableData()

        if self.expected_result in self.data:
            self.logger.info("Test Case Passed.")
            self.logger.info("Remark: searched data found.")
            self.element = self.driver.find_element(By.XPATH, "//*[@id='customers-grid']")
            self.element.screenshot(f".//Screenshots/SearchCustomer_{self.search_by}_DataFound_PASS.png")
            assert True
        elif self.search_customer.no_result_found_message == self.data or self.search_customer.no_result_found_message in self.data:
            self.logger.info("Test Case Passed.")
            self.logger.info("Remark: data not found and it's expected.")
            self.element = self.driver.find_element(By.XPATH, "//*[@id='customers-grid']")
            self.element.screenshot(f".//Screenshots/SearchCustomer_{self.search_by}_DataNotExists_PASS.png")
            assert True
        else:
            self.logger.error("Test Case Failed.")
            self.logger.error("Something went wrong.")
            self.element = self.driver.find_element(By.XPATH, "//*[@id='customers-grid']")
            self.element.screenshot(f".//Screenshots/SearchCustomer_{self.search_by}_DataFound_Fail.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_by_email(self, search_setup):
        self.search_customer_setup(search_setup, 'Email', 'sakshi12@gmail.com', 'sakshi12@gmail.com')

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_by_firstname(self, search_setup):
        self.search_customer_setup(search_setup, 'FirstName', 'sakshi', 'sakshi')

    @pytest.mark.regression
    def test_search_by_lastname(self, search_setup):
        self.search_customer_setup(search_setup, 'LastName', 'maurya', 'maurya')

    @pytest.mark.regression
    def test_search_by_birthdate(self, search_setup):
        self.search_customer_setup(search_setup, 'BirthDate', [6, 16], 'test1@random.com')

    @pytest.mark.regression
    def test_search_by_registration_date(self, search_setup):
        self.search_customer_setup(search_setup, 'RegistrationDate', ['1/25/2024', '1/27/2024'], 'test1@random.com')

    @pytest.mark.regression
    def test_search_by_activity_date(self, search_setup):
        self.search_customer_setup(search_setup, 'LastActivityDate', ['1/25/2024', '1/27/2024'], 'test1@random.com')

    @pytest.mark.regression
    def test_search_by_company_name(self, search_setup):
        self.search_customer_setup(search_setup, 'Company', "Codestdio", 'test1@random.com')

    @pytest.mark.regression
    def test_search_by_customer_role(self, search_setup):
        self.search_customer_setup(search_setup, 'CustomerRole', ['Registered', 'Administrators'], 'test1@random.com')
