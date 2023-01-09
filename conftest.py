import pytest
from time import sleep
from fixture.application import Application


fixture = None    # вводим глобальную переменную, по умолчанию None


@pytest.fixture
def app(request):
    global fixture    # пробрасываем переменную в область видимости функции
    if fixture is None:   # проверяем создана ли фикстура. если нет - создаем
        fixture = Application()
    else:
        if not fixture.isvalid():    # проверяем валидна ли фикстура. isvalid задана в application
            fixture = Application()
    fixture.session.ensure_login(user_name="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        sleep(1)
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
