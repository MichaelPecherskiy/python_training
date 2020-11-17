from model.contact import Contact


def test_modified_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modified_contact(Contact(firstname="qa", lastname="qa", company="qaqa", home="qwe",
                                         work="qwe", email="qwe@qa.qa"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
