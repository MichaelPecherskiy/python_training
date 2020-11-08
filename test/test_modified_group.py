from model.group import Group


def test_modified_group(app):
    app.group.modified_group(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))


