# -*- coding: utf-8 -*-
from model.contact import Contact


def test_untitled_test_case(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test",
                      lastname="test1",
                      company="test2",
                      homephone="12345",
                      workphone="12345",
                      email="qwae@qa.qa",
                      mobilephone="12345",
                      secondaryphone="12345",
                      email2="qwae@qa.qa",
                      email3="qwae@qa.qa",
                      address="test4",
                      )
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

