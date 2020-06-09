from model.contact import Contact
import random


def test_modify_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="79009009090"),
                           mobile_phone="901111",
                           work_phone="80245",
                           secondary_phone='7(902)001',
                           email1="mail1@mail.ru", email2="mail2@mail.ru", email3="mail3@mail.ru",
                           address="Address one")
    old_contacts = db.get_contact_list()
    modified_contact = random.choice(old_contacts)
    contact = Contact(firstname="Boris", lastname="Grebenschikov",
                      nickname="modified", home_phone="78008008080",
                      mobile_phone="501001", work_phone="601001",
                      secondary_phone='7(902)001',
                      email1="gr1@mail.ru", email2="gr2@mail.ru", email3="gr3@mail.ru",
                      address="Address Gr one"
                      )
    contact.id = modified_contact.id
    app.contact.modify_by_id(contact, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    index = old_contacts.index(modified_contact)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
