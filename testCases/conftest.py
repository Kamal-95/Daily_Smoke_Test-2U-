from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def setup2():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver

@pytest.fixture()
def setup1():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    return driver


