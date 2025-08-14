import pytest
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import data


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

@pytest.fixture(params=['Firefox', 'Chrome'])
def driver(request):
    data.BROWSER_NAME = request.param
    if data.BROWSER_NAME == 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()

