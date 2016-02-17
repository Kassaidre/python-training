# -*- coding: utf-8 -*-

from model.contact import Contact




def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(Contact(firstname="Michael", middlename="J", lastname="Fox", nickname="Marty",
                                   title="Back to the Future", company="Marty Inc", address="New York",
                                   home="123456", mobile="789101112", fax="17181920",
                                   work="13141516", email="michael.foxj.@marty-inc",
                                   email2="michael.foxj2.@marty-inc", email3="michael.foxj3.@marty-inc",
                                   homepage="btf.ru", byear="1970", address2="Street", ayear="2000", phone2="q",
                                   notes="q"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)

