import pytest

@pytest.fixture()
def fixtures_ready():
    print('head')
    yield
    print("down")

def test_one(fixtures_ready):
    print("im in")