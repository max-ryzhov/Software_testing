import json

import pytest
import json
import os.path
from fixture.application import Application

fixture = None  # вводим глобальную переменную, по умолчанию None
target = None  # вводим глобальную переменную, по умолчанию None


@pytest.fixture
def app(request):
    global fixture  # пробрасываем переменную в область видимости функции
    global target  # пробрасываем переменную в область видимости функции
    browser = request.config.getoption('--browser')
    if target is None:    # проверяем, прочитан ли конф.файл
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        # открываем кон.файл target.json в менеджере контекста with, как config_file
        with open(config_file) as f:
            target = json.load(f)  # читаем содержание config_file (target.json)
    if fixture is None or not fixture.isvalid():  # проверяем создана и валидна ли фикстура
        # извлекаем браузер, заданный в командной строке через объект-request
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        # создание сессии с имемем и паролем из target.json
    fixture.session.ensure_login(user_name=target["user_name"], password=target["password"])
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
    parser.addoption('--target', action='store', default='target.json')
