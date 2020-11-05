# -*- coding: utf-8 -*-


def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact()
    app.session.logout()
