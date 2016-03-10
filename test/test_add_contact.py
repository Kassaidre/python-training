# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, db, json_contacts):
        contact = json_contacts
        old_contacts = db.get_contact_list()
        app.contact.create(contact)
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










#contact = Contact(firstname="Michael", middlename="J", lastname="Fox", ni111ckname="Marty",
#                                   title="Back to the Future", company="Marty Inc", address="New York",
#                                   home="123456", mobile="789101112", fax="17181920",
#                                   work="13141516", email="michael.foxj.@marty-inc",
        #                                    email2="michael.foxj2.@marty-inc", email3="michael.foxj3.@marty-inc",
#                                   homepage="btf.ru", byear="1970", address2="Street", ayear="2000", phone2="q",
#                                   notes="q")