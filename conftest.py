import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#Выбор языка при запуске
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru or en")

#Фикстура для всех тестов которая запускает драйвер и настраивает язык
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
