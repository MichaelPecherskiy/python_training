from model.group import Group


def test_modified_group(app):
    old_groups = app.group.get_group_list()
    app.group.modified_group(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

