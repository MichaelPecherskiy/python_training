import re
from model.contact import Contact


def test_contact_db_ui(app, db):
    ui = app.contact.get_contact_list()
    print("ui", ui)

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                          address=contact.address.strip(),
                          all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                          all_emails_from_home_page=merge_emails_like_on_home_page(contact))
    db = map(clean, db.get_contact_list())
    print("db", db)
    assert sorted(ui, key=Contact.id_or_max) == sorted(db, key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [
                                                                contact.homephone,
                                                                contact.workphone,
                                                                contact.mobilephone,
                                                                contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None, [
                                                                contact.email,
                                                                contact.email2,
                                                                contact.email3]))))


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None, [
                                        contact.address
                                        ]))))
