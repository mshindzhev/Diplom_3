import pytest
from selenium import webdriver
import data
from page_object.pages.login_page import LoginPage

@pytest.fixture
def login_user(driver):
    login_user = LoginPage(driver)
    return login_user.login()

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    data.BROWSER_NAME = request.param
    if data.BROWSER_NAME == 'Chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

