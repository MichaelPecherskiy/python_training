from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                                    company="company", title="title", address="address", homephone="home", mobilephone="mobile",
                                    workphone="work", fax="fax", email="email", email2="email2", email3="email3", homepage="homepage",
                                    address2="address2", secondaryphone="phone2", notes="notes"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    m_contact = Contact(firstname="New contact", lastname="New lastname")
    app.contact.modify_contact_by_id(contact.id, m_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    old_contacts = app.contact.get_contact_list()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)