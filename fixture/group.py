from time import sleep


class GroupHelper:

    def __init__(self, app):
        self.app = app    # экземпляр кл GroupHelper принимает св-во - фикстуру app(экземпляр кл Application)

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

    def update_first(self, group_param):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group_param)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def fill_group_form(self, group_param):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_param.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_param.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_param.footer)

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
