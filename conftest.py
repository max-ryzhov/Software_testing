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
    browser = request.config.getoption('--browser')    # извлекаем тип браузер заданных параметров
    if target is None:    # проверяем, прочитан ли конф.файл
        # определение пути к файлу target.json относительно директории проекта
        # os.path.abspath(__file__) - абсолютный путь до файла conftest.py
        # os.path.dirname(os.path.abspath(__file__) - абс. путь до директории, содер. conftest.py (директории проекта)
        # os.path.join() - абс.путь до директории проекта + отностительный путь до target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        with open(config_file) as f:    # открываем кон.файл target.json в менеджере контекста with, как f
            target = json.load(f)  # читаем содержание f (target.json)
    if fixture is None or not fixture.isvalid():  # проверяем создана и валидна ли фикстура
        # извлекаем браузер, заданный в командной строке из объект-request, и base_url из target.json
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        # создание сессии с именем и паролем из target.json
    fixture.session.ensure_login(user_name=target["user_name"], password=target["password"])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# парсер параметров запуска тестов [# py.test test_del_group.py --browser=firefox]
def pytest_addoption(parser):
    # задать опции парсеру: имя параметра,  что сделать, значение по умолчанию
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--target', action='store', default='target.json')
