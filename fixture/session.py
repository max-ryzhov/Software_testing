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
