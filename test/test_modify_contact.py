from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(firstname="Boris",
                               lastname="Grebenschikov",
                               nickname="modified",
                               home_phone="7(800)8008080"))
    app.session.logout()
