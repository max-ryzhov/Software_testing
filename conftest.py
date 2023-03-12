import json

import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application
from fixture.db import DbFixture

fixture = None  # вводим глобальную переменную, по умолчанию None
target = None  # вводим глобальную переменную, по умолчанию None


# функция, загружающая данные авторизации из target.json для app и db
def load_config(file):
    global target  # пробрасываем переменную в область видимости функции
    if target is None:  # проверяем, прочитан ли конф.файл
        # определение пути к файлу target.json относительно директории проекта
        # os.path.abspath(__file__) - абсолютный путь до файла conftest.py
        # os.path.dirname(os.path.abspath(__file__) - абс. путь до директории, содер. conftest.py (директории проекта)
        # os.path.join() - абс.путь до директории проекта + отностительный путь до target.json
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:  # открываем кон.файл target.json в менеджере контекста with, как f
            target = json.load(f)  # читаем содержание f (target.json)
    return target


@pytest.fixture
def app(request):
    global fixture  # пробрасываем переменную в область видимости функции
    browser = request.config.getoption('--browser')  # извлекаем тип браузер заданных параметров
    # web_config - данные для веб-авторизации, извлеченные из блока web файла target.json
    web_config = load_config(request.config.getoption('--target'))['web']
    if fixture is None or not fixture.isvalid():  # проверяем создана и валидна ли фикстура
        # извлекаем браузер, заданный в командной строке из объект-request, и base_url из target.json
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
        # создание сессии с именем и паролем из блока web файла target.json
    fixture.session.ensure_login(user_name=web_config["user_name"], password=web_config["password"])
    return fixture





@pytest.fixture(scope='session')
def db(request):    # фикстура подключения к DB
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config["host"],
                          name=db_config["name"],
                          user=db_config["user"],
                          password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture





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


#  динамическое связывание теста и тестовых данных. тестовые данные в фикстурах data_ и json_
def pytest_generate_tests(metafunc):
    # собираем инфу о всех фикстурах, исп в тесте
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):  # обрабатываем данные, начинающиеся c data_ (файл.py)
            testdata = load_from_module(fixture[5:])  # тестовые данные. удалить первые 5 символов(data_)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):  # обрабатываем фикструры, начинающиеся c json_( файл.json)
            testdata = load_from_json(fixture[5:])  # тестовые данные. удалить первые 5 символов(_json)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module(f'data.{module}').testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'data/{file}.json')) as f_json:
        print(f'data/{file}.json')
        return jsonpickle.decode(f_json.read())
