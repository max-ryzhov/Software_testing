class SessionHelper:

    def __init__(self, app):
        self.app = app  # параметр app - ссылка на фикстуру application

    def login(self, user_name, password):
        wd = self.app.wd    # доступ к драйверу через ссылку фикстуру application
        self.app.open_home_page()   # медот отсался в application, добавляем .app
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
