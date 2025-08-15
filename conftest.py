import pytest
import requests
from selenium import webdriver
import data
from page_object.pages.login_page import LoginPage


@pytest.fixture
def create_user():
    response = requests.post(f'{data.BASE_API_URL}/auth{data.REGISTER_API_URL}', data={
        "email": data.EMAIL,
        "password": data.PASSWORD,
        "name": data.NAME
    })
    create_user = response.json()
    yield create_user
    requests.delete(f'{data.BASE_API_URL}/auth{data.USER_API_URL}', headers={'Authorization': create_user['accessToken']})

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

