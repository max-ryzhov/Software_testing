class SessionHelper:

    def __init__(self, app):
        self.app = app    # экземпляр кл SessionHelper принимает св-во - фикстуру app(экземпляр кл Application)

    def login(self, user_name, password):
        wd = self.app.wd    # доступ к драйверу через фикстуру
        self.app.open_home_page()   # медот остался в классе Application. Добавляем .app для доступа через фикстуру
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return wd.find_element_by_link_text("Logout") is True    # проверяю, что хоть что то возвращается

    def is_logged_in_as(self, user_name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+user_name+")"

    def ensure_login(self, user_name, password):
        #if self.is_logged_in():
        #     if self.is_logged_in_as(user_name):
        #    pass
        #     else:
        #         self.logout()
        self.login(user_name, password)

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()


