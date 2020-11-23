import re


def test_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.email == clear(contact_from_edit_page.email)
    assert contact_from_home_page.email2 == clear(contact_from_edit_page.email2)
    assert contact_from_home_page.email3 == clear(contact_from_edit_page.email3)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.secondaryaddress == clear(contact_from_edit_page.secondaryaddress)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)
