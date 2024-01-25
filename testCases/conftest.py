from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


def pytest_addoption(parser): # this will get the value from the CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): # this will return the browser value to the setup method
    return request.config.getoption("--browser")
