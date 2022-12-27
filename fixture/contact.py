from time import sleep


class ContactHelper:

    def __init__(self, app):
        self.app = app    # экземпляр кл ContactHelper принимает св-во - фикстуру app(экземпляр кл Application)

    def create(self, contact_param):
        wd = self.app.wd
        self.app.open_home_page()
        # init creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_param.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_param.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_param.nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_param.address)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_param.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_param.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_param.email)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_param.middlename)
        # submit new creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def del_first_contact(self):
        wd = self.app.wd
    # переход на стр контактов
        self.app.open_home_page()
    # выбор первого контакта
        wd.find_element_by_name('selected[]').click()
    # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
    # подтверждение удаления
        wd.switch_to.alert.accept()
    # возврат на главную
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
