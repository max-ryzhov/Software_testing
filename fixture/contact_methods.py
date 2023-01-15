from time import sleep
from model.contact_construct import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_param):
        wd = self.app.wd
        self.app.open_home_page()
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact_param)
        # submit new creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def update_first(self, contact_param):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact_param)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact_param):
        wd = self.app.wd
        self.change_field_value('firstname', contact_param.firstname)
        self.change_field_value('lastname', contact_param.lastname)
        self.change_field_value('middlename', contact_param.middlename)
        self.change_field_value('nickname', contact_param.nickname)
        self.change_field_value('title', contact_param.title_user)
        self.change_field_value('address', contact_param.address)
        self.change_field_value('company', contact_param.company)
        self.change_field_value('mobile', contact_param.mobile)
        self.change_field_value('email', contact_param.email)

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def view_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        self.return_to_home_page()

    def add_to_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_xpath("//*[contains(text(), 'group page')]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('addressbook/'):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                index = element.find_element_by_name("selected[]").get_attribute('value')
                f_name = element.find_element_by_xpath(".//td[3]").text
                l_name = element.find_element_by_xpath(".//td[2]").text
                self.contact_cache.append(Contact(cont_id=index, firstname=f_name, lastname=l_name))
        return self.contact_cache
