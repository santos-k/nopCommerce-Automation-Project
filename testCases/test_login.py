from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    base_URL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    expected_login_page_title = "Your store. Logi"
    expected_admin_page_title = "Dashboard / nopCommerce administratio"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        actual_login_page_title = self.driver.title
        if actual_login_page_title == self.expected_login_page_title:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            assert False

    def test_loginPage(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actual_admin_page_title = self.driver.title
        if actual_admin_page_title == self.expected_admin_page_title:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_loginPage.png")
            assert False
