# nopCommerceAutomation-Project

# Selenium Hybrid Framework for nopCommerce Backend System

## Introduction

This project aims to create a Selenium Hybrid Framework using Python for automating the backend system of the nopCommerce demo website. The framework utilizes key technologies such as Selenium, PyTest, Page Object Module, and HTML Reports to achieve re-usability and maintainability of automation files.

### What is a Framework?

A framework is an organized way of maintaining automation files where all files communicate with each other to perform specific tasks.

### Objectives/Goals

1. Re-usability: Create automation scripts that can be reused across multiple test scenarios.
2. Maintainability: Build a framework that is easy to maintain and update.

### Types of Frameworks

1. Built-in/Pre-defined frameworks: pytest, robot framework, unittest, etc.
2. Customized/User-defined frameworks: Data-Driven framework, keyword-driven framework, hybrid-driven framework.

## Phases

1. **Analyze Application, Technology & Skill Set**

   - Choose test cases based on the nopCommerce demo website.
   - Identify re-test cases, regression cases, and automate able test cases.
   - Note that 100% automation is not possible; certain scenarios like reports, captcha, and security-related cases require manual testing.

2. **Design & Implementation of Framework**

3. **Execution**

4. **Maintenance (Version Control System)**

## eCommerce Application Automation

[nopCommerce Demo Website](https://www.nopcommerce.com/en/demo)

1. **Front-end** - For End Users / Customers: [Front-end Demo](https://demo.nopcommerce.com/)
2. **Back-end** - For Admin: [Admin Demo](https://admin-demo.nopcommerce.com/admin/)

## Let's Start

### Step 1: Create a New Project in PyCharm

- Project Name: `nopCommerceAutomation`

#### Install Required Packages/Plugins

1. Selenium
2. Pytest
3. Pytest-html
4. Pytest-xdist : Run parallel execution use in CLI `-n 4`, `-n auto` or `-n=4`
5. Allure-pytest
6. Openpyxl
7. Pytest-repeat : repeat any test multiple times use in CLI `--count=4`

##### Install Packages from requirements.text file
```bash
pip install -r requirements.txt
```

##### Create requirements.txt if this new project after install manually all packages
```bash
pip freeze > requirements.txt    
```

### Step 2: Create Folder Structure

```
nopCommerceAutomation
├── pageObjects (package)
├── testCases (package)
├── utilities (package)
├── TestData (Folder)
├── Configurations (Folder)
├── Logs (Folder)
├── Screenshots (Folder)
├── Reports (Folder)
├── Screenshots (Folder)
├── Run.bat
```

### Step 3: Automating Login Test Cases

#### 3.1 Create LoginPage Object Class under "pageObjects"

- Create `LoginPage.py` under "pageObjects"

#### 3.2 Create LoginTest under "testCases"

- Create `test_login.py`
- run tests using below command, v for verbose, s for 
```commandline
pytest -v -s
```
The command `pytest -v -s` is used to run Python tests using the pytest framework with some specific options. Let's break down each part of the command:
1. **`pytest`**: This is the command to run tests using the pytest framework.
2. **`-v` (or `--verbose`)**: This option increases the verbosity of the test output. When you include `-v`, pytest will print more details about each test, including the names of each test case and the result of each test.
3. **`-s` (or `--capture=no`)**: This option disables output capturing. By default, pytest captures the output of each test and displays it only if the test fails. When you include `-s`, it disables this capturing, and you will see the output of print statements and any other standard output even if the test passes.
So, when you run `pytest -v -s`, you're essentially telling pytest to run the tests in a more verbose mode, showing detailed information about each test, and also to display the standard output (print statements, etc.) during the test execution.
Here's a breakdown of what each option does:
 - `-v`: Increases test verbosity, showing more details about each test.
   - `-s`: Disables output capturing, allowing you to see the standard output during test execution.

#### 3.3 Create `conftest.py` under "testCases"
`conftest.py` is a special Python file that is recognized by pytest as a configuration file. It is typically used to define fixtures, hooks, and other configurations that are shared across multiple test files within a pytest project.
    
Here are some common uses of `conftest.py`:
1. **Fixtures Definition:**
   - Fixtures are a way to set up preconditions or provide data to tests.
   - `conftest.py` can define fixtures that are shared across multiple test files.
   - Fixtures can be used to initialize resources, set up test data, or perform other setup tasks.

   ```python
   # Example conftest.py
   import pytest
   from selenium import webdriver

   @pytest.fixture
   def browser():
       driver = webdriver.Chrome()
       yield driver
       driver.quit()
   ```

   In this example, the `browser` fixture provides a Selenium WebDriver instance for tests, and it is available to any test file within the same project.

2. **Hooks:**
   - Pytest allows you to define hooks that are executed at different stages of the testing process.
   - Hooks can be defined in `conftest.py` to perform setup or teardown tasks.

   ```python
   # Example conftest.py
   def pytest_runtest_setup(item):
       # Code to execute before each test
       pass

   def pytest_runtest_teardown(item):
       # Code to execute after each test
       pass
   ```

   In this example, the `pytest_runtest_setup` and `pytest_runtest_teardown` hooks are defined in `conftest.py` to run setup and teardown tasks before and after each test.

3. **Plugin Initialization:**
   - `conftest.py` can also be used to initialize and configure pytest plugins.
   - Plugins can be activated or configured within the `conftest.py` file.

   ```python
   # Example conftest.py
   def pytest_configure(config):
       config.addinivalue_line("markers", "smoke: mark tests as smoke tests")
   ```

   In this example, the `pytest_configure` hook is used to add a custom marker to pytest, which can be used to tag tests as smoke tests.

By organizing shared fixtures, hooks, and configurations in `conftest.py`, you can create a centralized location for common testing infrastructure, promoting code reusability and maintainability across your pytest project.
### Step 4: Capture Screenshots on Failures

#### 4.1 Update Login Test with Screenshot under "testCases"
- Implement screenshot capture in case of test failures as below.
```
if actual_admin_page_title == self.expected_admin_page_title:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_loginPage.png")
            assert False
```

### Step 5: Read Common values from ini file
#### 5.1 Add 'config.ini' file in 'Configurations' folder
#### 5.2 Create 'readProperties.py' utility under 'Utilities' package to read common data
#### 5.3 Replace hard coded values in Login test case

### Step 6: Adding logs to Test case
#### 6.1 Add customLogger.py under utilities package.
#### 6.2 Add logs to login test case


### Step 7: Run tests on desired browser/cross browser/parallel
#### 7.1 Update `conftest.py` with required Fixtures which will accept command line argument(browser)
   - Command to run test in desired browser
```commandline
pytest -v -s --browser chrome   # will test in chrome similarly use firefox,edge,safari, chrome is default
or
pytest -v -s test_loginpage.py --browser chrome
```
#### 7.2 Pass browser name as an argument in command line
   ```
   pytest -v -s --browser chrome
   pytest -v -s --browser firefox
   pytest -v -s --browser edge
   pytest -v -s --browser safari
   pytest -v -s
   ```
#### 7.3 Parallel test execution
   - `pytest-xdist` package required for parallel test execution `pip install pytest-xdist`
   - This execution not required any code changes, run using CLI
```commandline
pytest -n NCPU # no of parallel CPU
pytest -n 2 # two parallel execution at same time
pytest -n auto # it will auto deside required CPUs
pytest -v -s -n 2 --browser firefox
```

### 8: Generate HTML Reports
#### 8.1 Update `conftest.py` with pytest hooks
```python

################ Pytest HTML Reports ########################
# It is hook for Adding Environment info to HTML Report
from pytest_metadata.plugin import metadata_key
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Login Page'
        config.stash[metadata_key]['Tester'] = 'Santosh Kumar'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
```
#### 8.2 To generate HTML reports run below command
```commandline
pytest -v -s --html=Reports/report.html .\testCases\test_login.py --browser chrome
```

### Step 9: Automating Data Driven Test Case
#### 9.1 Prepare test data in Excel sheet and place the Excel file in TestData directory.

##### Test Data for Login Data-Driven Testing

| Email                | Password | Expected Result |
|----------------------|----------|-----------------|
| admin@yourstore.com  | admin    | Pass            |
| admin@yourstore.com  | adm123   | Fail            |
| user@yourstore.com   | admin123 | Fail            |
| admin@gmail.com      | admin    | Fail            |
| admin@gmail.com      | admin123 | Fail            |

#### 9.2 Create `ExcelUtils.py` utility class under *utilities* package.
   - to read Excel data
```python
import openpyxl


def get_row_count(file, sheet_name):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return sheet.max_row


def read_data(file, sheet_name, row_num, column_no):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return sheet.cell(row=row_num, column=column_no).value
```
#### 9.3 Create `test_login_ddt.py` under *testCases* directory
- Create test case file for data driven testing 
#### 9.4 Run the test case
```
pytest -v -s -n=2  .\testCases\test_login_ddt.py --html=Reports/test_login_ddt.html --browser chrome
```
or 
```commandline
pytest -v -s  .\testCases\test_login_ddt.py --html=Reports/test_login_ddt.html --browser chrome
```
or 
```
pytest  .\testCases\test_login_ddt.py 
```

### Step 10: Adding New Test Cases
#### 10.1 Add New Customer
1. Create POM `AddCustomerPage.py` inside *pageObjects*<br>
**Summary of Code:**
    1. **Purpose**: This code defines a class named `AddNewCustomer` for automating the process of adding new customers on a web application using Selenium.
    
    2. **Functionality**:
        - It provides methods to interact with various elements on the customer addition page such as email, password, first name, last name, gender, date of birth, company, tax exemption status, manager or vendor selection, account activation status, comment, newsletter subscription, and customer roles.
        - Methods like `saveNewCustomer`, `saveAndContinueNewCustomer`, `getSuccessAlertOnSave`, `getFailureAlertOnSave`, and `getBackToCustomerList` handle the saving of new customer data, alert messages, and navigation after saving.
    
    3. **Element Locators**: The class contains XPath, ID, and Link Text locators for different elements on the web page, which are used by the methods to interact with those elements using Selenium WebDriver.
2. Create 'GenerateRandomNewCustomerData.py' inside *Utilities* to generate random user data and save into csv file
    1. **generate_random_user**: This function generates random customer data such as first name, last name, email, password, gender, birth date, company name, comment, tax exemption status, manager or vendor ID, account status, newsletter subscription, and customer role. It returns this data as a dictionary.

    2. **saveNewCustomerData2CSV**: This function takes the generated customer data (in the form of a dictionary) and a filename as input. It checks if the file already exists. If it doesn't exist, it writes the header (field names) to the CSV file and then writes the data to it. If the file exists, it appends the data to the existing file. 
3. Create  test suite `test_AddNewCustomer.py` inside *testCases*<br>
    This code defines a test class `Test_AddNewCustomer` for adding a new customer. <br>
    Here's a summary of what it does:
    1. **Setup**: 
        - It imports necessary modules and classes including `LoginPage`, `AddNewCustomer`, `ReadConfig`, `LogGen`, and `GenerateRandomNewCustomerData`.
        - It sets up the base URL, admin username, password, and logging configuration.
        - The test method `test_AddNewCustomer` is defined within this class.

    2. **Test Execution**:
        - The test starts by logging in to the application using the admin credentials.
        - After successful login, it navigates to the "Add New Customer" page.
        - It generates random customer data using the `generate_random_user` function from the `GenerateRandomNewCustomerData` module.
        - The generated data is then filled into the corresponding fields on the "Add New Customer" page.
        - After filling the data, it saves the new customer information.
        - It checks for success or failure alert messages after saving.
        - Screenshots are captured based on the test result.
        - Test results are logged.
        - Assertions are made based on the success or failure of the test.

        ```python
        # Function to generate random data for new customer
        import random
        import string
        from datetime import datetime, timedelta

        def generate_random_user():
            first_names = ["Rupa", "Pawan", "Priyanka", "Pankaj", "Arun"]
            last_names = ["Singh", "Yadav", "Sharma", "Saini", "Pandey"]

            first_name = random.choice(first_names)
            last_name = random.choice(last_names)

            random_number = str(random.randint(100, 999))
            email = f"{first_name.lower()}_{last_name.lower()}{random_number}@gmail.com"

            password_length = 8
            password_characters = string.ascii_letters + string.digits
            password = ''.join(random.choice(password_characters) for i in range(password_length))

            gender = "Female" if first_name in ['Rupa', 'Priyanka'] else "Male"

            today = datetime.now()
            birth_date = today - timedelta(
                days=random.randint(18 * 365, 60 * 365))  # Assuming a person can be between 18 and 60 years old
            formatted_birth_date = birth_date.strftime('%m-%d-%Y')

            comment = "Random comment for user " + first_name + " " + last_name

            return {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "gender": gender,
                "birth_date": formatted_birth_date,
                "company_name": random.choice(['TCS', 'Walmart', 'Wipro', 'HCL']),
                "comment": comment,
                "tax_exempt": random.choice([True, False]),
                "manager_vendor": random.choice(['1', '2']),
                "account_status": random.choice([True, False]),
                "newsletter": [random.choice(["Your store name", "Test store 2"])],
                "customer_role": [random.choice(["Registered", "Guests"])]
            }
        ```
        ```python
        # Handle single Select dropdown 
        manager_vendor = Select(driver.find_element(By.ID, vendor_select_id))
        manager_vendor.select_by_index(2)

        ```
        ```python
        # Handle Multi Select Dropdown
        customer_roles_select_id = "SelectedCustomerRoleIds"
        select_element = driver.find_element(By.ID, customer_roles_select_id)

        # Open the dropdown using JavaScript, must for multi select dropdown, if not working with comman method
        driver.execute_script("arguments[0].style.display='block'; arguments[0].click();", select_element)
        select_option = Select(select_element)
        select_option.deselect_all()

        # Select desired options
        for option in ['Administrators', 'Registered', 'Vendors']:
            select_option.select_by_visible_text(option)
        ```

#### 10.2 Search Customer
- Search by Email, First Name, Last Name, Birth Date, Registration date, last activity date, company name, customer role
- Create POM `SearchCustomer.py` inside pageObjects
    1. **Search Form Interaction**: The `SearchCustomer` class manages interactions with a web page's search form using Selenium, allowing users to input search criteria like email, names, dates, and roles.
    
    2. **Criteria Handling**: It offers methods to set various search criteria and execute searches, including email, names, birthdates, registration dates, company, IP address, and customer roles, enabling precise queries.
    
    3. **Automation Efficiency**: By leveraging Selenium's WebDriver, it facilitates efficient automation of search operations, including clicking the search button and retrieving results from the table.
- Create Test suite `test_SearchCustomer.py` inside testCases
    1. **Fixture Setup**: The code sets up fixture `search_setup`, initializing the test environment by logging in, navigating to the search page, and maximizing the window.

    2. **Search Setup**: Defines a method `search_customer_setup` for setting up search criteria and verifying search results. It logs test case details, sets search parameters based on input, performs the search, captures screenshots for pass/fail cases, and asserts the outcome.

    3. **Test Cases**: Multiple test methods (`test_search_by_email`, `test_search_by_firstname`, etc.) are defined to execute specific searches using different criteria (email, first name, last name, etc.) utilizing the `search_customer_setup` method. Each test method provides input data and expected outcomes for the search criteria.

## ********************** Till Here Design and Implementation Completed ****************************************

### Step 11: Grouping Tests
#### 11.1 Grouping Markers (Add Markers to every test method)
```python
@pytest.mark.sanity
@pytest.mark.regression
```
#### 11.2 Add Marker entries in `pytest.ini` file inside *root directory*
```python
# pytest.ini

[pytest]
markers = 
    sanity
    regression
```
#### Command to run test cases in CLI
```commandline
pytest -v -s -m "sanity"
pytest -v -s -m "regression"
pytest -v -s -m "sanity and regression"
pytest -v -s -m "sanity or regression"
pytest -v -s -m "sanity" --html=.Reports/Sanity_test_report.html --browser edge
```
- Here `and` those test cases have both sanity and regression mark will execute from all the test cases
```python
@pytest.mark.sanity
@pytest.mark.regression
def test_loginPageTitle(self, setup):
    self.driver = setup
```
- `or` means those test cases have either sanity or regression will execute from all the test cases
```python
@pytest.mark.sanity
def test_AddNewCustomer(self, setup):

# or 

@pytest.mark.regression
def test_login_ddt(self, setup):
```

### ~~Step 12: Run Tests in Command Prompt and using `run.bat` file : **Not working in my system**~~
#### 12.1 Create `run.bat` file inside root directory
- Paste the same command above command as required or modify as per required.
- Multiple commands can also be written in run.bat file but only one command can be executed at a time, so comment other commands
- there are two types to comment in bat file `REM` and `::`, use any one
```bat
REM This is a comment using the REM command.
:: This is a comment using the :: command.
```
 - Paste the below command in run.bat and save it. No,IDE or browser required to keep open. 
 - **Double click on bat file to run**,
```commandline
# run.bat
pytest -v -s -m "sanity" --html=Reports/testReport.html --browser edge
:: pytest -v -s -m "regression" --html=Reports/Test_Report.html --browser chrome
:: pytest -v -s -m "sanity and regression" --html=Reports/Test_Report.html --browser edge
:: pytest -v -s -m "sanity or regression" --html=Reports/Test_Report.html --browser edge
:: pytest -n=3 "sanity"
:: pytest "regression" --browser chrome --count=3
```

