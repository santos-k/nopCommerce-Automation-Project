# nopCommerceAumation-Project

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
4. Pytest-xdist
5. Allure-pytest
6. Openpyxl

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

### 8 Generate HTML Reports
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
