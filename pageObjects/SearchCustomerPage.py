from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchCustomer:
    hide_search_box_xpath = "//div[@class='row search-row opened']"
    open_search_box_xpath = "//i[@class='far fa-angle-down']"
    searchEmail_textbox_id = "SearchEmail"
    searchFirstName_textbox_id = "SearchFirstName"
    searchLastName_textbox_id = "SearchLastName"
    searchMonthBirth_select_id = "SearchMonthOfBirth"
    searchDayBirth_select_id = "SearchDayOfBirth"
    searchRegistrationDateFrom_input_id = "SearchRegistrationDateFrom"
    searchRegistrationDateTo_input_id = "SearchRegistrationDateTo"
    searchLastActivityFrom_input_id = "SearchLastActivityFrom"
    searchLastActivityTo_input_id = "SearchLastActivityTo"
    searchCompany_input_id = "SearchCompany"
    searchIPAddress_input_id = "SearchIpAddress"
    searchCustomerRole_select_id = "SelectedCustomerRoleIds"
    search_button_id = "search-customers"

    searchResult_Table_Body_xpath = "//*[@id='customers-grid']//tbody"

    no_result_found_message = "no data available in table"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.searchEmail_textbox_id).send_keys(email)

    def setFirstName(self, first_name):
        self.driver.find_element(By.ID, self.searchFirstName_textbox_id).send_keys(first_name)

    def setLastName(self, last_name):
        self.driver.find_element(By.ID, self.searchLastName_textbox_id).send_keys(last_name)

    def setBirthMonth(self, month):
        """
        :param month: int 0 to 12
        :return: None
        """
        birth_month = Select(self.driver.find_element(By.ID, self.searchMonthBirth_select_id))
        birth_month.select_by_value(str(month))

    def setBirthDay(self, day):
        """
        :param day: int 0 to 31
        :return: None
        """
        birth_month = Select(self.driver.find_element(By.ID, self.searchDayBirth_select_id))
        birth_month.select_by_value(str(day))

    def setRegistrationDateFrom(self, date):
        self.driver.find_element(By.ID, self.searchRegistrationDateFrom_input_id).send_keys(date)

    def setRegistrationDateTo(self, date):
        self.driver.find_element(By.ID, self.searchRegistrationDateTo_input_id).send_keys(date)

    def setLastActivityDateFrom(self, date):
        self.driver.find_element(By.ID, self.searchLastActivityFrom_input_id).send_keys(date)

    def setLastActivityDateTo(self, date):
        self.driver.find_element(By.ID, self.searchLastActivityTo_input_id).send_keys(date)

    def setCompany(self, company):
        self.driver.find_element(By.ID, self.searchCompany_input_id).send_keys(company)

    def setIPAddress(self, ipaddress):
        self.driver.find_element(By.ID, self.searchIPAddress_input_id).send_keys(ipaddress)

    def setCustomerRole(self, roles):
        select_element = self.driver.find_element(By.ID, self.searchCustomerRole_select_id)

        # Open the dropdown using JavaScript
        self.driver.execute_script("arguments[0].style.display='block'; arguments[0].click();", select_element)
        select_option = Select(select_element)
        select_option.deselect_all()
        for role in roles:
            select_option.select_by_visible_text(role)

    def deselectCustomerRole(self):
        select_element = self.driver.find_element(By.ID, self.searchCustomerRole_select_id)

        # Open the dropdown using JavaScript
        self.driver.execute_script("arguments[0].style.display='block'; arguments[0].click();", select_element)
        select_option = Select(select_element)
        select_option.deselect_all()

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def getTableData(self):
        table_records = self.driver.find_element(By.XPATH, self.searchResult_Table_Body_xpath)
        return table_records.text.lower()
