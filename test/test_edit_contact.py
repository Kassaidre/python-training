
from model.contact import Contact


def test_edit_first_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.edit_first_contact(Contact(firstname="Michael123", middlename="", lastname="", nickname="", title="", company="", address="", homenumber="",
                               mobilenumber="", faxnumber="", worknumber="", email="", email2="",
                               email3="", homepage="", byear="", address2="", ayear="", phone2="", notes=""))
        app.session.logout()