from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="79009009090",
                                   mobile_phone="901111",
                                   work_phone="80245",
                                   secondary_phone='7(902)001',
                                   email1="mail1@mail.ru", email2="mail2@mail.ru", email3="mail3@mail.ru",
                                   address="Address one"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts