# -*- coding: utf-8 -*-

from model.group import Group



def test_add_group(app):
        app.group.create(Group(name="111", header="2222", footer="333"))


def test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))



