from model.contact import Contact


def test_modified_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modified_contact(Contact(firstname="qa", lastname="qa", company="qaqa", home="qwe",
        work="qwe", email="qwe@qa.qa", bday="26", bmonth="December", byear="1997"))
    app.session.logout()