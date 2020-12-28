from model.group import Group


def test_modified_group(app, db):
    old_groups = db.get_group_list()
    app.group.modified_group(Group(name="qweqwe", header="qweqwe", footer="qweqwe"))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

