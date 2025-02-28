from selenium import webdriver

import datetime
import pytest
import logging
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def driver(request):
    url = "https://demo-opencart.ru"
    
    browser = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    
    logger = logging.getLogger(request.node.name)
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser == "chrome": driver = webdriver.Chrome()
    elif browser == "firefox": driver = webdriver.Firefox()
    else: raise Exception("Driver not supported")

    allure.attach(
        name=driver.session_id,
        body=driver.current_url,
        attachment_type=allure.attachment_type.JSON
    )

    driver.log_level = log_level
    driver.logger = logger
    driver.maximize_window()
    driver.get(url)
    
    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
