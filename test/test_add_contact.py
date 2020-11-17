# -*- coding: utf-8 -*-
from model.contact import Contact


def test_untitled_test_case(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test", lastname="test1", company="test2", home="test3",
                                       work="test4", email="qwae@qa.qa")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

