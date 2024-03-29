# nopCommerceAutomation-Project
**Selenium Hybrid Framework for nopCommerce Backend System**

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
---

## Let's Start

### Step 1: Create a New Project in PyCharm, use Virtual Environment

- Project Name: `nopCommerceAutomation`

#### 1.1 Activate Virtual Environment
1. **Open Terminal**
2. **Navigate to Your Project Directory**: 
3. **Activate Virtual Environment**: Once you're in the project directory, you can activate the virtual environment using the following command:

   ```bash
   source venv/bin/activate
   ```

   If you're using Windows, the command will be slightly different:

   ```bash
   venv\Scripts\activate
   ```
4. **Verify Activation**: You'll know the virtual environment is activated when you see the environment name in parentheses at the beginning of your command prompt, something like `(venv) user@hostname:~/project$`.

#### 1.2 Install Required Packages/Plugins

1. Selenium
2. Pytest
3. Pytest-html
4. Pytest-xdist : Run parallel execution use in CLI `-n 4`, `-n auto` or `-n=4`
5. Allure-pytest
6. Openpyxl
7. Pytest-repeat : repeat any test multiple times use in CLI `--count=4`

##### 1.3 Install Packages from requirements.text file
```bash
pip install -r requirements.txt
```

##### 1.4 Create requirements.txt if this new project after install manually all packages
```bash
pip freeze > requirements.txt    
```
---

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
    ├── requirement.txt
    ├── pytest.ini
    ├── run.bat
```
---
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
2. **`-v` (or `--verbose`)**: Increases test verbosity, showing more details about each test.
3. **`-s` (or `--capture=no`)**: Disables output capturing, allowing you to see the standard output during test execution.

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
- By organizing shared fixtures, hooks, and configurations in `conftest.py`, you can create a centralized location for common testing infrastructure, promoting code reusability and maintainability across your pytest project.
---
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
---
### Step 5: Read Common values from ini file
#### 5.1 Add 'config.ini' file in 'Configurations' folder
```commandline
[common info]
base_URL = https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
adminEmail = admin@yourstore.com
password = admin

```
#### 5.2 Create 'readProperties.py' utility under 'Utilities' package to read common data
```python
import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURl():
        url = config.get('common info', 'base_URL')
        return url

    @staticmethod
    def getAdminEmail():
        adminEmail = config.get('common info', 'adminEmail')
        return adminEmail

    @staticmethod
    def getAdminPassword():
        password = config.get('common info', 'password')
        return password

```
#### 5.3 Replace hard coded values in Login test case
```python
class Test_001_Login:
    base_URL = ReadConfig.getApplicationURl()
    username = ReadConfig.getAdminEmail()
    password = ReadConfig.getAdminPassword()
    logger = LogGen.loggen()
```
---
### Step 6: Adding Logs to Test cases
#### 6.1 Add customLogger.py under utilities package.
```python
import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        f_handler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        f_handler.setFormatter(formatter)
        logger.addHandler(f_handler)
        logger.setLevel(logging.INFO)
        return logger

```
#### 6.2 Add logs to login test case
```python
from utilities.customLogger import LogGen

class Test_001_Login:
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info(f"************ Test running in {self.driver.capabilities['browserName']} browser ***************")
        self.logger.info("*********** test_homePageTitle *************")

```
---
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
---
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
---
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
---
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

<br>****************** Till Here Design and Implementation Completed ******************************

---
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
---
### Step 12: Run Tests in Command Prompt and using `run.bat` file
#### 12.1 Create `run.bat` file inside root directory
- Paste the same command above command as required or modify as per required.
- Comment in batch file `REM` and `::`, use any one
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
if above code giving error like `pytest is not recognized as an internal or external command, operable program or batch file.`
##### **Try with below code** : 
First mention project path of virtual env followed by pytest command and save it to batch file `run.bat` and open or double click to run
```commandline
C:\Projects\Python\nopCommerceAutomation\venv\Scripts\pytest -v -s -m "sanity" --html=Reports/testReport.html --browser edge
```

- Multiple commands can also be run in batch file, it will run in sequence only, like first comment will execute then second and third command.
```commandline
C:\Projects\Python\nopCommerceAutomation\venv\Scripts\pytest -v .\testCases\test_SearchCustomer.py::Test_SearchCustomer_003::test_search_by_email --browser chrome
C:\Projects\Python\nopCommerceAutomation\venv\Scripts\pytest -v .\testCases\test_SearchCustomer.py::Test_SearchCustomer_003::test_search_by_firstname --browser edge
C:\Projects\Python\nopCommerceAutomation\venv\Scripts\pytest -v .\testCases\test_SearchCustomer.py::Test_SearchCustomer_003::test_search_by_lastname --browser firefox
```
---
### Step 13: Push the Code into Git & GitHub Repository

Let's break down Git, GitHub, and Jenkins workflows separately, and then discuss how they can work together:

### Git:
Git is a distributed version control system used for tracking changes in source code during software development. Here's how it works:

1. **Repository**: A Git repository is a collection of files and their history. It resides either locally on a developer's machine or remotely on a server.

2. **Commits**: Developers make changes to files in their local repository and create commits to save those changes. Each commit represents a snapshot of the files at a particular point in time.

3. **Branches**: Git allows developers to work on multiple versions of a project simultaneously through branches. Branches are independent lines of development that can be merged back into the main codebase.

4. **Merging and Pull Requests**: When a developer completes work on a branch, they can merge it back into the main codebase through a merge operation. In collaborative environments, developers often use pull requests to propose changes, discuss them, and merge them into the main branch.

### GitHub:
GitHub is a web-based platform built around Git that provides hosting for Git repositories and collaboration features. Here's how it works:

1. **Remote Repository Hosting**: GitHub hosts remote Git repositories, allowing developers to store their code in the cloud and collaborate with others.

2. **Pull Requests and Code Reviews**: GitHub provides features for creating pull requests, reviewing code, and discussing changes collaboratively. This facilitates code review processes and ensures high-quality contributions.

3. **Issue Tracking and Project Management**: GitHub includes issue tracking and project management tools that help teams organize their work, track bugs, and plan releases.

### Jenkins:
Jenkins is an open-source automation server used for building, testing, and deploying software. Here's how it works:

1. **Jobs**: Jenkins jobs are individual tasks that automate various aspects of the software development process, such as compiling code, running tests, and deploying applications.

2. **Build Pipelines**: Jenkins allows users to define pipelines, which are sequences of jobs that define the entire software delivery process. Pipelines can include stages for building, testing, and deployment, with conditional logic and parallel execution.

3. **Integration with Version Control Systems**: Jenkins integrates with version control systems like Git to trigger builds automatically whenever changes are pushed to a repository. This ensures that code is continuously tested and integrated into the project.

### Combined Workflow:
When combined, Git, GitHub, and Jenkins form a powerful workflow for software development:

1. **Version Control with Git and GitHub**: Developers use Git for version control, making changes locally and pushing them to GitHub for collaboration and backup.

2. **Continuous Integration with Jenkins**: Jenkins monitors GitHub repositories for changes and automatically triggers build and test jobs whenever new code is pushed. This ensures that changes are tested continuously and integrated into the codebase as soon as possible.

3. **Automated Deployment**: Jenkins can also handle deployment tasks, allowing teams to automate the process of releasing new versions of their software.

4. **Collaboration and Code Review**: GitHub's pull request and code review features facilitate collaboration among team members, ensuring that changes are reviewed and discussed before being merged into the main codebase.

In summary, Git provides version control, GitHub offers collaboration features and remote repository hosting, and Jenkins automates the build, test, and deployment process, creating a seamless workflow for software development.

Certainly! Let's walk through a simplified example of how Git, GitHub, and Jenkins can work together in a software development workflow, using commands and code snippets where appropriate.

### Git Workflow:

![Git](https://www.nexcess.net/images/blog/posts/2021/10/what-is-git-embedded-3.png)

1. **Initialize a Git Repository:**
   ```bash
   git init my_project
   cd my_project
   ```

2. **Add and Commit Changes:**
   ```bash
   touch README.md
   git add README.md
   git commit -m "Initial commit"
   ```

3. **Create and Switch to a New Branch:**
   ```bash
   git checkout -b feature-branch
   ```

4. **Make Changes and Commit:**
   ```bash
   # Make changes to files
   git add .
   git commit -m "Add new feature"
   ```

5. **Push Changes to GitHub:**
   ```bash
   git push origin feature-branch
   ```

### GitHub Workflow:
![Git](https://blog.kakaocdn.net/dn/l6NAP/btrDqUnEpR5/2VDMW0FoSLhwXNm2mu99x0/img.png)
![Git](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd47de46b-2c7b-43d2-8a9a-a2ebb7600347_1324x2004.jpeg)

1. **Create Pull Request:**
   - Create a new pull request on the GitHub web interface.
   - Describe the changes and request a review from team members.

2. **Code Review and Discussion:**
   - Team members review the pull request, provide feedback, and discuss changes.
   - Make any necessary modifications based on feedback.

3. **Merge Pull Request:**
   - Once the changes are approved, merge the pull request into the main branch on GitHub.

### Jenkins Workflow:
![Jenkins](https://media.licdn.com/dms/image/C5612AQGxPAmm8GEqYw/article-cover_image-shrink_720_1280/0/1594662460637?e=1712188800&v=beta&t=1MPInCm6C3BqzblenhXzECZncaRvu5wJ8eoBRsUdT2M)
![Jenkins](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2019/10/20/Diagram2.png)

1. **Set Up Jenkins Job:**
   - Create a new Jenkins job and configure it to monitor the GitHub repository for changes.

2. **Define Build Steps:**
   - Define build steps in the Jenkins job configuration, such as compiling code, running tests, and generating artifacts.

3. **Trigger Builds Automatically:**
   - Configure the Jenkins job to trigger builds automatically whenever changes are pushed to the GitHub repository.

4. **View Build Results:**
   - Monitor the Jenkins dashboard to view build results and logs.
   - Receive notifications for build failures or successes.

### Combined Workflow:

1. **Developer Pushes Changes to GitHub:**
   - After making changes and committing them locally, the developer pushes the changes to the GitHub repository.
   ```bash
   git push origin feature-branch
   ```

2. **Jenkins Triggers Build:**
   - Jenkins detects the new changes on GitHub and triggers a build job automatically.

3. **Build, Test, and Deploy:**
   - Jenkins executes the build steps defined in the job configuration, including compiling code, running tests, and generating artifacts.
   - If the build is successful, Jenkins can automatically deploy the application to a staging environment.

4. **Review and Merge Pull Request:**
   - Team members review the changes on GitHub, discuss them, and merge the pull request into the main branch once approved.

5. **Jenkins Continuous Integration:**
   - Jenkins continues to monitor the GitHub repository for new changes and repeats the build process whenever new commits are pushed.

This integrated workflow ensures that changes are tested automatically, reviewed by team members, and integrated into the codebase efficiently.

## Structure:
1. **Project Code** : in local system
   - Project -> File Structure -> Code
2. **Git**: Local Repository
   - Code inside a local repository, it can be on local system or server
   - Commands to create git repository
   ```commandline
    git init
    git add .
    git commit -m "Commit message"
    git remote add origin https://github.com/santos-k/nopCommerce-Automation-Project.git  
    ```
3. **GitHub** : Remote/Global Repository
   - code to remote server like github.com
   - Command to push git on GitHub
   ```commandline
    git push -u origin master
    ```
4. **Jenkins**: automation server used for building, testing, and deploying software
   
### Important Git Commands

#### Configuration
- **git config**: Set or get configuration options.
  - Example:
    ```bash
    git config --global user.name "John Doe"
    ```

#### Repository Initialization
- **git init**: Create an empty Git repository or reinitialize an existing one.
  - Example:
    ```bash
    git init
    ```

#### Staging and Committing
- **git add**: Add file contents to the index.
  - Example:
    ```bash
    git add myfile.txt
    ```
- **git status**: Show the working tree status.
  - Example:
    ```bash
    git status
    ```
- **git commit**: Record changes to the repository.
  - Example:
    ```bash
    git commit -m "Initial commit"
    ```

#### Branching and Merging
- **git branch**: List, create, or delete branches.
  - Example:
    ```bash
    git branch mybranch
    ```
- **git checkout**: Switch branches or restore working tree files.
  - Example:
    ```bash
    git checkout mybranch
    ```
- **git merge**: Join two or more development histories together.
  - Example:
    ```bash
    git merge mybranch
    ```

#### Remote Repositories
- **git remote**: Manage set of tracked repositories.
  - Example:
    ```bash
    git remote add origin <remote_URL>
    ```
- **git fetch**: Download objects and refs from another repository.
  - Example:
    ```bash
    git fetch origin
    ```
- **git pull**: Fetch from and integrate with another repository or a local branch.
  - Example:
    ```bash
    git pull origin master
    ```
- **git push**: Update remote refs along with associated objects.
  - Example:
    ```bash
    git push origin master
    ```

#### Undoing Changes
- **git reset**: Reset current HEAD to the specified state.
  - Example:
    ```bash
    git reset --hard HEAD~1
    ```
- **git revert**: Create new commit that undoes changes made in the specified commit.
  - Example:
    ```bash
    git revert HEAD
    ```

#### History and Inspection
- **git log**: Show commit logs.
  - Example:
    ```bash
    git log
    ```
- **git diff**: Show changes between commits, commit and working tree, etc.
  - Example:
    ```bash
    git diff HEAD~1 myfile.txt
    ```

#### Tagging
- **git tag**: Create, list, delete, or verify a tag object signed with GPG.
  - Example:
    ```bash
    git tag v1.0.0
    ```

#### Collaboration
- **git clone**: Clone a repository into a new directory.
  - Example:
    ```bash
    git clone <repository_URL>
    ```
- This is not an exhaustive list, but it covers many of the common Git commands and their basic usage.

---

### Step 14: Run Tests using Jenkins
**Jenkins-CI Tool Setup Guide**

1. **Accessing Jenkins**
   - Open Jenkins in a browser by navigating to `http://localhost:8080/`.
   - Log in with the default credentials: `admin:admin`.

2. **Project Setup**
   - **Running GitHub Project in Jenkins:**
     1. Click on **New Item** to create a new project.
     2. Enter the desired project name and select **Freestyle Project**.
     3. Click **OK** and wait for the configuration page to appear.
     4. Configure project settings:
        - Under **General Tab**:
          - Provide a description if needed.
          - Select **Git** under **Source Code Management**.
            - Paste the GitHub repo URL in the `Repositories` section.
            - Specify the branch name in `Branches to Build` section.
          - Under **Build Steps**, select **Execute Windows batch command**.
            - Enter `run.bat` or the required command to execute.
          - Configure **Post-build Actions** (e.g., Email Notifications) if needed.
        - Click **Apply** and then **Save**.

   - **Configuring Git for Jenkins - One Time setup for all projects**:
     1. Copy the git.exe path from the local system (e.g., `C:\Program Files\Git\bin\git.exe`).
     2. Navigate to Jenkins Dashboard > **Manage Jenkins** > **Tools** > **Git**.
     3. Paste the Git/bin path into the `Path to Git Executable`.
     4. Click **Apply** and then **Save**.

   - **Running the Build**:
     - Click on **Build Now** to run the build inside the Jenkins project, or inside the Dashboard, click on **Build** button in the same project row to trigger the build.

3. **Jenkins Admin Password**
   - Access the Jenkins admin password from `C:\Users\withu\.jenkins\secrets\initialAdminPassword`.

**1. Jenkins Installation Methods:**
   **1.1 With WAR File:**
   - Deployment from Command Prompt
     - Navigate to the Jenkins directory
     - Run `java -jar jenkins.war`
     - Jenkins remains running until the Command Prompt is open
     - Browser opens automatically for Selenium tests

   **1.2 Using Jenkins Windows Installer:**
   - Install Jenkins as a Windows service
   - Automatically starts on system boot/reboot
   - Tests run in headless mode

**2. Additional Jenkins Commands:**

   **2.1 Managing Jenkins Processes:**
   - Stopping Jenkins: `.\jenkins.exe stop`
   - Starting Jenkins: `.\jenkins.exe start`
   - Restarting Jenkins: `.\jenkins.exe restart`

   **2.2 Jenkins Shutdown Best Practices:**
   - Avoid direct shutdown of Java process or Windows service
   - Use Jenkins' built-in shutdown mechanism
   - Access Jenkins via HTTP for safe shutdown
   - Commands include `exit`, `restart`, and `reload`
   - Example: `http://localhost:8080/exit` to stop Jenkins running on port 8080.

   **2.3 Starting Jenkins from Command Line:**
   - Open Command Prompt
   - Navigate to the directory with `jenkins.war`
   - Run `java -jar jenkins.war`

---
Till here folder structure:
```markdown
nopCommerceAutomation
│
├── Configurations
│   ├── config.ini
│
├── Logs
│   ├── automation.log
│
├── pageObjects
│   ├── AddNewCustomerPage.py
│   ├── LoginPage.py
│   ├── SearchCustomerPage.py
│   
│
├── Reports
│   ├── Sanity_Test_Report.html
│   └── testReport.html
│
├── Screenshots
│   ├── AddNewCustomer_Fail.png
│   ├── test_login_DDT_aNEe_Fail.png
│   └── test_login_DDT_aNEe_Pass.png
│
├── testCases
│   ├── conftest.py
│   ├── test_AddNewCustomer.py
│   ├── test_login.py
│   ├── test_login_ddt.py
│   └── test_SearchCustomer.py
│
├── TestData
│   ├── NewCustomerData.csv
│   └── nopCommerce_testdata.xlsx
│
├──utilities
│   ├── customLogger.py
│   ├── ExcelUtils.py
│   ├── GenerateRandomNewCustomerData.py
│   └── readProperties.py
├── requirement.txt
├── pytest.ini
└── run.bat

```
