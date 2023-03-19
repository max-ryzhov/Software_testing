from time import sleep
import re
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

    def modify_first(self, contact_param):
        wd = self.app.wd
        self.modify_contact_by_index(0, contact_param)

    def modify_contact_by_index(self, index, contact_param):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_edit_page_by_index(index)
        self.fill_contact_form(contact_param)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_edit_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]   # выбрал ряд
        row.find_element_by_xpath(".//td[7]").click()    # кнопка просмотр в 7м столбце

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        secondphone = re.search('P: (.*)', text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondphone=secondphone)

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        cont_id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondphone = wd.find_element_by_name('phone2').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, cont_id=cont_id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondphone=secondphone,
                       email=email, email2=email2, email3=email3)

    def fill_contact_form(self, contact_param):
        wd = self.app.wd
        self.change_field_value('firstname', contact_param.firstname)
        self.change_field_value('lastname', contact_param.lastname)
        self.change_field_value('middlename', contact_param.middlename)
        self.change_field_value('nickname', contact_param.nickname)
        self.change_field_value('title', contact_param.title_user)
        self.change_field_value('address', contact_param.address)
        self.change_field_value('company', contact_param.company)
        self.change_field_value('email', contact_param.email)
        self.change_field_value('email2', contact_param.email2)
        self.change_field_value('email3', contact_param.email3)
        self.change_field_value('home', contact_param.homephone)
        self.change_field_value('mobile', contact_param.mobilephone)
        self.change_field_value('work', contact_param.workphone)
        self.change_field_value('phone2', contact_param.secondphone)

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def delete_first(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name('selected[]')[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    # удаление контактов по group_id
    def delete_contact_by_id(self, con_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(con_id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    # выбор контактов по group_id
    def select_contact_by_id(self, con_id):
        wd = self.app.wd
        wd.find_element_by_id(con_id).click()

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
                all_phones = element.find_element_by_xpath(".//td[6]").text    # получаем строку с 4 переносами
                all_emails = element.find_element_by_xpath(".//td[5]").text    # получаем строку с 4 переносами
                self.contact_cache.append(Contact(cont_id=index, firstname=f_name, lastname=l_name,
                                                  all_phones_from_hp=all_phones, all_emails_from_hp=all_emails))
        return self.contact_cache
