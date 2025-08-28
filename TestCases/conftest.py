import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager

        options = Options()
        options.add_argument("--remote-allow-origins=*")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("launching chrome browser********")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("launching firefox browser********")
    else:
        driver = webdriver.Ie()

    return driver






