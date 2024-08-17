import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    return driver


def pytest_addoption(parser):  # this will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to set-up method
    return request.config.getoption("--browser")



# Customising the HTML report
# it is hook for adding the environment info to the HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = "Noop Commerce"
#     config._metadata['Module Name'] = "Login Module"
#     config._metadata['Tester Name'] = "Mohammad Zayn"
#
# # it is hook for deleting/modifying the environment info in the HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('Python', None)
#     metadata.pop('Plugins', None)