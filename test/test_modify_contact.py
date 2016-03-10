from model.contact import Contact
from random import randrange


def test_modify_some_contact(app, db, check_ui):
        if app.contact.count() == 0:
                app.contact.create(Contact(middlename="test"))
        old_contacts = db.get_contact_list()
        contact = Contact(home="111", mobile= "222", work="333", phone2="444")
        index = randrange(len(old_contacts))
        contact.id = old_contacts[index].id
        contact.firstname = old_contacts[index].firstname
        contact.lastname = old_contacts[index].lastname
        app.contact.modify_contact_by_index(index, contact)
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[index] = contact
        def clean(contact):
                return Contact(id=contact.id, firstname=contact.firstname.strip())
        new_contacts = map(clean, db.get_contact_list())
        new_contacts_1 = map(clean, app.contact.get_contact_list())
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts_1, key=Contact.id_or_max)

