from model.contact import Contact


def test_modified_contact(app):
    app.contact.modified_contact(Contact(firstname="qa", lastname="qa", company="qaqa", home="qwe",
                                         work="qwe", email="qwe@qa.qa"))
