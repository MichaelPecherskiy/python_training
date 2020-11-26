# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="",
                    lastname="",
                    company="",
                    homephone="",
                    workphone="",
                    email="",
                    mobilephone="",
                    secondaryphone="",
                    email2="",
                    email3="",
                    address="",
                    )] + [
    Contact(firstname=random_string("name", 10),
            lastname=random_string("lastname", 20),
            company=random_string("company", 20),
            homephone=random_string("home", 20),
            workphone=random_string("work", 20),
            email=random_string("email", 20),
            mobilephone=random_string("mobile", 20),
            secondaryphone=random_string("phone2", 20),
            email2=random_string("email2", 20),
            email3=random_string("email3", 20),
            address=random_string("address", 20))
    for name in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_untitled_test_case(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    #contact = Contact(firstname="test",
                      #lastname="test1",
                      #company="test2",
                      #homephone="12345",
                      #workphone="12345",
                      #email="qwae@qa.qa",
                      #mobilephone="12345",
                      #secondaryphone="12345",
                      #email2="qwae@qa.qa",
                      #email3="qwae@qa.qa",
                      #address="test4",
                      #)