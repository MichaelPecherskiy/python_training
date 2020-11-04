# -*- coding: utf-8 -*-
from fixture.app_test import Apptest
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Apptest()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="qa", lastname="qa", company="qaqa", home="qwe",
                       work="qwe", email="qwe@qa.qa", bday="26", bmonth="December", byear="1997"))
    app.session.logout()
