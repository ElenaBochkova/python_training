from model.contact import Contact
from random import randrange


def test_show_contact_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="79009009090",
                           mobile_phone="901111",
                           work_phone="80245",
                           secondary_phone='7(902)001',
                           email1="mail1@mail.ru", email2="mail2@mail.ru", email3="mail3@mail.ru",
                           address="Address one"))
    all_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    all_contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    i = 0
    for contact in all_contacts:
        contact_from_db = all_contacts_from_db[i]
        i = i+1
        #ниже проверяются все телефоны методом обратной проверки. Слияние всех телефонов положено в функцию в app.contact
        assert contact.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_db)
        #ниже проверяются все email методом обратной проверки. Слияние всех email положено в функцию в app.contact
        assert contact.all_email == app.contact.merge_emails_like_on_home_page(contact_from_db)
        assert contact.firstname == contact_from_db.firstname
        assert contact.lastname == contact_from_db.lastname
        assert contact.address == contact_from_db.address

