import pytest
from fixture.application import Application


fixture = None    # вводим глобальную переменную, по умолчанию None


@pytest.fixture
def app(request):
    global fixture    # пробрасываем переменную в область видимости функции
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    if fixture is None:   # проверяем создана ли фикстура. если нет - создаем
        # извлекаем браузер, заданный в командной строке через объект-request
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.isvalid():    # проверяем валидна ли фикстура. isvalid задана в application
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(user_name="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# hook(зацепка), в нашем случае парсер командной строки
def pytest_addoption(parser):
    # задать опции парсеру: имя параметра,  что сделать, значение по умолчанию
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/')
