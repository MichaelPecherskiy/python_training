
def test_modified_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modified_group()
    app.session.logout()