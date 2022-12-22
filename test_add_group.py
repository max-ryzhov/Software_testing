# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()    # driver link
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd    # driver link
        self.open_home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_group_page(wd)
        self.create_new_group(wd, group_name="Meeting", header="Hello", footer="Bye")
        self.return_to_group_page(wd)
        self.logout(wd)








    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_new_group(self, wd, group_name, header, footer):
        # init new creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit new creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
