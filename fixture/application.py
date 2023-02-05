from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group_methods import GroupHelper
from fixture.contact_methods import ContactHelper


class Application:

    def __init__(self, browser='chrome'):
        if browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f'Unrecognised browser {browser}')
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
