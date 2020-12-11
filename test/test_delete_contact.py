from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                                    company="company", title="title", address="address", homephone="home", mobilephone="mobile",
                                    workphone="work", fax="fax", email="email", email2="email2", email3="email3", homepage="homepage",
                                    address2="address2", secondaryphone="phone2", notes="notes"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=contact.id_or_max)