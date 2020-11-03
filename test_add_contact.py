# -*- coding: utf-8 -*-
from app_test import Apptest
from contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Apptest()
    request.addfenalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="qa", lastname="qa", company="qaqa", home="qwe",
    work="qwe", email="qwe@qa.qa", bday="26", bmonth="December", byear="1997"))
    app.logout()
