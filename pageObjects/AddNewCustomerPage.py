import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddNewCustomer:
    customersMenu_link_xpath = "//ul[contains(@class,'nav nav-pills nav-sidebar flex-column nav-legacy')]/li[4]/a"
    customersSubMenu_link_xpath = "//ul[contains(@class,'nav nav-pills nav-sidebar flex-column nav-legacy')]/li[4]/a/following-sibling::ul/li[1]"
    addNew_button_xpath = "//a[@href='/Admin/Customer/Create']"
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    firstname_textbox_id = "FirstName"
    lastname_textbox_id = "LastName"
    male_radio_btn_id = "Gender_Male"
    female_radio_btn_id = "Gender_Female"
    dob_textbox_id = "DateOfBirth"
    companyName_textbox_id = "Company"
    tax_checkbox_id = "IsTaxExempt"
    newsletter_select_id = "SelectedNewsletterSubscriptionStoreIds"
    customer_roles_select_id = "SelectedCustomerRoleIds"
    manager_vendor_select_id = "VendorId"
    active_account_checkbox_id = "Active"
    comment_textarea_id = "AdminComment"

    save_button_xpath = "//button[@name='save']"
    saveContinue_button_xpath = "//button[@name='save-continue']"
    success_alert_xpath = "//div[@class='alert alert-success alert-dismissable']"
    failure_alert_xpath = "//div[@class='alert alert-danger alert-dismissable']"
    backToCustomerList_link_text = "back to customer list"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.customersMenu_link_xpath).click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element(By.XPATH, self.customersSubMenu_link_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.addNew_button_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.lastname_textbox_id).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.male_radio_btn_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.female_radio_btn_id).click()
        else:
            pass

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.dob_textbox_id).send_keys(dob)

    def setCompany(self, company):
        self.driver.find_element(By.ID, self.companyName_textbox_id).send_keys(company)

    def setTaxExempt(self, value):
        checkbox = self.driver.find_element(By.ID, self.tax_checkbox_id)
        if (checkbox.is_selected() and not value) or (not checkbox.is_selected() and value):
            checkbox.click()

    def setManagerVendor(self, vendor):
        manager_vendor = Select(self.driver.find_element(By.ID, self.manager_vendor_select_id))
        manager_vendor.select_by_value(vendor)

    def setActiveAccount(self, active):
        checkbox_element = self.driver.find_element(By.ID, self.active_account_checkbox_id)
        is_checked = checkbox_element.is_selected()
        if is_checked:
            checkbox_element.click()
        if active and not is_checked:
            checkbox_element.click()

    def setComment(self, comment):
        self.driver.find_element(By.ID, self.comment_textarea_id).send_keys(comment)

    def setNewsLetter(self, options):
        select_element = self.driver.find_element(By.ID, self.newsletter_select_id)

        # Open the dropdown using JavaScript
        self.driver.execute_script("arguments[0].style.display='block'; arguments[0].click();", select_element)
        select_option = Select(select_element)
        select_option.deselect_all()
        for option in options:
            select_option.select_by_visible_text(option)

    def setCustomerRole(self, roles):
        select_element = self.driver.find_element(By.ID, self.customer_roles_select_id)

        # Open the dropdown using JavaScript
        self.driver.execute_script("arguments[0].style.display='block'; arguments[0].click();", select_element)
        select_option = Select(select_element)
        select_option.deselect_all()
        time.sleep(1)
        for role in roles:
            select_option.select_by_visible_text(role)

    def saveNewCustomer(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def saveAndContinueNewCustomer(self):
        self.driver.find_element(By.NAME, self.saveContinue_button_xpath)

    def getSuccessAlertOnSave(self):
        return self.driver.find_element(By.XPATH, self.success_alert_xpath).text

    def getFailureAlertOnSave(self):
        failure_alert = self.driver.find_elements(By.XPATH, self.failure_alert_xpath)
        return [msg.text for msg in failure_alert]

    def getBackToCustomerList(self):
        self.driver.find_element(By.LINK_TEXT, self.backToCustomerList_link_text).click()
