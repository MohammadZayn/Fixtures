import pytest


@pytest.fixture(scope='class' )
def setup():
    print('I will execute the first google driver setup')
    yield
    print("I will execute last in row")


@pytest.fixture()
def dataload():
    print('User profile data is being created')
    return ["rahul","zyan","www.google.com"]