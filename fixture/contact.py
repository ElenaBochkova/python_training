
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def count(self):
        wd = self.app.wd
        self.open_list_of_contact()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first(self, contact):
        wd = self.app.wd
        self.open_list_of_contact()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_list_of_contact()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to.alert.accept()
        self.app.return_to_home_page()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

    def fill_contact(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("home", contact.home_phone)

    def change_field_value(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_list_of_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()