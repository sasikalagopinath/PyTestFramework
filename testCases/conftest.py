import pytest
import pytest_html
from selenium import webdriver

#we will create fixture method which will return the driver for us
# @pytest.fixture
# def setup(browser):
#    driver = webdriver.Chrome()
#    return driver
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver


# This tells pytest to accept a command-line argument called --browser.
# It allows you to add custom command-line options when running tests.
# parser is a built-in object that lets you add those options.

def pytest_addoption(parser):
    parser.addoption("--browser")

#This function fetches the value passed using --browser.
@pytest.fixture()
def browser(request):
    #This line retrieves the value that was passed using --browser in the command line.
    return request.config.getoption("--browser")

#Clean unwanted data
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Platform", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     session.config._metadata["Project Name"]= "Mercury Tours"

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     if not hasattr(config, '_metadata'):
#         config._metadata = {}
#     config._metadata["Project Name"] = "Mercury Tours"
#     config._metadata["Module Name"] = "Login"
#     config._metadata["Tester"] = "Sasikala"