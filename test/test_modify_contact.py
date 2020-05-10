from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="7(900)9009090"))
    app.contact.modify_first(Contact(firstname="Boris",
                               lastname="Grebenschikov",
                               nickname="modified",
                               home_phone="7(800)8008080"))
