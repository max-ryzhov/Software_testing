from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group_methods import GroupHelper
from fixture.contact_methods import ContactHelper
""" Win 7
Python 3.8.7
selenium==3.141.0
Chrome 109.0.5414, ChromeDriver 109.0.5414
FF 109.0.1,        geckodriver-v0.32.1
IE 11.0.96,        IEDriverServer_x64_4.8.0
"""
# C:\Users\Max\Python_QA\Software_testing\venv\Scripts\activate
# py.test --browser=firefox --target=target.json ./test/test_add_contact.py


class Application:

    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f'Unrecognised browser {browser}')
        self.wd.implicitly_wait(.5)
        self.base_url = base_url
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
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
