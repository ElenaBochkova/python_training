# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Elena",
                               lastname="Bochkova",
                               nickname="alef",
                               home_phone="7(900)9009090"))
    app.session.logout()



