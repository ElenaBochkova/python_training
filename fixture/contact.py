from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_list_of_contact()
            contacts = wd.find_elements_by_name("entry")
            self.contact_cache = []
            for element in contacts:
                fname = element.find_element_by_xpath(".//td[3]").text
                lname = element.find_element_by_xpath(".//td[2]").text
                phone = element.find_element_by_xpath(".//td[6]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, home_phone=phone, id=id))
        return self.contact_cache

    def count(self):
        wd = self.app.wd
        self.open_list_of_contact()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first(self, contact):
        self.modify_by_index(contact, 0)

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.open_list_of_contact()
        self.select_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_list_of_contact()
        self.select_by_index(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to.alert.accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

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
        if not(wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()