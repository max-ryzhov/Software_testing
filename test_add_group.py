# -*- coding: utf-8 -*-
import unittest
from group_param import GroupParam
from application.application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(user_name="admin", password="secret")
        self.app.create_new_group(GroupParam(group_name="Meeting", header="Hello", footer="Bye"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(user_name="admin", password="secret")
        self.app.create_new_group(GroupParam(group_name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
