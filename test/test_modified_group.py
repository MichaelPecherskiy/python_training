from model.group import Group


def test_modified_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modified_group(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    app.session.logout()


