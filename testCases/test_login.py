from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    base_URL = ReadConfig.getApplicationURl()
    username = ReadConfig.getAdminEmail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*********** Test_001_Login *************")
        self.logger.info("*********** test_homePageTitle *************")
        self.driver = setup
        self.driver.get(self.base_URL)
        actual_login_page_title = self.driver.title
        if actual_login_page_title == "Your store. Login":
            self.logger.info("*********** Pass *************")
            assert True
        else:
            self.logger.error("*********** Fail *************")
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            assert False

    def test_loginPageTitle(self, setup):
        self.logger.info("*********** test_loginPageTitle *************")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actual_admin_page_title = self.driver.title
        if actual_admin_page_title == "Dashboard / nopCommerce administratio":
            self.logger.info("*********** Pass *****************")
            assert True
        else:
            self.logger.error("************ Fail ****************")
            self.driver.save_screenshot(".\\Screenshots\\test_loginPage.png")
            assert False
