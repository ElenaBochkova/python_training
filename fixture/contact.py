from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_list_of_contact()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_list_of_contact()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").text
        print(address)
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone,
                       email1=email1, email2=email2, email3=email3,
                       address=address)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_list_of_contact()
            contacts = wd.find_elements_by_name("entry")
            self.contact_cache = []
            for element in contacts:
                cells = element.find_elements_by_tag_name("td")
                lname = cells[1].text
                fname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  address=address, all_email=all_email
                                                  ))
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
        self.open_contact_to_edit_by_index(index)
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.select_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

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
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address", contact.address)

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

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        print([contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone])
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x), filter(lambda x: x is not None,
                                                               [contact.home_phone, contact.mobile_phone,
                                                                contact.work_phone, contact.secondary_phone]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3])))