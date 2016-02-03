# -*- coding: utf-8 -*-

from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Michael", middlename="J", lastname="Fox", nickname="Marty", title="Back to the Future", company="Marty Inc", address="New York", homenumber="123456",
                               mobilenumber="789101112", faxnumber="17181920", worknumber="13141516", email="michael.foxj.@marty-inc", email2="michael.foxj2.@marty-inc",
                               email3="michael.foxj3.@marty-inc", homepage="btf.ru", byear="1970", address2="Street", ayear="2000", phone2="q", notes="q"))
    app.session.logout()


