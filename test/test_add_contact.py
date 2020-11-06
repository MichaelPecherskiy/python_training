# -*- coding: utf-8 -*-
from model.contact import Contact


def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="qaa", lastname="qaa", company="qaqaa", home="qwea",
        work="qwae", email="qwae@qa.qa", bday="25", bmonth="December", byear="1999"))
    app.session.logout()
