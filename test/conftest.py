from fixture.application import Application
from fixture.app_test import Apptest
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def app(request):
    fixture = Apptest()
    request.addfinalizer(fixture.destroy)
    return fixture