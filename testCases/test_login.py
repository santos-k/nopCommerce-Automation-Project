from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    base_URL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    expected_login_page_title = "Your store. Login"
    expected_admin_page_title = "Dashboard / nopCommerce administration"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_URL)
        actual_login_page_title = self.driver.title
        self.driver.close()
        if actual_login_page_title == self.expected_login_page_title:
            assert True
        else:
            assert False

    def test_loginPage(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        actual_admin_page_title = self.driver.title
        if actual_admin_page_title == self.expected_admin_page_title:
            assert True
        else:
            assert False
