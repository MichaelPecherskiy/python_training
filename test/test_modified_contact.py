
def test_modified_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modified_contact()
    app.session.logout()