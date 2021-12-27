import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(autouse=True,scope="class")
def setup(request, browser):
    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "IE":
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    elif browser == "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    request.cls.driver = driver # return driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True )
def browser(request):
    """
    This function return the Browser value to setup method
    """
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True )
def url(request):
    """
    This function return the Browser value to setup method
    """
    return request.config.getoption("--url")