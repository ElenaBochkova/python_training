
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def modify_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(contact, wd)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to.alert.accept()
        self.app.return_to_home_page()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact(contact, wd)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

    def fill_contact(self, contact, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()