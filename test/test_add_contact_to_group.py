from model.group import Group
from model.contact import Contact
import random

def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New",
                               lastname="Contact",
                               nickname="test",
                               home_phone="79009009090",
                                   mobile_phone="901111",
                                   work_phone="80245",
                                   secondary_phone='7(902)001',
                                   email1="mail1@mail.ru", email2="mail2@mail.ru", email3="mail3@mail.ru",
                                   address="Address one"))
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    if contact in (orm.get_contacts_in_group(group)):
        app.contact.delete_contact_from_group(contact, group)
    app.contact.add_contact_to_group(contact, group)
    assert contact in orm.get_contacts_in_group(group)
