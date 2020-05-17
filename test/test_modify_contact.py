from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="7(900)9009090"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Boris", lastname="Grebenschikov",
                      nickname="modified", home_phone="7(800)8008080")
    contact.id = old_contacts[index].id
    app.contact.modify_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
