# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Bochkova",
                      nickname="alef", home_phone="79009009090",
                      mobile_phone="901111", work_phone="80245",
                      secondary_phone='7(902)001',
                      email1="mail1@mail.ru", email2="mail2@mail.ru", email3="mail3@mail.ru",
                      address="Address one")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



