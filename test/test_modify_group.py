from model.group import Group
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified", header="modified", footer="modified")
    group.id = old_groups[index].id
    app.group.modify_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first(Group(name="New group"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)