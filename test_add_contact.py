# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from group_param import GroupParam


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd, firstname="Max", lastname="Ryzhov", nickname="max_ryzh", address="NN",
                                company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                middlename="Nick")
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_new_contact2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd, firstname="Петя", lastname="Иванов", nickname="pet", address="Spb",
                                company="Ya", mobile="+79993330011", email="pet@gmail.com",
                                middlename="Ya")
        self.return_to_home_page(wd)
        self.logout(wd)


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_new_contact(self, wd, firstname, lastname, nickname, address, company, mobile, email, middlename):
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        # submit new creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
