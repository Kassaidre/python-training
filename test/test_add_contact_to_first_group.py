from model.contact import Contact
from model.group import Group
import random

def test_add_to_group(app, db):
    if len(db.get_group_list()) == 0:
               app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
               app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)




