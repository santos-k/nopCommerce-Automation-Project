import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_002_DDT_Login:
    base_URL = ReadConfig.getApplicationURl()
    path = ".//TestData/nopCommerce_testdata.xlsx"
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.driver = setup
        self.logger.info(f"Test running in {self.driver.capabilities['browserName']} browser")
        self.logger.info("Test_002_DDT_Login")
        self.logger.info("Verifying Deta Driven Login Test")
        self.driver.get(self.base_URL)
        self.loginPage = LoginPage(self.driver)
        self.rows = ExcelUtils.get_row_count(self.path, 'Sheet1')

        list_status = []
        for row in range(2, self.rows + 1):
            self.username, self.password, self.exp_result = (
                ExcelUtils.read_data(self.path, 'Sheet1', row, i) for i in range(1, 4)
            )
            self.loginPage.setUserName(self.username)
            self.loginPage.setPassword(self.password)
            self.loginPage.clickLogin()
            actual_title, expected_title = self.driver.title, "Dashboard / nopCommerce administration"
            # time.sleep(5) # time sleep required for firefox browser only

            if actual_title == expected_title:
                if self.exp_result == "Pass":
                    self.logger.info("Test Case Passed")
                    self.try_logout()
                    list_status.append("Pass")
                elif self.exp_result == "Fail":
                    self.logger.error("Test Case Failed")
                    self.driver.save_screenshot(f".\\Screenshots\\test_login_DDT_aEe_Fail.png")
                    self.try_logout()
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if self.exp_result == 'Pass':
                    self.logger.error("Test Case Failed")
                    self.driver.save_screenshot(f".\\Screenshots\\test_login_DDT_aNEe_Pass.png")
                    self.try_logout()
                    list_status.append("Fail")
                elif self.exp_result == 'Fail':
                    self.logger.info("Test Case Passed")
                    self.try_logout()
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("Login Data Driven Test Passed")
            assert True
        else:
            self.logger.error("Login Data Driven Test Failed")
            assert False

        self.logger.info("End of Login Data Driven Testing")
        self.logger.info("Completed Test_002_DDT_Login")

    def try_logout(self):
        try:
            self.loginPage.clickLogout()
        except Exception as e:
            pass
