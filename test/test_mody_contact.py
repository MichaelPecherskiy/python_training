from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    contact = Contact(firstname="New contact")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)