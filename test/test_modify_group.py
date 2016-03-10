from model.group import Group
import random
from random import randrange

def test_modify_group_name(app, db, check_ui):
        if len(db.get_group_list()) == 0:
                app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
        index = randrange(len(old_groups))
        group = Group(name = "New group")
        group.id = old_groups[index].id
        app.group.modify_group_by_index(index, group)
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        def clean(group):
                return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        new_groups_1 = map(clean, app.group.get_group_list())
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(new_groups_1, key=Group.id_or_max)