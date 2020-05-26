from model.contact import Contact
from random import randrange


def test_show_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="79009009090",
                           mobile_phone="901111",
                           work_phone="80245",
                           secondary_phone='7(902)001',
                           email1="mail1@mail.ru", email2="mail2@mail.ru", email3="mail3@mail.ru",
                           address="Address one"))
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact = all_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #ниже проверяются все телефоны методом обратной проверки. Слияние всех телефонов положено в функцию в app.contact
    assert contact.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    #ниже проверяются все email методом обратной проверки. Слияние всех email положено в функцию в app.contact
    assert contact.all_email == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact.firstname == contact_from_edit_page.firstname
    assert contact.lastname == contact_from_edit_page.lastname
    assert contact.address == contact_from_edit_page.address

