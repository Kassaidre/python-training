
from model.group import Group

def test_edit_first_group(app):
        app.session.login(username="admin", password="secret")
        app.group.edit_first_group(Group(name="change", header="change1", footer="change2"))
        app.session.logout()