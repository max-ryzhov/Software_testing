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

    def ensure_login(self, user_name, password):
        wd = self.app.wd
        if self.is_logged_in():    # залогинены?
            if self.is_logged_in_as(user_name):    # имя пользователя верное?
                return    # если оба условия True - ничего не делаем
            else:
                self.logout()    # logout если имя пользователя неверное
        self.login(user_name, password)    # login, если хоть одно условие False

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):    # проверяем залогинены ли мы
        wd = self.app.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            return True

    def is_logged_in_as(self, user_name):    # проверяем верное ли имя пользователя
        wd = self.app.wd
        if wd.find_element_by_xpath("//div[@id='top']/form/b").text == '('+user_name+')':
            return True
