from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="7(900)9009090"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Boris", lastname="Grebenschikov",
                      nickname="modified", home_phone="7(800)8008080")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
