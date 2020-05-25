# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.digits + "(" + ")" + "+" + "-" + " "
    return "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_email(prefix, maxlen1, maxlen2):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    first = "".join([random.choice(symbols) for i in range(random.randrange(maxlen1))])
    second = "".join([random.choice(symbols) for i in range(random.randrange(maxlen2))])
    return prefix + first + "@" + second

testdata = [Contact(
    firstname=random_string("firstname", 10),
    lastname=random_string("lastname", 10),
    nickname=random_string("nickname", 10),
    home_phone=random_number(10),
    mobile_phone=random_number(10),
    work_phone=random_number(10),
    secondary_phone=random_number(10),
    email1=random_email("email1", 10,5),
    email2=random_email("email2", 10,5),
    email3=random_email("email3", 10,5),
    address=random_string("address", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



