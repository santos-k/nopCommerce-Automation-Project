from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_001_Login:
    base_URL = ReadConfig.getApplicationURl()
    username = ReadConfig.getAdminEmail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.logger.info(f"************ Test running in {self.driver.capabilities['browserName']} browser ***************")
        self.logger.info("*********** test_homePageTitle *************")
        self.driver.get(self.base_URL)
        actual_login_page_title = self.driver.title
        if actual_login_page_title == "Your store. Login":
            self.logger.info("*********** Pass *************")
            assert True
        else:
            self.logger.error("*********** Fail *************")
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPageTitle(self, setup):
        self.driver = setup
        self.logger.info(f"************ Test running in {self.driver.capabilities['browserName']} browser ***************")
        self.logger.info("*********** test_homePageTitle *************")
        self.driver.get(self.base_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actual_admin_page_title = self.driver.title
        if actual_admin_page_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********** Pass *****************")
            assert True
        else:
            self.logger.error("************ Fail ****************")
            self.driver.save_screenshot(".\\Screenshots\\test_loginPage.png")
            assert False
