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
   - Identify re-test cases, re-fression cases, and automatable test cases.
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

#### 3.3 Create `conftest.py` under "testCases"

### Step 4: Capture Screenshots on Failures

#### 4.1 Update Login Test with Screenshot under "testCases"

- Implement screenshot capture in case of test failures.
