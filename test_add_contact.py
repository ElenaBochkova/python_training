# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Elena",
                            lastname="Bochkova",
                            nickname="alef",
                            home_phone="7(900)9009090"))
    app.logout()



