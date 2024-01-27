import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import GenerateRandomNewCustomerData


class Test_AddNewCustomer:
    base_URL = ReadConfig.getApplicationURl()
    username = ReadConfig.getAdminEmail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddNewCustomer(self, setup):
        self.logger.info("Test_AddNewCustomer Started...")
        self.logger.info("Setup of Test Add New Customer Started...")
        self.driver = setup
        self.logger.info(f"Testing in {self.driver.capabilities['browserName']} browser")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.base_URL)

        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        self.logger.info("Log in successful")
        self.logger.info("Setup completed")
        self.logger.info("Add New Customer Started...")

        self.add_new_customer = AddNewCustomer(self.driver)
        self.add_new_customer.clickOnCustomersMenu()
        self.add_new_customer.clickOnCustomersSubMenu()

        self.add_new_customer.clickOnAddNew()
        self.logger.info("Providing customer details")

        user_data = GenerateRandomNewCustomerData.generate_random_user()
        self.logger.info(f"User Data : {user_data}")
        self.add_new_customer.setEmail(user_data['email'])
        self.add_new_customer.setPassword(user_data['password'])
        self.add_new_customer.setFirstName(user_data['first_name'])
        self.add_new_customer.setLastName(user_data['last_name'])
        self.add_new_customer.setGender(user_data['gender'])
        self.add_new_customer.setDOB(user_data['birth_date'])
        self.add_new_customer.setCompany(user_data['company_name'])
        self.add_new_customer.setTaxExempt(user_data['tax_exempt'])
        self.add_new_customer.setNewsLetter(user_data['newsletter'])
        self.add_new_customer.setCustomerRole(user_data['customer_role'])
        self.add_new_customer.setManagerVendor(user_data['manager_vendor'])
        self.add_new_customer.setActiveAccount(user_data['account_status'])
        self.add_new_customer.setComment(user_data['comment'])
        self.add_new_customer.saveNewCustomer()
        self.logger.info("Saving customer info...")
        try:
            save_msg = self.add_new_customer.getSuccessAlertOnSave()
            user_data['Customer_Created'] = 'Created'
            GenerateRandomNewCustomerData.saveNewCustomerData2CSV(user_data, ".//TestData/NewCustomerData.csv")
        except:
            save_msg = self.add_new_customer.getFailureAlertOnSave()
            user_data['Customer_Created'] = 'Not Created'
            GenerateRandomNewCustomerData.saveNewCustomerData2CSV(user_data, ".//TestData/NewCustomerData.csv")

        if 'The new customer has been added successfully.' in save_msg:
            self.driver.save_screenshot(".//Screenshots/AddNewCustomer_Pass.png")
            self.logger.info(f"Alert On Save: {save_msg}")
            self.logger.info("Test Passed")
            self.logger.info("Test completed")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots/AddNewCustomer_Fail.png")
            self.logger.warning(f"Alert On Save: {save_msg}")
            self.logger.warning("Test Failed")
            self.logger.info("Test completed")
            assert False
