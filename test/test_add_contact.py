# -*- coding: utf-8 -*-
from model.contact import Contact


def test_untitled_test_case(app, db, json_contact, check_ui):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
