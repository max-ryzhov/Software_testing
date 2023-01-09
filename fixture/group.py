from time import sleep


class GroupHelper:

    def __init__(self, app):
        self.app = app  # экземпляр кл GroupHelper принимает св-во - фикстуру app(экземпляр кл Application)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group_param):
        wd = self.app.wd
        self.open_group_page()
        # init new creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_param)
        # submit new creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def modify_first_group(self, new_group_param):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_param)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group_param):
        wd = self.app.wd
        self.change_field_value('group_name', group_param.group_name)
        self.change_field_value('group_header', group_param.header)
        self.change_field_value('group_footer', group_param.footer)

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
