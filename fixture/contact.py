from time import sleep


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

    def update_first(self, contact_param):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact_param)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()

    # def fill_contact_form(self, contact_param):
    #     wd = self.app.wd
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact_param.firstname)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact_param.lastname)
    #     wd.find_element_by_name("middlename").click()
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(contact_param.middlename)
    #     wd.find_element_by_name("nickname").click()
    #     wd.find_element_by_name("nickname").clear()
    #     wd.find_element_by_name("nickname").send_keys(contact_param.nickname)
    #     wd.find_element_by_name("title").click()
    #     wd.find_element_by_name("title").clear()
    #     wd.find_element_by_name("title").send_keys(contact_param.title)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact_param.address)
    #     wd.find_element_by_name("company").click()
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys(contact_param.company)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact_param.mobile)
    #     wd.find_element_by_name("email").click()
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys(contact_param.email)

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
