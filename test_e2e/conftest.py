from selenium import webdriver

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(autouse=True, scope="session")
def driver():
    # browser_name = request.config.getoption("--browser_name")
    #if browser_name == "chrome":
    driver = webdriver.Chrome(executable_path="I:\\Softwares\\Selenium\\chromedriver.exe")
    driver.get("http://ninedt.herokuapp.com/#/game")
    # elif browser_name == "firefox":
    #     driver = webdriver.Firefox(executable_path="C:\\gecko.exe")
    #     driver.get("http://ninedt.herokuapp.com/#/game")
    driver.maximize_window()
    # request.cls.driver = driver
    yield driver
    #driver.close()
