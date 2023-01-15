from time import sleep
from model.group_construct import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def modify_first_group(self, new_group_param):
        wd = self.app.wd
        self.modify_group_by_index(0, new_group_param)

    def modify_group_by_index(self, index, new_group_param):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_param)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

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
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                index = element.find_element_by_name("selected[]").get_attribute('value')
                self.group_cache.append(Group(group_name=text, group_id=index))
        return list(self.group_cache)
