from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group_methods import GroupHelper
from fixture.contact_methods import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()  # ссылка на веб-драйвер
#        self.wd.implicitly_wait(2)
        # ссылки на помощники:
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def isvalid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith('addressbook/'):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
